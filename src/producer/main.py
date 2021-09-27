#............................................................
# Imports
import sys
import boto3
import functionalities.getUsrList as usr 
import functionalities.readMessages as read 
import functionalities.registrationLogin as regLog 
import functionalities.sendMessage as send 
import functionalities.GraphicClient as graph

#............................................................
# Global variables

username = ''
application_name = ''

#............................................................


def exitSelected():
    return 0

def signInSelected(operationCode, user=None):
    
    # following function returns the lambda function return value. It's
    # a Boolean value:
    #   True stands for registration done
    #   False stands for registration problem
    response_list = regLog.registrationLogin(operationCode, user)
    lambda_response = response_list[0]

    if lambda_response == 'true': 
        input('Signin done, press a key to continue')
        return 1
    else:
        input('Username still present retry')
        return None

def loginSelected(operationCode, user=None):
    global username
    
    response_list = regLog.registrationLogin(operationCode, user)
    lambda_response = response_list[0]
    username = response_list[1]

    if lambda_response == 'true': 
        input('Login has been done successfully. Press a key to continue')
        return 2
    else:
        input('Wrong username or password')
        return None



def showMainMenu():
    clear()
    print("......................................................................................")
    print("......................................................................................")
    print("................__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __..............")
    print("...............|                                                        |.............")
    print("...............|                   SYSTEM ACCESS POINT                  |.............")
    print("...............|__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __|.............")
    print("......................................................................................")
    print("......................................................................................")
    print("..........................   Welcome! Choose an option   .............................")
    print("......................................................................................")
    print("......................................................................................")
    print(".................._________..........._________..........._________...................")
    print(".................|         |.........|         |.........|         |..................")
    print(".................|   EXIT  |.........| SIGN IN |.........|  LOGIN  |..................")
    print(".................|   [0]   |.........|   [1]   |.........|   [2]   |..................")
    print(".................|_________|.........|_________|.........|_________|..................")
    print("......................................................................................")
    print("......................................................................................")
    print("......................................................................................")
    #need a try for invalid numbers
    mainMenuOptions = {
            0 : exitSelected,
            1 : signInSelected,
            2 : loginSelected
    }
    operation = int(input("Choose an operation: "))
    try:
        return mainMenuOptions[operation](operation)
    except Exception as e:
        print(str(e))
        print("Il valore inserito non è accettabile. Riprova")
        return -1



def logOut():
    #@TODO
    input('log out done, press a key to continue')
    return 0

def getUsersList():
    #@TODO
    a = usr.getUsrList()
    print(a)
    input('list done, press a key to continue')
    return 1

def readAllMessages():
    #@TODO
    input('read all done, press a key to continue')
    return 2

def readNewMessages():
    #@TODO
    input('read new done, press a key to continue')
    return 3

def sendMessage(usr_list = None):
    # param usr_list is not None only when is invoked by CLI-client
    global username 
    print(send.sendMessage(username, usr_list))
    input('send done, press a key to continue')
    return 4

def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    

def showMenu():
    clear()
    print(".....................................................................................")
    print("..............................|       USER MENU       |..............................")
    print(".....................................................................................")
    print(".....................................................................................")
    print("_________________________________Avaiable_Operations_________________________________")
    print("|                                                                                    |")
    print("|                                                                    [Log out: 0]    |")
    print("|    OPERATION 1 : Get the user's list                                               |")
    print("|    OPERATION 2 : Read all messages                                                 |")
    print("|    OPERATION 3 : Read new messages                                                 |")
    print("|    OPERATION 4 : Send a message                                                    |")
    print("|____________________________________________________________________________________|")


    menuOptions = {
            0 : logOut,
            1 : getUsersList,
            2 : readAllMessages,
            3 : readNewMessages,
            4 : sendMessage
    }
    operation = int(input("Choose an operation: "))
    print(operation)
    try:
        return menuOptions[operation]()
    except Exception as e:
        print(str(e))
        print("Il valore inserito non è accettabile. Riprova")
        return -1


def graphicClient():
    check = -1
    while check != 2: #2 is the value returned from a valid login

        if check == 0: #user selected exit procedure 
            sys.exit()
             
        check = showMainMenu()

    #restoring default value of check, and start the logged user menu loop
    check = -1
    while check != 0: #user selected exit procedure
        check = showMenu()


def commandLineClient():
    #TODO
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
    #TODO
    params = user_input.split(' ')

    # first element is the cmd to execute
    main_command = params[0]

    # checking if it's a clear, help or exit command. Same behaviour in any
    # case for these commands:

    if main_command == '':
        # just show a new line
        return
    elif main_command == 'exit':
        # checking for no params:
        if len(params) != 1:
            print('Error: too mach params.')
            return 1
        else:
            return exitSelected()

    elif main_command == 'clear':
        # checking for no params:
        if len(params) != 1:
            print('Error: too mach params.')
            return 1
        else:
            return clear()

    elif main_command == 'help':
        # checking for no params:
        if len(params) != 1:
            print('Error: too mach params.')
            return 1
        else:
            return showHelp()


    if not loginDone:
        # only clear, exit, reg, log will be accepted:

        menuOptions = {
                1 : signInSelected,
                2 : loginSelected
        }

        # parsing main cmd: 

        if main_command == 'reg':
            # reg -u <user>
            if len(params) != 3:
                print('Error: you have to specify user.')
                return 1

            if params[1] != '-u':
                print('Error: invalid option.')
                return 1

            menuOptions[1](1, params[2])
            return 1
        elif main_command == 'log':
            # log -u <user>
            if len(params) != 3:
                print('Error: you have to specify user.')
                return 1

            if params[1] != '-u':
                print('Error: invalid option.')
                return 1

            menuOptions[2](2, params[2])
            return 2

        
        else: 
            print('Error: command not found.')
    
    else:
        menuOptions = {
                1 : getUsersList,
                2 : readAllMessages,
                3 : readNewMessages,
                4 : sendMessage,
        }

        if main_command == 'usr_list':
            # usr_list
            if len(params) != 1:
                print('Error: too mach params.')
                return 1

            return menuOptions[1]() 

        elif main_command == 'read':
            # read      or      read -n

            if len(params) == 1: # only the read command
                menuOptions[2]()
            elif len(params) > 2: # the name and 2 or more params
                print('Error: too mach argument.')
                return 2
            # we have a param. check if it's the -n
            if params[1] != '-n':
                print('Error: invalid option.')
                return 2
            else:
                return menuOptions[3](1)
            
            menuOptions[1](1)
            return 1

        elif main_command == 'send':
            # send -u <user1> <user2> .. <user_n> -o <object>
            if len(params) < 3:
                print('Error: you have to specify user.')
                return 4

            if params[1] != '-t':
                print('Error: invalid option.')
                return 4
            
            usr_list = []
            for i in range(2, len(params)):
                curr = params[i]
                if (curr == '-o'):
                    break
                usr_list.append(curr)

            # checking if cycle ends because of break or just because the
            # params are finished. In this case, the -o option is missing
            if i == len(params):
                print('Error: missing -o option for object.')
                return 4
            
            menuOptions[4](usr_list)
            return 2
        else: 
            print('Error: command not found.')


    return 


def showHelp():
    #TODO
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
    print('\tSigning in to the system (note that password will be asked \
interactively):')
    print('\t\t>> reg -u <username_with_wich_signin_in>')
    print('\tLogging in to the system (note that password will be asked \
interactively):')
    print('\t\t>> log -u <username_with_wich_signin_in>\n')

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
    print('\t\t>> send -t <dest1> <dest2> ... <dest_n> -o <object> ')
    return 






if __name__ == '__main__':
    application_name = sys.argv[0]

    graph.HomeApp().run()
    if len(sys.argv) == 2: # there are params
        if (sys.argv[1] == '-g'):
            graphicClient()  
        if (sys.argv[1] == '-h'):
            showHelp()
        else: 
            print('Invalid params.')
            showHelp()
        
    else:
        commandLineClient()





    


        
