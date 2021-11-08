#............................................................
# Imports
from decouple import config
import os
import sys
import functionalities.getUsrList as usr 
import functionalities.readMessages as read 
import functionalities.registrationLogin as regLog 
import functionalities.sendMessage as send 
import graphic as graph

#............................................................
# Global variables

username = ''
application_name = ''

#............................................................


def exitSelected():
    return 0

def parseUsername(user):
    invalidChars = [',', ';', '.', ':', '/', "'"]
    for c in invalidChars:
        if c in user:
            return False
    return True 

def signUpSelected(operationCode, user=None):
    
    # parsing user input
    isValid = parseUsername(user)
    if not isValid:
        print('Error: username cannot contain following chars:')
        print("',', ';', '.', ':', '/', '''\n")
        return None

    # the following invocation returns the lambda function return value. 
    # It's a String value:
    #   'true' stands for registration done
    #   The error message of the lamda's invocation
    lambda_response = regLog.registrationLogin(operationCode, user)

    if lambda_response == 'true': 
        print('Success.\n')
        return 1
    else:
        print('Error: {}\n'.format(lambda_response))
        return None

def loginSelected(operationCode, user=None):
    global username
    
    lambda_response = regLog.registrationLogin(operationCode, user)

    if lambda_response == 'true': 
        print('Success.\n')
        username = user
        return 2
    else:
        print('Error: {}\n'.format(lambda_response))
        return None


def getUsersList():
    l = usr.getUsrList()
    print(l, '\n')
    return 1

def readAllMessages():
    global username
    read.getMessages(username) 
    return 2

def readNewMessages():
    global username
    read.getMessages(username, False) 
    return 3

def sendMessage(params):
    send.sendMessage(params)
    return 4

def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    
def commandLineClient():
    print()
    
    check = -1
    loginDone = False
    base_prompt = '>> '

    while check != 0:
        if (loginDone):
            prompt = 'user: {} '.format(username) + base_prompt
        else:
            prompt = base_prompt

        usr_input = input(prompt)
        
        # parsing the input. the second param is needed because if login has
        # been done, user cannot performe a registration or login anymore,
        # otherwise it cannot performe a send, read or get the users list
        check = commandLineParser(usr_input, loginDone)
        if not loginDone and check == 2:
            loginDone = True
    return 



def commandLineParser(user_input, loginDone):
    tmp_params = user_input.split(' ')
    params = []
    for i in tmp_params:
        params += i.split(',')
    while '' in params:
        params.remove('')

    if len(params) == 0:
        # just show a new line
        return 
    # first element is the cmd to execute
    main_command = params[0]

    # checking if it's a clear, help or exit command. Same behaviour in any
    # case for these commands:

    if main_command == 'exit':
        # checking for no params:
        if len(params) != 1:
            print('Error: too mach params.\n')
            return 1
        else:
            return exitSelected()

    elif main_command == 'clear':
        # checking for no params:
        if len(params) != 1:
            print('Error: too mach params.\n')
            return 1
        else:
            return clear()

    elif main_command == 'help':
        # checking for no params:
        if len(params) != 1:
            print('Error: too mach params.\n')
            return 1
        else:
            return showHelp()


    if not loginDone:
        # only clear, exit, reg, log will be accepted:

        # parsing main cmd: 
        if main_command == 'reg':
            # reg -u <user>
            if len(params) != 3:
                print('Error: you have to specify user.\n')
                return 1

            if params[1] != '-u':
                print('Error: invalid option.\n')
                return 1

            signUpSelected(1, params[2])
            return 1
        elif main_command == 'log':
            # log -u <user>
            if len(params) != 3:
                print('Error: you have to specify user.\n')
                return 1

            if params[1] != '-u':
                print('Error: invalid option.\n')
                return 1

            return loginSelected(2, params[2])
        else: 
            print('Error: command not found.\n')
    # login Done. usr list, send and read (all and new) accepted
    else:
        if main_command == 'usr_list':
            # usr_list
            if len(params) != 1:
                print('Error: too mach params.\n')
                return 1

            return getUsersList() 

        elif main_command == 'read':
            # read      or      read -n

            if len(params) == 1: # only the read command
                readAllMessages()
                return 
            elif len(params) > 2: # the name and 2 or more params
                print('Error: too much argument.\n')
                return 2
            # we have a param. check if it's the -n
            if params[1] != '-n':
                print('Error: invalid option.\n')
                return 2
            else:
                readNewMessages()
                return

        elif main_command == 'send':
            # send -u <user1>, <user2>,<user3> .. <user_n> -o <object>
            if len(params) < 3:
                print('Error: no user given.\n')
                return 4

            if params[1] != '-t':
                print('Error: invalid option.\n')
                return 4
            
            usr_list = []
            oOptionFound = False 
            for i in range(2, len(params)):
                curr = params[i]
                if curr.endswith(','):
                    curr = curr[:-1]
                if (curr == '-o'):
                    oOptionFound = True
                    break
                usr_list.append(curr)

            # checking if cycle ends because of break or just because the
            # params are finished. In this case, the -o option is missing

            if not oOptionFound:
                print('Error: missing -o option for object.\n')
                return 4
            # checking if params is correctly len size:
            # if everything was correct, now we have i that is the -o index,
            # then just check if the i+1-th element of param exists:
            #
            if i + 1 == len(params):
                print('Error: missing object.\n')
                return 4
            obj_ = params[i + 1]
            for j in range(i + 2, len(params)):
                obj_ += ' ' + params[j]

            lambdaParams = {}
            lambdaParams['receivers'] = usr_list
            #lambdaParams['object'] = params[i + 1]
            lambdaParams['object'] = obj_
            lambdaParams['body'] = None
            global username
            lambdaParams['sender'] = username
            lambdaParams['reply'] = False
            sendMessage(lambdaParams)
            return 2
        else: 
            print('Error: command not found.\n')

    return 


def showHelp():
    print('Command Line application works with the following:\n')

    print("From command shell:")
    print('\tStarting client with basical graphic support:')
    print('\t\t$ {} -g '.format(application_name))
    print('\tShowing this help message:')
    print('\t\t$ {} -h\n'.format(application_name))
    
    print('\tAt any time in the application:')
    print('\tClearing the screen:')
    print('\t\t>> clear')
    print('\tShowing this help message:')
    print('\t\t>> help')
    print('\tClosing the application:')
    print('\t\t>> exit\n')

    print("Before logging in:")
    print('\tSigning up to the system (note that password will be asked \
interactively):')
    print('\t\t>> reg -u <username_with_wich_signing_up>')
    print('\tLogging in to the system (note that password will be asked \
interactively):')
    print('\t\t>> log -u <username_with_wich_loging_in>\n')

    print("After logging in:")
    print('\tClearing the screen:')
    print('\t\t>> clear')
    print('\tRetrieving the user list to which you can send messages:')
    print('\t\t>> usr_list')
    print('\tReading all the messages:')
    print('\t\t>> read')
    print('\tReading only the new messages:')
    print('\t\t>> read -n')
    print('\tSending a messages to one or more users (note that message \
body will be asked interactively):')
    print('\t\t>> send -t <dest1> <dest2> ... <dest_n> -o <object> \n')
    return 


if __name__ == '__main__':
    application_name = sys.argv[0]

    if not config('use_credentials_file', default=True, cast=bool):
        # setting up environ variables:
        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config ('AWS_SECRET_ACCESS_KEY')
        AWS_SESSION_TOKEN = config('AWS_SESSION_TOKEN')
        os.environ['AWS_ACCESS_KEY_ID'] = AWS_ACCESS_KEY_ID
        os.environ['AWS_SECRET_ACCESS_KEY'] = AWS_SECRET_ACCESS_KEY
        os.environ['AWS_SESSION_TOKEN'] = AWS_SESSION_TOKEN 

    if len(sys.argv) == 2: # there are params
        if (sys.argv[1] == '-g'):
            graph.main()
            #graphicClient()  
        if (sys.argv[1] == '-h'):
            showHelp()
        else: 
            print('Invalid params.\n')
            showHelp()
        
    else:
        commandLineClient()

