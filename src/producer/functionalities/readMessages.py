import boto3
import json
import ast
import signal
import sys 
from functools import partial
#---------------------------------------------
import functionalities.deleteMessagesAndMarkAsRead as delAndMark
import functionalities.Message as mess 
import gui_support.support_functions as supp 
import functionalities.sendMessage as send 
#---------------------------------------------

messagesList = []

# class for manage use case
#---------------------------------------------
# this is a subclass of Message
#
class ToDisplayMessage(mess.Message):
    deleted = False
    read = False 
    index = None
    key = ''
    isNew = None 

    def __init__(self, msgString, position, key, new):
        super().__init__(msgString) # filling Message's field
        self.index = position 
        self.key = key 
        self.isNew = new 


class MessageList():
    toDisplayMessageList = []
    numOfDeleted = 0

    def __init__(self):
        self.toDisplayMessageList = list()
        self.numOfDeleted = 0

    def __len__(self):
        return len(self.toDisplayMessageList) - self.numOfDeleted

    def append(self, item):
        self.toDisplayMessageList.append(item)

    def __getitem__(self, i):
        if i > len(self):
            raise IndexError('list index out of range')
        else:
            for item in self.toDisplayMessageList:
                if item.index == i and not item.deleted:
                    return item

    def delete(self, i):
        if i >= len(self):
            raise IndexError('list index out of range')
        else:
            item = self[i]
            item.deleted = True
            self.numOfDeleted += 1
            for i in range(i + 1, len(self.toDisplayMessageList)):
                self.toDisplayMessageList[i].index -= 1

    def getRead(self):
        l = []
        for i in self.toDisplayMessageList:
            if i.read:
                l.append(i)

    def __str__(self):
        s = '['
        for i in range(len(self) - 1):
            item = self[i]
            s += str(item) + ', '
        s += str(self[len(self) - 1]) + ']'
        return s

#---------------------------------------------

# this function invokes lambda function
def getMessages(username, all_ = True, graphic=False):
    global messagesList 

    messagesList = MessageList() 

    # prepare invocation
    input_params = {}
    input_params['All'] = all_ 
    input_params['Username'] = username

    # invoke and convert result
    client = boto3.client('lambda')
    response = client.invoke( FunctionName='read_messages',
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps(input_params), )

    strPayload = response['Payload'].read().decode('utf-8')
    payload = ast.literal_eval(strPayload)

    # filling messagesList with the bodies of returned mess
    i = 0
    for keyIndex in payload.keys():
        
        # getting returned information for all returned message
        #
        # isNew
        if payload[keyIndex]['new'] == 'True':
            isNew = True
        else:
            isNew = False 

        # key: s3 name
        key = payload[keyIndex]['key']

        # the string representing the message
        msgStr = payload[keyIndex]['message']

        # add a new ToDisplayMessage into the list
        messagesList.append(ToDisplayMessage(msgStr, i, key, isNew))
        i += 1

    # for CLI client, the messageList must be shown
    if not graphic:
        showMessages(username, all_)
        

def showMessages(username, all_):
    global messagesList

    # command line changing handler for ctrl+c: in this way, even if a sigint
    # occurs, the changes will be sent to aws.
    # 
    # storing the default behaviour: later the handler will be set at the
    # default
    default_handler = signal.getsignal(signal.SIGINT)
    # changing handler:
    signal.signal(signal.SIGINT, partial(signalHandler, False))
    
    # no message case:
    s = "You don't have any " 
    if (len(messagesList) == 0):
        if not all_:
            s += 'new '
        s += "message to display.\n"
        print(s)
        return

    if (all_):
        print("You have {} messages to display.".format(len(messagesList)))
    else:
        print("You have {} new messages to display.".format(len(messagesList)))
    
    # current is the index of the last message shown
    current = 0
    while current < len(messagesList):
        # print a message separator
        print('-' * 60)
        # printing message's attributes
        print('index: {}\tNew: {}\n'.format(current + 1,
            messagesList[current].isNew))
        # printing the message
        print('.' * 30)
        print(messagesList[current])
        print('.' * 30)

        # save that message has been read
        messagesList[current].read = True 

        # getting usr cmd
        print('Give me a command:')
        print('c = show next, b = break, d = delete this message, j <n>' +
        ' = show n-th message, r [<-a>] = reply [to all]\n')
        cmd = input('user: {} - read >> '.format(username))

        # parsing cmd:
        if cmd == 'c':
            current += 1
        elif cmd == 'b':
            print()
            break
        elif cmd == 'd':
            messagesList.delete(current)
            # current is not incremented: the current-th message is changed
        else:
            # expecting a "j n" or a "r [-a]" command 
            params = cmd.split(' ')
            while '' in params:
                params.remove('')

            if len(params) > 2:
                print('Error: too much params.\n')
                continue

            # reply case. may have argument
            if params[0] == 'r':
                curr_message = messagesList[current]
                dict_param = dict()

                # reply -all case
                if len(params) == 2:
                    if params[1] != '-a':
                        print('Error: invalid params.\n')
                        continue
                    else:
                        # getting the To field of message. it's a string like
                        # the following:
                        # 'usr1, usr2, ...'
                        old_receivers = curr_message.to

                        # getting a list type:
                        new_receivers = old_receivers.split(', ')

                        # deleting this user from the receivers list
                        new_receivers.remove(username)

                        # adding sender to the new receivers list:
                        if curr_message.from_ not in new_receivers:
                            new_receivers.append(curr_message.from_)
                        
                        # prepare lambda_send invocation:
                        dict_param['receivers'] = new_receivers 
                        dict_param['object'] = 'RE: ' + curr_message.object_ 
                        dict_param['sender'] = username 
                        dict_param['reply'] = True
                        dict_param['body'] = None
                        dict_param['graphic'] = False

                elif len(params) == 1:
                    # reply to the only sender case:
                    dict_param['receivers'] = [curr_message.from_]
                    dict_param['object'] = 'RE: ' + curr_message.object_ 
                    dict_param['sender'] = username 
                    dict_param['reply'] = True
                    dict_param['body'] = None
                    dict_param['graphic'] = False

                else: #len(params) > 2
                    print('Error: too much params.\n')
                    continue

                # starting send:
                print() # printing a new-line
                send.sendMessage(dict_param)
                print('Message(s) sent.\n')

            elif params[0] == 'j':

                # this case needs exactly 1 param other the 'j' cmd
                if len(params) > 2:
                    print('Error: too much params.\n')
                    continue
                if len(params) < 2:
                    print('Error: too few params.\n')
                    continue
                
                # try to cast the given value
                try:
                    n = int(params[1])
                except:
                    print("Second param should be an integer.\n")
                    continue

                # cannot show a message whose index is bigger than the list
                if n > len(messagesList):
                    print("You only have {} messages.\n".format(len(messagesList)))
                    continue
                
                # n-th mess is in n-1 position
                current = n - 1

            else:
                # params[0] != 'r' and params[0] != 'j'
                print('Invalid input.\n')
                continue
        
        #end params[0] switch
    # end-cycle

    # all messages have ben read
    if current == len(messagesList):
        print("You don't have other messages.\n")
    
    # make changes on aws
    prepareAndInvokeDelete()
    # restoring previous handler:
    signal.signal(signal.SIGINT, default_handler)


def signalHandler(graphic, signum, frame):
    if not graphic:
        print('\nPlease wait few seconds..\n')
    prepareAndInvokeDelete()
    sys.exit()

def prepareAndInvokeDelete():
    readMessages = []
    toDeleteMessages = [] 

    # scanning the complete list of messages:
    for i in messagesList.toDisplayMessageList: 
        # mark as read only if not deleted
        if i.deleted:
            toDeleteMessages.append(i.key)
        else:
            if i.read:
                readMessages.append(i.key)

    # if both lists are empty, no operation is needed:
    if readMessages != [] or toDeleteMessages != []:
        inputDict = {}
        for key in readMessages:
            inputDict[key] = 'mark'

        for key in toDeleteMessages:
            inputDict[key] = 'del'
        
        delAndMark.manageDelAndMark(inputDict)
