import boto3
import json
import ast

import functionalities.deleteMessagesAndMarkAsRead as delAndMark

readMessages = []
toDeleteMessages = []
messagesList = []
payload = None

def getMessages(username, all_ = True, graphic=False):
    
    global readMessages
    global toDeleteMessages
    global messagesList 
    global payload

    messagesList = []
    readMessages = []
    toDeleteMessages = []

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
    for key in payload.keys():
        messagesList.append(payload[key]['message'])

    if not graphic:
        showMessages(username, all_)
        prepareAndInvokeDelete()
        


def prepareAndInvokeDelete():
    global readMessages
    global toDeleteMessages 
    global payload 

    # now readMessages and toDeleteMessages lists are filled. use them to
    # create dict that will be used as input of lambda for deleting and marking
    # as read:

    # schedule messages to be mark as read. I'm going to remove indexes
    # relatives to messages that are already read:
    for i in range(len(payload)):
        if payload[str(i)]['new'] == 'False' and \
                i in readMessages:
                    readMessages.remove(i)
    # then, i don't want to mark as read a message that will be deleted:
    for i in toDeleteMessages:
        if i in readMessages:
            readMessages.remove(i)

    # following dict will keep pairs like <key-name-in-s3>:<operation>
    # where operation is 'del' or 'mark'
    # if both lists are empty, no operation is needed:
    if readMessages != [] or toDeleteMessages != []:
        inputDict = {}
        for i in readMessages:
            inputDict[payload[str(i)]['key']] = 'mark'

        for i in toDeleteMessages:
            inputDict[payload[str(i)]['key']] = 'del'
        
        delAndMark.manageDelAndMark(inputDict)

    # reinitializing payload
    payload = None


# CLI read-messages support
def showMessages(username, all_):
    global messagesList
    global readMessages
    global toDeleteMessages 
    global payload 

    if (len(messagesList) == 0):
        print("You don't have any message to display.")
        return

    if (all_):
        print("You have {} messages to display.".format(len(messagesList)))
    else:
        print("You have {} new messages to display.".format(len(messagesList)))
    
    current = 0
    while current < len(messagesList):
        print('-' * 60)
        print('index: {}\tNew: {}\n'.format(current + 1,
            payload[str(current)]['new']))
        print('.' * 30)
        print(messagesList[current])
        print('.' * 30)

        if current not in readMessages:
            readMessages.append(current)

        print('Give me a command:')
        print('c = show next, b = break, d = delete this message, j <n>' +
        ' = show n-th message\n')
        cmd = input('user: {} >> '.format(username))

        if cmd == 'c':
            current += 1
        elif cmd == 'b':
            break
        elif cmd == 'd':
            if current not in toDeleteMessages:
                toDeleteMessages.append(current)
            current += 1
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

    if current == len(messagesList):
        print("You don't have other messages.")


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
