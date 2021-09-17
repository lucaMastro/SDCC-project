#............................................................
# Imports
import sys
import boto3

#............................................................
# Global variables

username = ''

#............................................................


def exitSelected():
    return 0

def signInSelected():
    #@TODO
    input('signin done, press a key to continue')
    return 1

def loginSelected():
    #@TODO
    global username
    username = 'Luca'

    input('Login has been done successfully. Press a key to continue')
    return 2


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
        return mainMenuOptions[operation]()
    except:
        print("Il valore inserito non è accettabile. Riprova")
        return -1



def logOut():
    #@TODO
    input('log out done, press a key to continue')
    return 0

def getUsersList():
    #@TODO
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
    try:
        return menuOptions[operation]()
    except:
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





    


        
