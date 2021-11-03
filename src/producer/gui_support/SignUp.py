from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
import sys
from PyQt5.QtCore import pyqtSignal, QObject

import functionalities.registrationLogin as regLog 
import gui_support.support_functions as supp 

class SignUp(object):
    backScene = 'home'    

    def __init__(self, WidgetStack=None):
        super().__init__()
        self.widgetStack = WidgetStack

    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.setEnabled(True)
        Signup.resize(720, 480)
        Signup.setStyleSheet("QDialog{\n"
"  background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #ffffff;\n"
"}")
        self.signupButton = QtWidgets.QPushButton(Signup)
        self.signupButton.setGeometry(QtCore.QRect(564, 390, 106, 30))
        self.signupButton.setStyleSheet("QPushButton\n"
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
        self.signupButton.setObjectName("signupButton")
        self.label_3 = QtWidgets.QLabel(Signup)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 699, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.backButton = QtWidgets.QPushButton(Signup)
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
        self.formLayoutWidget = QtWidgets.QWidget(Signup)
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

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

        
        self.signupButton.clicked.connect(self.signupClicked)
        self.backButton.clicked.connect(self.backClicked)

    def signupClicked(self):
        usr = self.userField.text()
        pw = self.passwordField.text()
        # removing eventual initial space from usr 
        startIndex = 0
        for i in range(len(usr)):
            if usr[i] == ' ':
                startIndex += 1
        usr = usr[startIndex:]

        # call login func and if else for checking login resul
        lambda_response = regLog.registrationLogin(1, usr, pw)

        if lambda_response == 'true': 
            supp.showPopup(self.widgetStack, 'Success!', 'Signup done.', None,
                    False)
        else:
            supp.showPopup(self.widgetStack, 'Error!', 'Something went wrong:', 
                'Username still present', True)


    def backClicked(self):
        self.userField.setText('')
        self.passwordField.setText('')
        self.widgetStack.setCurrentIndex(
                self.widgetStack.sceneDict[self.backScene])

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Signup page"))
        self.signupButton.setText(_translate("Signup", "Signup"))
        self.label_3.setText(_translate("Signup", "Signup form"))
        self.label_2.setText(_translate("Signup", "Username:"))
        self.label_4.setText(_translate("Signup", "Password:"))


if __name__ == '__main__':
    main()
