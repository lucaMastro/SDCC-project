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


readPayload = None

class Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(720, 480)
        Home.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Home.setStyleSheet("QDialog{\n"
"  background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #ffffff;\n"
"}")
        self.login_button = QtWidgets.QPushButton(Home)
        self.login_button.setGeometry(QtCore.QRect(210, 250, 300, 30))

        self.login_button.setStyleSheet("QPushButton\n"
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

        self.login_button.setObjectName("login_button")
        self.signin_button = QtWidgets.QPushButton(Home)
        self.signin_button.setEnabled(True)
        self.signin_button.setGeometry(QtCore.QRect(210, 320, 300, 30))
        self.signin_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.signin_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.signin_button.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #b3b1b1;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #bababa;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"}")
        self.signin_button.setIconSize(QtCore.QSize(20, 20))
        self.signin_button.setObjectName("signin_button")
        self.label = QtWidgets.QLabel(Home)
        self.label.setGeometry(QtCore.QRect(10, 40, 699, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Home)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 699, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.close_button = QtWidgets.QPushButton(Home)
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

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

        # connecting button to their handler:
        self.login_button.clicked.connect(self.loginClicked)
        self.signin_button.clicked.connect(self.signinClicked)
        self.close_button.clicked.connect(self.closeClicked)

    def loginClicked(self):
        widgetStack.setCurrentIndex(sceneDict['login'])

    def signinClicked(self):
        widgetStack.setCurrentIndex(sceneDict['signin'])

    def closeClicked(self):
       sys.exit()

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home page"))
        self.login_button.setText(_translate("Home", "Log in"))
        self.signin_button.setText(_translate("Home", "Sign in"))
        self.label.setText(_translate("Home", "Welcome to Graphic support for Client. "))
        self.label_2.setText(_translate("Home", "Please select an operation:"))
        self.close_button.setText(_translate("Home", "Close"))


#----------------------------------------------------------------------------------------------


class LoggedUserHome(QObject):

    readSignal = pyqtSignal(int)
    readNewSignal = pyqtSignal(int)

    def setupUi(self, LoggedUserHome, readMessagesObject=None,
            readNewMessagesObject=None):

        global username

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

        # changing title with username name:
        #self.welcomeLabel.setText(self.welcomeLabel.text()+ ' ' + username)
        self.sendMessageButton.clicked.connect(self.sendButtonClicked)
        self.readMessagesButton.clicked.connect(self.readButtonClicked)
        self.readNewMessagesButton.clicked.connect(self.readNewButtonClicked)
        self.userListButton.clicked.connect(self.usrListButtonClicked)
        self.close_button.clicked.connect(self.closeButtonClicked)

        # connecting signal
        self.readSignal.connect(readMessagesObject.startUseCase)
        self.readNewSignal.connect(readNewMessagesObject.startUseCase)


    def sendButtonClicked(self):
        widgetStack.setCurrentIndex(sceneDict['sendMessage'])

    def readButtonClicked(self):
        self.readSignal.emit(0)
        # preparing first message view:
        widgetStack.setCurrentIndex(sceneDict['readMessages'])

    def readNewButtonClicked(self):
        self.readNewSignal.emit(0)
        widgetStack.setCurrentIndex(sceneDict['readNewMessages'])

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


class LogIn(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setEnabled(True)
        Login.resize(720, 480)
        Login.setStyleSheet("QDialog{\n"
"  background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #ffffff;\n"
"}")
        self.loginButton = QtWidgets.QPushButton(Login)
        self.loginButton.setGeometry(QtCore.QRect(564, 390, 106, 30))
        self.loginButton.setStyleSheet("QPushButton\n"
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
        self.loginButton.setObjectName("loginButton")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 699, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.backButton = QtWidgets.QPushButton(Login)
        self.backButton.setGeometry(QtCore.QRect(50, 390, 106, 30))
        self.backButton.setStyleSheet("QPushButton\n"
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
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("functionalities/images/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(50, 50))
        self.backButton.setObjectName("backButton")
        self.formLayoutWidget = QtWidgets.QWidget(Login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 160, 611, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(50)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.userField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.userField.setObjectName("userField")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userField)
        self.passwordField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setObjectName("passwordField")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordField)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        
        self.loginButton.clicked.connect(self.loginClicked)
        self.backButton.clicked.connect(self.backClicked)


    def loginClicked(self):
        global username
        global backScene

        usr = self.userField.text()
        pw = self.passwordField.text()

        # removing eventual initial space from usr 
        startIndex = 0
        for i in range(len(usr)):
            if usr[i] == ' ':
                startIndex += 1
        usr = usr[startIndex:]

        # call login func and if else for checking login resul

        response_list = regLog.registrationLogin(2, usr, pw)
        lambda_response = response_list[0]
        username = response_list[1]

        if lambda_response == 'true': 
            backScene = 'loggedHome'
            username = usr
            w = widgetStack.widget(sceneDict['loggedHome'])
            welcome_label = w.findChild(QLabel, 'welcomeLabel')
            welcome_label.setText('Welcome {}'.format(username))

            widgetStack.setCurrentIndex(sceneDict['loggedHome'])
        else:
            showPopup(('Error!', 'Something went wrong:', 'Wrong username or \
                password', -1))

    def backClicked(self):
        widgetStack.setCurrentIndex(sceneDict[backScene])



    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login page"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.label_3.setText(_translate("Login", "Login form"))
        self.label_2.setText(_translate("Login", "Username:"))
        self.label_4.setText(_translate("Login", "Password:"))

#----------------------------------------------------------------------------------------------

class ReadMessages(object):
    messageObjectList = []
    def setupUi(self, ReadMessages):
        ReadMessages.setObjectName("ReadMessages")
        ReadMessages.setEnabled(True)
        ReadMessages.resize(720, 480)
        ReadMessages.setStyleSheet("QDialog{\n"
"  background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #ffffff;\n"
"}")
        self.nextButton = QtWidgets.QPushButton(ReadMessages)
        self.nextButton.setGeometry(QtCore.QRect(564, 390, 106, 30))
        self.nextButton.setStyleSheet("QPushButton\n"
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
        self.nextButton.setObjectName("nextButton")
        self.label_3 = QtWidgets.QLabel(ReadMessages)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 699, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.backButton = QtWidgets.QPushButton(ReadMessages)
        self.backButton.setGeometry(QtCore.QRect(50, 390, 106, 30))
        self.backButton.setStyleSheet("QPushButton\n"
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
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("functionalities/images/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(50, 50))
        self.backButton.setObjectName("backButton")
        self.formLayoutWidget = QtWidgets.QWidget(ReadMessages)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 104, 671, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.fromField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fromField.setWhatsThis("")
        self.fromField.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.fromField.setReadOnly(True)
        self.fromField.setPlaceholderText("")
        self.fromField.setObjectName("fromField")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fromField)
        self.objectField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.objectField.setReadOnly(True)
        self.objectField.setObjectName("objectField")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.objectField)
        self.bodyField = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.bodyField.setReadOnly(True)
        self.bodyField.setObjectName("bodyField")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bodyField)
        self.spinBox = QtWidgets.QSpinBox(ReadMessages)
        self.spinBox.setGeometry(QtCore.QRect(250, 390, 52, 30))
        self.spinBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.spinBox.setObjectName("spinBox")



        self.deleteButton = QtWidgets.QPushButton(ReadMessages)
        self.deleteButton.setGeometry(QtCore.QRect(430, 390, 50, 30))
        #self.deleteButton.setToolTip("Delete this message")
        #self.deleteButton.setToolTipDuration(-1)
        self.deleteButton.setStyleSheet("QPushButton\n"
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
        self.deleteButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("functionalities/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QtCore.QSize(20, 20))
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(ReadMessages)
        QtCore.QMetaObject.connectSlotsByName(ReadMessages)

        #missing spin box change and next button clicked
        self.backButton.clicked.connect(self.backClicked)
        self.nextButton.clicked.connect(self.nextClicked)
        self.deleteButton.clicked.connect(self.deleteClicked)
 
        
    def startUseCase(self):
        # setting empty labels:
        self.fromField.setText('')
        self.objectField.setText('')
        self.bodyField.setPlainText('')
        global username
        read.getMessages(username,graphic=True)
        # creating a list of Message objects, based on the read.messagesList
        self.messageObjectList = []
        for msgString in read.messagesList:
            self.messageObjectList.append(mess.Message(msgString))
        if len(self.messageObjectList) == 0:
            showPopup(('No message found', "You don't have any new message",\
                    None, 0))
            return
        
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(len(self.messageObjectList))
        # init to -1 to use nextClicked function to initialize first view
        self.toDisplayIndex = -1
        self.nextClicked()


    def nextClicked(self):
        self.toDisplayIndex += 1
        if len(self.messageObjectList) != 0:
            self.toDisplayIndex %= len(self.messageObjectList)

        toDisplayMessage = self.messageObjectList[self.toDisplayIndex]
        self.fromField.setText(toDisplayMessage.from_)
        self.objectField.setText(toDisplayMessage.object_)
        self.bodyField.setPlainText(toDisplayMessage.text)

        # updating spinBox number:
        self.spinBox.setValue(self.toDisplayIndex + 1)

        # updating read.readMessages
        if self.toDisplayIndex not in read.readMessages:
            read.readMessages.append(self.toDisplayIndex)

    def deleteClicked(self):
        # updating read.toDeleteMessages
        read.toDeleteMessages.append(self.toDisplayIndex)
        # showing the enxt one
        self.nextClicked()
        return

    def backClicked(self):
        self.deleteAndMark()
        widgetStack.setCurrentIndex(sceneDict[backScene])

    def deleteAndMark(self):
        read.prepareAndInvokeDelete()

    def retranslateUi(self, ReadMessages):
        _translate = QtCore.QCoreApplication.translate
        ReadMessages.setWindowTitle(_translate("ReadMessages", "Read messages page"))
        self.nextButton.setText(_translate("ReadMessages", "Next"))
        self.label_3.setText(_translate("ReadMessages", "Read messages"))
        self.label_7.setText(_translate("ReadMessages", "Message body:"))
        self.label_2.setText(_translate("ReadMessages", "From:"))
        self.label_4.setText(_translate("ReadMessages", "Object:"))

#----------------------------------------------------------------------------------------------


class ReadNewMessages(object):
    messageObjectList = []

    def setupUi(self, ReadNewMessages):
        ReadNewMessages.setObjectName("ReadNewMessages")
        ReadNewMessages.setEnabled(True)
        ReadNewMessages.resize(720, 480)
        ReadNewMessages.setStyleSheet("QDialog{\n"
"  background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #ffffff;\n"
"}")
        self.nextButton = QtWidgets.QPushButton(ReadNewMessages)
        self.nextButton.setGeometry(QtCore.QRect(564, 390, 106, 30))
        self.nextButton.setStyleSheet("QPushButton\n"
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
        self.nextButton.setObjectName("nextButton")
        self.label_3 = QtWidgets.QLabel(ReadNewMessages)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 699, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.backButton = QtWidgets.QPushButton(ReadNewMessages)
        self.backButton.setGeometry(QtCore.QRect(50, 390, 106, 30))
        self.backButton.setStyleSheet("QPushButton\n"
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
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("functionalities/images/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(50, 50))
        self.backButton.setObjectName("backButton")
        self.formLayoutWidget = QtWidgets.QWidget(ReadNewMessages)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 104, 671, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.fromField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fromField.setWhatsThis("")
        self.fromField.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.fromField.setReadOnly(True)
        self.fromField.setPlaceholderText("")
        self.fromField.setObjectName("fromField")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fromField)
        self.objectField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.objectField.setReadOnly(True)
        self.objectField.setObjectName("objectField")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.objectField)
        self.bodyField = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.bodyField.setReadOnly(True)
        self.bodyField.setObjectName("bodyField")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bodyField)
        self.spinBox = QtWidgets.QSpinBox(ReadNewMessages)
        self.spinBox.setGeometry(QtCore.QRect(250, 390, 52, 30))
        self.spinBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.spinBox.setObjectName("spinBox")



        self.deleteButton = QtWidgets.QPushButton(ReadNewMessages)
        self.deleteButton.setGeometry(QtCore.QRect(430, 390, 50, 30))
        #self.deleteButton.setToolTip("Delete this message")
        #self.deleteButton.setToolTipDuration(-1)
        self.deleteButton.setStyleSheet("QPushButton\n"
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
        self.deleteButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("functionalities/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QtCore.QSize(20, 20))
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(ReadNewMessages)
        QtCore.QMetaObject.connectSlotsByName(ReadNewMessages)

        #missing spin box change and next button clicked
        self.backButton.clicked.connect(self.backClicked)
        self.nextButton.clicked.connect(self.nextClicked)
        self.deleteButton.clicked.connect(self.deleteClicked)
 
        
    def startUseCase(self):
        # setting empty labels:
        self.fromField.setText('')
        self.objectField.setText('')
        self.bodyField.setPlainText('')
        
        global username
        read.getMessages(username,all_=False,graphic=True)
        # creating a list of Message objects, based on the read.messagesList
        self.messageObjectList = []
        for msgString in read.messagesList:
            self.messageObjectList.append(mess.Message(msgString))
        
        if len(self.messageObjectList) == 0:
            showPopup(('No message found', "You don't have any new message",\
                    None, 0))
            return
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(len(self.messageObjectList))
        # init to -1 to use nextClicked function to initialize first view
        self.toDisplayIndex = -1
        self.nextClicked()


    def nextClicked(self):
        self.toDisplayIndex += 1
        if len(self.messageObjectList) != 0:
            self.toDisplayIndex %= len(self.messageObjectList)

        toDisplayMessage = self.messageObjectList[self.toDisplayIndex]
        self.fromField.setText(toDisplayMessage.from_)
        self.objectField.setText(toDisplayMessage.object_)
        self.bodyField.setPlainText(toDisplayMessage.text)

        # updating spinBox number:
        self.spinBox.setValue(self.toDisplayIndex + 1)

        # updating read.readMessages
        if self.toDisplayIndex not in read.readMessages:
            read.readMessages.append(self.toDisplayIndex)

    def deleteClicked(self):
        # updating read.toDeleteMessages
        read.toDeleteMessages.append(self.toDisplayIndex)
        # showing the enxt one
        self.nextClicked()
        return

    def backClicked(self):
        self.deleteAndMark()
        widgetStack.setCurrentIndex(sceneDict[backScene])

    def deleteAndMark(self):
        read.prepareAndInvokeDelete()



    def retranslateUi(self, ReadNewMessages):
        _translate = QtCore.QCoreApplication.translate
        ReadNewMessages.setWindowTitle(_translate("ReadNewMessages", "Read new messages page"))
        self.nextButton.setText(_translate("ReadNewMessages", "Next"))
        self.label_3.setText(_translate("ReadNewMessages", "Read new messages"))
        self.label_7.setText(_translate("ReadNewMessages", "Message body:"))
        self.label_2.setText(_translate("ReadNewMessages", "From:"))
        self.label_4.setText(_translate("ReadNewMessages", "Object:"))


#----------------------------------------------------------------------------------------------
class SendMessage(object):
    def setupUi(self, SendMessage):
        SendMessage.setObjectName("SendMessage")
        SendMessage.setEnabled(True)
        SendMessage.resize(720, 480)
        SendMessage.setStyleSheet("QDialog{\n"
"  background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #ffffff;\n"
"}")
        self.sendButton = QtWidgets.QPushButton(SendMessage)
        self.sendButton.setGeometry(QtCore.QRect(564, 390, 106, 30))
        self.sendButton.setStyleSheet("QPushButton\n"
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
        self.sendButton.setObjectName("sendButton")
        self.label_3 = QtWidgets.QLabel(SendMessage)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 699, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.backButton = QtWidgets.QPushButton(SendMessage)
        self.backButton.setGeometry(QtCore.QRect(50, 390, 106, 30))
        self.backButton.setStyleSheet("QPushButton\n"
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
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("functionalities/images/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(50, 50))
        self.backButton.setObjectName("backButton")
        self.formLayoutWidget = QtWidgets.QWidget(SendMessage)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 104, 691, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.destinationField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.destinationField.setToolTip("You can insert here multiple destiantion: dest1, dest2 ...")
        self.destinationField.setToolTipDuration(-1)
        self.destinationField.setWhatsThis("")
        self.destinationField.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.destinationField.setPlaceholderText("")
        self.destinationField.setObjectName("destinationField")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.destinationField)
        self.objectField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.objectField.setObjectName("objectField")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.objectField)
        self.bodyField = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.bodyField.setObjectName("bodyField")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bodyField)

        self.retranslateUi(SendMessage)
        QtCore.QMetaObject.connectSlotsByName(SendMessage)

        self.backButton.clicked.connect(self.backClicked)
        self.sendButton.clicked.connect(self.sendClicked)

    def sendClicked(self):
        global username

        dest = self.destinationField.text()
        dest_list = dest.split(',')
        # removing eventual initial space:
        # dest = 'a, b, c, d'
        # dest.split(',') produces: ['a', ' b', ' c', ' d']
        for i in range(len(dest_list)):
            if dest_list[i][0] == ' ':
                dest_list[i] = dest_list[i][1:]

        obj = self.objectField.text()
        body = self.bodyField.toPlainText()
        graphicsInput = {}
        graphicsInput['receivers'] = dest_list 
        graphicsInput['sender'] =username
        graphicsInput['object'] = obj
        graphicsInput['body'] = body

        send.sendMessage(graphicsInput)

        showPopup(('Success!', 'Message sent successfully', None, None))
        self.objectField.setText('')
        self.bodyField.setPlainText('')
        self.destinationField.setText('')


    def backClicked(self):
        widgetStack.setCurrentIndex(sceneDict[backScene])



    def retranslateUi(self, SendMessage):
        _translate = QtCore.QCoreApplication.translate
        SendMessage.setWindowTitle(_translate("SendMessage", "Send message page"))
        self.sendButton.setText(_translate("SendMessage", "Send"))
        self.label_3.setText(_translate("SendMessage", "Send message"))
        self.label_7.setText(_translate("SendMessage", "Message body:"))
        self.label_2.setText(_translate("SendMessage", "Destinations:"))
        self.label_4.setText(_translate("SendMessage", "Object:"))

#----------------------------------------------------------------------------------------------

sceneDict = {'home' : 0,
        'signin' : 1,
        'login' : 2,
        'loggedHome' : 3,
        'sendMessage' : 4,
        'readMessages' : 5,
        'readNewMessages' : 6
        }


app = None
widgetStack = None
backScene = ''
username = ''

   
#----------------------------------------------------------------------------------------------

class SignIn(object):
    def setupUi(self, Signin):
        Signin.setObjectName("Signin")
        Signin.setEnabled(True)
        Signin.resize(720, 480)
        Signin.setStyleSheet("QDialog{\n"
"  background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #ffffff;\n"
"}")
        self.signinButton = QtWidgets.QPushButton(Signin)
        self.signinButton.setGeometry(QtCore.QRect(564, 390, 106, 30))
        self.signinButton.setStyleSheet("QPushButton\n"
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
        self.signinButton.setObjectName("signinButton")
        self.label_3 = QtWidgets.QLabel(Signin)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 699, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.backButton = QtWidgets.QPushButton(Signin)
        self.backButton.setGeometry(QtCore.QRect(50, 390, 106, 30))
        self.backButton.setStyleSheet("QPushButton\n"
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
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("functionalities/images/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(50, 50))
        self.backButton.setObjectName("backButton")
        self.formLayoutWidget = QtWidgets.QWidget(Signin)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 160, 611, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(50)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.userField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.userField.setObjectName("userField")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userField)
        self.passwordField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setObjectName("passwordField")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordField)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.retranslateUi(Signin)
        QtCore.QMetaObject.connectSlotsByName(Signin)

        
        self.signinButton.clicked.connect(self.signinClicked)
        self.backButton.clicked.connect(self.backClicked)

    def signinClicked(self):
        usr = self.userField.text()
        pw = self.passwordField.text()
        # removing eventual initial space from usr 
        startIndex = 0
        for i in range(len(usr)):
            if usr[i] == ' ':
                startIndex += 1
        usr = usr[startIndex:]

        # call login func and if else for checking login resul
        response_list = regLog.registrationLogin(1, usr, pw)
        lambda_response = response_list[0]

        if lambda_response == 'true': 
            showPopup(('Success!', 'Signin done.', None, 0))
        else:
            showPopup(('Error!', 'Something went wrong:', 'Username still \
                present', -1))

    def backClicked(self):
        widgetStack.setCurrentIndex(sceneDict[backScene])

    def retranslateUi(self, Signin):
        _translate = QtCore.QCoreApplication.translate
        Signin.setWindowTitle(_translate("Signin", "Signin page"))
        self.signinButton.setText(_translate("Signin", "Signin"))
        self.label_3.setText(_translate("Signin", "Signin form"))
        self.label_2.setText(_translate("Signin", "Username:"))
        self.label_4.setText(_translate("Signin", "Password:"))


#----------------------------------------------------------------------------------------------
class UserList(QWidget):

    def __init__(self, usersList):
        super().__init__()
        self.title = "System users list"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vLayout =QVBoxLayout()
        groupBox = QGroupBox("User's List:")
        labelLis = []

        # sorting in alpha order
        usersList.sort()
        for i in range(len(usersList)):
            labelLis.append(QLabel(usersList[i]))
            vLayout.addWidget(labelLis[i])
        groupBox.setLayout(vLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        self.show()



#----------------------------------------------------------------------------------------------



def main():
    global app
    global widgetStack
    global backScene 

    backScene = 'home'

    app = QtWidgets.QApplication(sys.argv)
    widgetStack = QtWidgets.QStackedWidget()

    # class instances:
    home_ui = Home()
    signin_ui = SignIn()
    login_ui = LogIn()
    loggedHome_ui = LoggedUserHome()
    sendMessage_ui = SendMessage()
    readMessages_ui = ReadMessages()
    readNewMessages_ui = ReadNewMessages()

    home = QtWidgets.QDialog()
    home_ui.setupUi(home)
    widgetStack.addWidget(home)
    
    signin = QtWidgets.QDialog()
    signin_ui.setupUi(signin)
    widgetStack.addWidget(signin)

    login = QtWidgets.QDialog()
    login_ui.setupUi(login)
    widgetStack.addWidget(login)

    loggedHome = QtWidgets.QDialog()
    loggedHome_ui.setupUi(loggedHome, readMessages_ui, readNewMessages_ui)
    widgetStack.addWidget(loggedHome)

    sendMessage = QtWidgets.QDialog()
    sendMessage_ui.setupUi(sendMessage)
    widgetStack.addWidget(sendMessage)
    
    readMessages = QtWidgets.QDialog()
    readMessages_ui.setupUi(readMessages)
    widgetStack.addWidget(readMessages)
    
    readNewMessages = QtWidgets.QDialog()
    readNewMessages_ui.setupUi(readNewMessages)
    widgetStack.addWidget(readNewMessages)

    widgetStack.setFixedHeight(480)
    widgetStack.setFixedWidth(720)
    widgetStack.setWindowTitle('Graphic client')
    widgetStack.show()

    #global username
    #username = 'luca'
    #widgetStack.setCurrentIndex(sceneDict['loggedHome'])

    sys.exit(app.exec_())

def showPopup(params):
    mbox = QMessageBox()
    title = params[0]
    baseMsg = params[1]
    msg = params[2]
    returnCode = params[3]

    if returnCode == -1:
        mbox.setIcon(QMessageBox.Critical)
    else:
        mbox.setIcon(QMessageBox.Information)

    mbox.setWindowTitle(title)
    mbox.setText(baseMsg)
    mbox.setInformativeText(msg)



    qApp.setStyleSheet("QMessageBox QPushButton{\n"
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

    mbox.setStandardButtons(QMessageBox.Ok)
    mbox.exec_()



if __name__ == '__main__':
    main()
