#............................................................
# Imports
import sys
import boto3
import functionalities.getUsrList as usr 
import functionalities.Message as mess 
import functionalities.readMessages as read 
import functionalities.registrationLogin as regLog 
import functionalities.sendMessage as send 

#............................................................
# Global variables

username = ''

#............................................................


def exitSelected():
    return 0

def signInSelected(operationCode):
    
    # following function returns the lambda function return value. It's
    # a Boolean value:
    #   True stands for registration done
    #   False stands for registration problem
    response_list = regLog.registrationLogin(operationCode)
    lambda_response = response_list[0]

    if lambda_response == 'true': 
        input('Signin done, press a key to continue')
        return 1
    else:
        input('Username still present retry')
        return None

def loginSelected(operationCode):
    global username
    
    response_list = regLog.registrationLogin(operationCode)
    lambda_response = response_list[0]
    username = response_list[1]

    print('response = .', lambda_response)
    if lambda_response == 'true': 
        input('Login has been done successfully. Press a key to continue')
        return 2
    else:
        input('Wrong username or password')
        return None



def showMainMenu():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
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

def sendMessage():
    #@TODO
    input('send done, press a key to continue')
    return 4

    
def showMenu():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
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




if __name__ == '__main__':

    check = -1
    while check != 2: #2 is the value returned from a valid login

        if check == 0: #user selected exit procedure 
            sys.exit()
             
        check = showMainMenu()

    #restoring default value of check, and start the logged user menu loop
    check = -1
    while check != 0: #user selected exit procedure
        check = showMenu()





    


        
