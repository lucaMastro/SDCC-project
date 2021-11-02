from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
import sys
from PyQt5.QtCore import pyqtSignal, QObject

import functionalities.getUsrList as usr 
import functionalities.readMessages as read 
import functionalities.registrationLogin as regLog 
import functionalities.sendMessage as send 
import functionalities.Message as mess

from gui_support.WidgetStack import WidgetStack 
from gui_support.Home import Home
from gui_support.LoggedUserHome import LoggedUserHome 
from gui_support.LogIn import LogIn
from gui_support.ReadMessages import ReadMessages 
from gui_support.ReadNewMessages import ReadNewMessages 
from gui_support.SendMessage import SendMessage 
from gui_support.SignUp import SignUp

def main():

    app = QtWidgets.QApplication(sys.argv)
    widgetStack = WidgetStack()

    # class instances:
    home_ui = Home(widgetStack)
    login_ui = LogIn(widgetStack)
    signup_ui = SignUp(widgetStack)
    loggedHome_ui = LoggedUserHome(widgetStack)
    sendMessage_ui = SendMessage(widgetStack)
    readMessages_ui = ReadMessages(widgetStack)
    readNewMessages_ui = ReadNewMessages(widgetStack)

    home = QtWidgets.QDialog()
    home_ui.setupUi(home)
    widgetStack.addWidget(home)
    
    signup = QtWidgets.QDialog()
    signup_ui.setupUi(signup)
    widgetStack.addWidget(signup)

    login = QtWidgets.QDialog()
    login_ui.setupUi(login, readMessages_ui, 
            readNewMessages_ui, sendMessage_ui)
    widgetStack.addWidget(login)

    loggedHome = QtWidgets.QDialog()
    loggedHome_ui.setupUi(loggedHome, readMessages_ui, readNewMessages_ui)
    widgetStack.addWidget(loggedHome)

    sendMessage = QtWidgets.QDialog()
    sendMessage_ui.setupUi(sendMessage)
    widgetStack.addWidget(sendMessage)
    
    readMessages = QtWidgets.QDialog()
    readMessages_ui.setupUi(readMessages, sendMessage_ui)
    widgetStack.addWidget(readMessages)
    
    readNewMessages = QtWidgets.QDialog()
    readNewMessages_ui.setupUi(readNewMessages, sendMessage_ui)
    widgetStack.addWidget(readNewMessages)

    widgetStack.setFixedHeight(480)
    widgetStack.setFixedWidth(720)
    widgetStack.setWindowTitle('Graphic client')
    widgetStack.show()

    #global username
    #username = 'a'
    #widgetStack.setCurrentIndex(widgetStack.sceneDict['readMessages'])

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
