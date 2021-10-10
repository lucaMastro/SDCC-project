from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
import sys
sys.path.append('..')
from PyQt5.QtCore import pyqtSignal, QObject

import functionalities.getUsrList as usr 
import functionalities.readMessages as read 
import functionalities.sendMessage as send 
import functionalities.Message as mess

from gui_support.UserList import UserList

class LoggedUserHome(QObject):

    readSignal = pyqtSignal(int)
    readNewSignal = pyqtSignal(int)
    
    def __init__(self, WidgetStack=None):
        super().__init__()
        self.widgetStack = WidgetStack


    def setupUi(self, LoggedUserHome, readMessagesObject=None,
            readNewMessagesObject=None):


        LoggedUserHome.setObjectName("LoggedUserHome")
        LoggedUserHome.resize(720, 480)
        LoggedUserHome.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        LoggedUserHome.setStyleSheet("QDialog{\n"
"  background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #ffffff;\n"
"}")
        self.welcomeLabel = QtWidgets.QLabel(LoggedUserHome)
        self.welcomeLabel.setGeometry(QtCore.QRect(10, 40, 699, 50))
        self.welcomeLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.label_2 = QtWidgets.QLabel(LoggedUserHome)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 699, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.close_button = QtWidgets.QPushButton(LoggedUserHome)
        self.close_button.setGeometry(QtCore.QRect(300, 410, 120, 30))
        self.close_button.setStyleSheet("QPushButton{\n"
"    background-color: #b30000;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #cf0202;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"}")
        self.close_button.setObjectName("close_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoggedUserHome)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 190, 491, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(26, -1, 26, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.userListButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.userListButton.setEnabled(True)
        self.userListButton.setMinimumSize(QtCore.QSize(106, 30))
        self.userListButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #10151f;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #242f45;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"}")
        self.userListButton.setObjectName("userListButton")
        self.verticalLayout_2.addWidget(self.userListButton)
        self.sendMessageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sendMessageButton.setMinimumSize(QtCore.QSize(106, 30))
        self.sendMessageButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #10151f;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #242f45;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"}")
        self.sendMessageButton.setObjectName("sendMessageButton")
        self.verticalLayout_2.addWidget(self.sendMessageButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(26, -1, 26, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.readMessagesButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.readMessagesButton.setEnabled(True)
        self.readMessagesButton.setMinimumSize(QtCore.QSize(106, 30))
        self.readMessagesButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #10151f;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #242f45;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"}")
        self.readMessagesButton.setObjectName("readMessagesButton")
        self.verticalLayout.addWidget(self.readMessagesButton)
        self.readNewMessagesButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.readNewMessagesButton.setMinimumSize(QtCore.QSize(106, 30))
        self.readNewMessagesButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #10151f;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #242f45;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"}")
        self.readNewMessagesButton.setObjectName("readNewMessagesButton")
        self.verticalLayout.addWidget(self.readNewMessagesButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(LoggedUserHome)
        QtCore.QMetaObject.connectSlotsByName(LoggedUserHome)

        self.sendMessageButton.clicked.connect(self.sendButtonClicked)
        self.readMessagesButton.clicked.connect(self.readButtonClicked)
        self.readNewMessagesButton.clicked.connect(self.readNewButtonClicked)
        self.userListButton.clicked.connect(self.usrListButtonClicked)
        self.close_button.clicked.connect(self.closeButtonClicked)

        # connecting signal
        self.readSignal.connect(readMessagesObject.startUseCase)
        self.readNewSignal.connect(readNewMessagesObject.startUseCase)


    def sendButtonClicked(self):
        self.widgetStack.setCurrentIndex(self.widgetStack.sceneDict['sendMessage'])

    def readButtonClicked(self):
        self.readSignal.emit(0)
        # preparing first message view:
        self.widgetStack.setCurrentIndex(self.widgetStack.sceneDict['readMessages'])

    def readNewButtonClicked(self):
        self.readNewSignal.emit(0)
        self.widgetStack.setCurrentIndex(self.widgetStack.sceneDict['readNewMessages'])

    def usrListButtonClicked(self):
        # direct invocation of lambda service, then showing result
        l = usr.getUsrList()
        self.dialog = UserList(l)
        

    def closeButtonClicked(self):
        sys.exit()


    def retranslateUi(self, LoggedUserHome):
        _translate = QtCore.QCoreApplication.translate
        LoggedUserHome.setWindowTitle(_translate("LoggedUserHome", "Logged user home"))
        self.welcomeLabel.setText(_translate("LoggedUserHome", "Welcome"))
        self.label_2.setText(_translate("LoggedUserHome", "Please select an operation:"))
        self.close_button.setText(_translate("LoggedUserHome", "Close"))
        self.userListButton.setText(_translate("LoggedUserHome", "Get user list"))
        self.sendMessageButton.setText(_translate("LoggedUserHome", "Send Message"))
        self.readMessagesButton.setText(_translate("LoggedUserHome", "Read messages"))
        self.readNewMessagesButton.setText(_translate("LoggedUserHome", "Read new messages"))


#----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print('ok')
