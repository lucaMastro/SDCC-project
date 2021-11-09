from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
from PyQt5.QtCore import pyqtSignal, QObject
#---------------------------------------------
import sys
sys.path.append('..')
#---------------------------------------------
import functionalities.registrationLogin as regLog 
import gui_support.support_functions as supp 
import ast
#---------------------------------------------

# this class uses pyqtSignal, then must be a subclass of QObject
class LogIn(QObject):
    
    loginDoneSignal = pyqtSignal(str)
    backScene = 'home'

#---------------------------------------------
    def __init__(self, WidgetStack=None):
        super().__init__()
        self.widgetStack = WidgetStack

    def setupUi(self, Login, 
            ReadMessages=None,
            ReadNewMessages=None,
            SendMessage=None):
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
        icon.addPixmap(QtGui.QPixmap("gui_support/images/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

        # connecting buttons:
        self.loginButton.clicked.connect(self.loginClicked)
        self.backButton.clicked.connect(self.backClicked)
        # connecting signal:
        self.loginDoneSignal.connect(ReadMessages.updateUsername)
        self.loginDoneSignal.connect(ReadNewMessages.updateUsername)
        self.loginDoneSignal.connect(SendMessage.updateUsername)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login page"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.label_3.setText(_translate("Login", "Login form"))
        self.label_2.setText(_translate("Login", "Username:"))
        self.label_4.setText(_translate("Login", "Password:"))

#---------------------------------------------


    def loginClicked(self):
        # getting user input
        usr = self.userField.text()
        pw = self.passwordField.text()

        # checking single user inserted:
        if len(usr.split(' ')) > 1 or len(usr.split(',')) > 1:
                supp.showPopup(self.widgetStack, 'Error!', 'Something went wrong:',
                        'Too much users.', True)
                return


        # removing eventual initial space from usr 
        usr = usr.strip()

        # call login lambda
        lambda_response = regLog.registrationLogin(2, usr, pw)

        if lambda_response == 'true': 
            # updating welcome label of loggedHome scene:
            w = self.widgetStack.widget(self.widgetStack.sceneDict['loggedHome'])
            welcome_label = w.findChild(QLabel, 'welcomeLabel')
            welcome_label.setText('Welcome {}'.format(usr))

            # emit the signal of login done: this make the attribute "username"
            # of connected class to change
            self.loginDoneSignal.emit(usr)

            #update the scene
            self.widgetStack.setCurrentIndex(self.widgetStack.sceneDict['loggedHome'])
        else:
            supp.showPopup(self.widgetStack, 'Error!', 'Something went wrong:',
                    lambda_response, True)

    def backClicked(self):
        # re-init fields
        self.userField.setText('')
        self.passwordField.setText('')
        self.widgetStack.setCurrentIndex(
                self.widgetStack.sceneDict[self.backScene])
