from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
import sys
from PyQt5.QtCore import pyqtSignal, QObject
#---------------------------------------------

class Home(object):
    
    def __init__(self, WidgetStack=None):
        super().__init__()
        self.widgetStack = WidgetStack

    # gui init
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
        self.signup_button = QtWidgets.QPushButton(Home)
        self.signup_button.setEnabled(True)
        self.signup_button.setGeometry(QtCore.QRect(210, 320, 300, 30))
        self.signup_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.signup_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.signup_button.setStyleSheet("QPushButton\n"
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
        self.signup_button.setIconSize(QtCore.QSize(20, 20))
        self.signup_button.setObjectName("signup_button")
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
        self.signup_button.clicked.connect(self.signupClicked)
        self.close_button.clicked.connect(self.closeClicked)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home page"))
        self.login_button.setText(_translate("Home", "Log in"))
        self.signup_button.setText(_translate("Home", "Sign up"))
        self.label.setText(_translate("Home", "Welcome to Graphic support for Client. "))
        self.label_2.setText(_translate("Home", "Please select an operation:"))
        self.close_button.setText(_translate("Home", "Close"))
#---------------------------------------------
# button handlers

    def loginClicked(self):
        self.widgetStack.setCurrentIndex(self.widgetStack.sceneDict['login'])

    def signupClicked(self):
        self.widgetStack.setCurrentIndex(self.widgetStack.sceneDict['signup'])

    def closeClicked(self):
       sys.exit()

