import boto3
import json
import ast
import signal
import sys 

import functionalities.deleteMessagesAndMarkAsRead as delAndMark
import functionalities.Message as mess 

messagesList = []

# class for manage use case: it's a subclass of Message
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


def getMessages(username, all_ = True, graphic=False):
    
    global messagesList 

    messagesList = MessageList() 

    client = boto3.client('lambda')
    input_params = {}
    input_params['All'] = all_ 
    input_params['Username'] = username
    response = client.invoke( FunctionName='read_messages',
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps(input_params), )

    strPayload = response['Payload'].read().decode('utf-8')
    payload = ast.literal_eval(strPayload)

    # filling messagesList with the bodies
    i = 0
    for keyIndex in payload.keys():
        msgStr = payload[keyIndex]['message']
        
        if payload[keyIndex]['new'] == 'True':
            isNew = True
        else:
            isNew = False 

        key = payload[keyIndex]['key']

        messagesList.append(ToDisplayMessage(msgStr, i, key, isNew))
        i += 1
        #messagesList.append(payload[key]['message'])

    if not graphic:
        showMessages(username, all_)
        

# CLI read-messages support
def showMessages(username, all_):
    global messagesList

    # command line changing handler for ctrl +c: in this way, even if a ctrl+c
    # is execute, the changes will be sent to aws
    # this is needed to restore default status
    default_handler = signal.getsignal(signal.SIGINT)
    # changing handler:
    signal.signal(signal.SIGINT, signalHandler)
    
    s = "You don't have any " 
    if (len(messagesList) == 0):
        if not all_:
            s += 'new '
        s += "message to display."
        print(s)
        return

    if (all_):
        print("You have {} messages to display.".format(len(messagesList)))
    else:
        print("You have {} new messages to display.".format(len(messagesList)))
    
    current = 0
    while current < len(messagesList):
        print('-' * 60)
        print('index: {}\tNew: {}\n'.format(current + 1,
            messagesList[current].isNew))
        print('.' * 30)
        print(messagesList[current])
        print('.' * 30)

        messagesList[current].read = True 

        print('Give me a command:')
        print('c = show next, b = break, d = delete this message, j <n>' +
        ' = show n-th message\n')
        cmd = input('user: {} - read >> '.format(username))

        if cmd == 'c':
            current += 1
        elif cmd == 'b':
            break
        elif cmd == 'd':
            messagesList.delete(current)
            # not increment: the current-th message is changed
            #current += 1
        else:
            # expecting a j n command
            params = cmd.split(' ')
            while '' in params:
                params.remove('')

            if len(params) != 2 or params[0] != 'j':
                print('Invalid input.\n')
                continue

            try:
                n = int(params[1])
            except:
                print("Second param should be an integer.\n")
                continue

            if n > len(messagesList):
                print("You only have {} messages.\n".format(len(messagesList)))
                continue
            
            # n-th mess is in n-1 position
            current = n - 1

    # all messages have ben read
    if current == len(messagesList):
        print("You don't have other messages.")
    
    # make changes on aws
    prepareAndInvokeDelete()
    # restoring previous handler:
    signal.signal(signal.SIGINT, default_handler)

def signalHandler(*args):
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

if __name__ == '__main__':
    #payload = '["From: luca\nTo: luca\nObject: test2\nBody: provaprova\n\n", "From: luca\nTo: luca\nObject: asd\nBody: prova\n\n"]'
    #print(payload)
    
    # testing not graphic case
    
    # reporting to list:
    # suppoose to have it
    #
    # interactive shell
#    payloadList = ["From: luca\nTo: luca\nObject: test2\nBody: provaprova\n\n", "From: luca\nTo: luca\nObject: asd\nBody: prova\n\n"]

 #   if (len(payloadList) == 0):
  #      print("You don't have any message to display.")
   # else:
    #    endIndex = showMessages(payloadList)
    
   # if endIndex == len(payloadList):
    #    print("You don't have other messages.")
    print(getMessages('luca'))
