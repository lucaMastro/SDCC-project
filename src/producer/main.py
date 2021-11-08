#---------------------------------------------
from decouple import config
import os
import sys
import functionalities.getUsrList as usr 
import functionalities.readMessages as read 
import functionalities.registrationLogin as regLog 
import functionalities.sendMessage as send 
import graphic 
#---------------------------------------------
# Global variables
username = ''
application_name = ''
loginDone = False
#---------------------------------------------
# return codes
exit_code = 1
#---------------------------------------------


def isUsernameValid(user):
    # this function prevent an username to have the following chars: the
    # sign-up will be aborted
    invalidChars = [',', ';', '.', ':', '/', "'"]
    for c in invalidChars:
        if c in user:
            return False
    return True 

def signUpSelected(user=None):
    # the sign-up code is 1: it's needed because registration and login are
    # performed by the same client function
    sign_up_code = 1

    # parsing user input
    isValid = isUsernameValid(user)
    if not isValid:
        print('Error: username cannot contain following chars:')
        print("',', ';', '.', ':', '/', '''\n")
    else:
        # the following invocation returns the lambda function return value. 
        # It's a String value:
        #   - 'true', that stands for registration done
        #   - The error message of the lamda's invocation
        lambda_response = regLog.registrationLogin(sign_up_code, user)
        if lambda_response == 'true': 
            print('Success.\n')
        else:
            print('Error: {}\n'.format(lambda_response))


def loginSelected(user=None):
    global username
    global loginDone 

    # the log-in code is 2: it's needed because registration and login are
    # performed by the same client function
    log_in_code = 2

    # invoke lambda function and check result
    lambda_response = regLog.registrationLogin(log_in_code, user)
    if lambda_response == 'true': 
        print('Success.\n')
        username = user
        loginDone = True
    else:
        print('Error: {}\n'.format(lambda_response))


def getUsersList():
    # invoke lambda function 
    l = usr.getUsrList()
    print(l, '\n')

def readAllMessages():
    global username
    read.getMessages(username) 

def readNewMessages():
    global username
    read.getMessages(username, False) 

def sendMessage(params):
    send.sendMessage(params)

def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    

def commandLineClient():
    global loginDone
    global username

    print()
    base_prompt = '>> '

    while True:
        if (loginDone):
            prompt = 'user: {} '.format(username) + base_prompt
        else:
            prompt = base_prompt

        # getting command
        cmd = input(prompt)
        # parsing the input. 
        check = commandLineParser(cmd, loginDone)
        if check == exit_code:
            break
    return 



def commandLineParser(cmd, loginDone):
    global username
    
    # from a string to a list of [cmd, param_1, ..., param_n]
    tmp_params = cmd.split(' ')
    params = []
    for i in tmp_params:
        params += i.split(',')
    while '' in params:
        params.remove('')

    if len(params) == 0:
        # just show a new line: no cmd given
        return 

    # first element is the cmd to execute
    main_command = params[0]

    # checking if it's a clear, help or exit command. Same behaviour in any
    # case for these commands:
    if main_command == 'exit':
        # checking for no other params:
        if len(params) != 1:
            print('Error: too much params.\n')
            return 
        else:
            return exit_code 

    elif main_command == 'clear':
        # checking for no params:
        if len(params) == 1:
            clear()
        else:
            print('Error: too much params.\n')
        return

    elif main_command == 'help':
        # checking for no params:
        if len(params) == 1:
            showHelp()
        else:
            print('Error: too much params.\n')
        return 


    if not loginDone:
        # only reg, log will be accepted:
        # parsing main cmd: 
        if main_command == 'reg':
            # reg -u <user>
            if len(params) > 3:
                print('Error: too much arguments.\n')
                return 
            elif len(params) < 3:
                print('Error: too few arguments.\n')
                return 

            if params[1] != '-u':
                print('Error: invalid option.\n')
                return 
            signUpSelected(params[2])
            return 

        elif main_command == 'log':
            # log -u <user>
            if len(params) > 3:
                print('Error: too much arguments.\n')
                return 
            elif len(params) < 3:
                print('Error: too few arguments.\n')
                return 

            if params[1] != '-u':
                print('Error: invalid option.\n')
                return
            loginSelected(params[2])
            return 
        else: 
            print('Error: command not found.\n')

    else:
    # login Done == True. usr list, send and read (all and new) accepted
        if main_command == 'usr_list':
            # usr_list
            if len(params) == 1:
                getUsersList()
            else:
                print('Error: too much params.\n')
            return  

        elif main_command == 'read':
            # read      or      read -n
            if len(params) == 1: # only the read command
                readAllMessages()
            elif len(params) > 2: 
                print('Error: too much argument.\n')
            else:
                # len(params) == 2
                # we have a param. check if it's the -n
                if params[1] != '-n':
                    print('Error: invalid option.\n')
                else:
                    readNewMessages()
            return

        elif main_command == 'send':
            # send -u <user1>, <user2>,<user3> .. <user_n> -o <object>
            if len(params) < 5:
                # send -t <user> -o <object>
                print('Error: no user given.\n')
                return 

            if params[1] != '-t':
                print('Error: invalid option.\n')
                return 
            
            usr_list = []
            # checking for -o while scan the list of destination
            oOptionFound = False 
            for i in range(2, len(params)):
                curr = params[i].strip(',')
                if (curr == '-o'):
                    oOptionFound = True
                    break
                usr_list.append(curr)

            # checking if cycle ends because of break or just because the
            # params are finished. In this case, the -o option is missing
            if not oOptionFound:
                print('Error: missing -o option for object.\n')
                return 

            # checking if params is correctly len size:
            # if everything was correct, now we have i that is the -o index.
            # the last element of the params is in the len(params) - 1.
            # Then, if i + 1 == len(params) means that -o was the last element
            # of params list
            if i + 1 == len(params):
                print('Error: missing object.\n')
                return 
            
            # getting object
            obj_ = params[i + 1]
            # if there are other params in the list, then the object has space.
            # recostruction of the object
            for j in range(i + 2, len(params)):
                obj_ += ' ' + params[j]

            # preparing lambda invocation
            lambdaParams = {}
            lambdaParams['receivers'] = usr_list
            lambdaParams['object'] = obj_
            lambdaParams['body'] = None
            lambdaParams['sender'] = username   #global
            lambdaParams['reply'] = False
            sendMessage(lambdaParams)
            return 
        else: 
            # undefined main_cmd
            print('Error: command not found.\n')

    return 


def showHelp():
    # this is just a print function
    print('Command Line application works with the following:\n')

    print("From command shell:")
    print('\tStarting client with CLI support:')
    print('\t\t$ python {}'.format(application_name))
    print('\tStarting client with basical graphic support:')
    print('\t\t$ python {} -g'.format(application_name))
    print('\tShowing this help message:')
    print('\t\t$ python {} -h\n'.format(application_name))
    
    print('At any time in the application (not during read sub-shell):')
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
    print('\tRetrieving the user list to which you can send messages:')
    print('\t\t>> usr_list')
    print('\tReading your [only new] messages:')
    print('\t\t>> read [-n]')
    print('\tSending a messages to one or more users (note that message \
body will be asked interactively):')
    print('\t\t>> send -t <dest1> <dest2> ... <dest_n> -o <object> \n')


if __name__ == '__main__':
    application_name = sys.argv[0]

    # checking how to retrieve credentials
    if not config('use_credentials_file', default=True, cast=bool):
        # setting up environ variables:
        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config ('AWS_SECRET_ACCESS_KEY')
        AWS_SESSION_TOKEN = config('AWS_SESSION_TOKEN')
        os.environ['AWS_ACCESS_KEY_ID'] = AWS_ACCESS_KEY_ID
        os.environ['AWS_SECRET_ACCESS_KEY'] = AWS_SECRET_ACCESS_KEY
        os.environ['AWS_SESSION_TOKEN'] = AWS_SESSION_TOKEN 

    if len(sys.argv) > 2:
        print('Too much params.\n')

    elif len(sys.argv) == 2: 
        # there are params: the only valid optios are '-g' and '-h'
        
        if (sys.argv[1] == '-g'):
            # GUI mode
            graphic.main()

        if (sys.argv[1] == '-h'):
            showHelp()
        else: 
            print('Invalid params.\n')
    else:
        commandLineClient()

