from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
#---------------------------------------------
import functionalities.sendMessage as send 
import gui_support.support_functions as supp 
#---------------------------------------------

class SendMessage(object):
    
    backScene = 'loggedHome'    

    def __init__(self, WidgetStack=None):
        super().__init__()
        self.widgetStack = WidgetStack

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
        icon.addPixmap(QtGui.QPixmap("gui_support/images/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.label_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_1.setObjectName("label_1")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_1)
        
        self.destinationField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.destinationField.setToolTip("You can insert here multiple destinations: dest1, dest2 ...")
        self.destinationField.setToolTipDuration(-1)
        self.destinationField.setWhatsThis("")
        self.destinationField.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.destinationField.setPlaceholderText("")
        self.destinationField.setObjectName("destinationField")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.destinationField)
        self.objectField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.objectField.setObjectName("objectField")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.objectField)
        self.bodyField = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.bodyField.setObjectName("bodyField")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.bodyField)

        self.fromField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fromField.setObjectName("fromField")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fromField)
        self.fromField.setReadOnly(True)

        self.retranslateUi(SendMessage)
        QtCore.QMetaObject.connectSlotsByName(SendMessage)

        # connecting button
        self.backButton.clicked.connect(self.backClicked)
        self.sendButton.clicked.connect(self.sendClicked)
        
        # initialize this boolean to False: generally it's not a reply. When
        # a reply is clicked, this value will be switched into True
        self.reply = False

    def retranslateUi(self, SendMessage):
        _translate = QtCore.QCoreApplication.translate
        SendMessage.setWindowTitle(_translate("SendMessage", "Send message page"))
        self.sendButton.setText(_translate("SendMessage", "Send"))
        self.label_3.setText(_translate("SendMessage", "Send message"))
        self.label_7.setText(_translate("SendMessage", "Message body:"))
        self.label_2.setText(_translate("SendMessage", "To:"))
        self.label_4.setText(_translate("SendMessage", "Object:"))
        self.label_1.setText(_translate("SendMessage", "From:"))
#---------------------------------------------

    def sendClicked(self):
        # getting destination field text. it can be a list
        dest = self.destinationField.text()
        # separe users, splitting on ',' and on ' '
        tmp_dest = dest.split(' ')
        dest_list = []
        for i in tmp_dest:
            dest_list += i.split(',')
        while '' in dest_list:
            dest_list.remove('')

        obj = self.objectField.text()
        body = self.bodyField.toPlainText()

        # make dict param
        graphicsInput = dict()
        graphicsInput['receivers'] = dest_list 
        graphicsInput['sender'] =self.username
        graphicsInput['object'] = obj
        graphicsInput['body'] = body
        graphicsInput['reply'] = self.reply 
        graphicsInput['graphic'] = True 

        # send
        send.sendMessage(graphicsInput)

        supp.showPopup(self.widgetStack, 'Success!', 
            'Message sent successfully', None, False)

        # re-initializing the labels
        self.objectField.setText('')
        self.bodyField.setPlainText('')
        self.destinationField.setText('')

        # re-initializing the reply attribute
        self.reply = False

    def backClicked(self):
        # not saving draft
        self.destinationField.setText('')
        self.objectField.setText('')
        self.bodyField.setPlainText('')

        self.widgetStack.setCurrentIndex(
                self.widgetStack.sceneDict[self.backScene])


    # when login done, set the username. It's a signal-slot function
    def updateUsername(self, usr):
        self.username = usr
        self.fromField.setText(usr)

    # when reply is clicked, the labels of To field and object field shoul be
    # set. it's a signal slot function
    def replyHandler(self, dict_param):
        dest_field = makeStringFromList(dict_param['to'])
        self.destinationField.setText(dest_field)
        self.objectField.setText(dict_param['object'])
        self.reply = True

def makeStringFromList(l):
    s = ''
    for i in range(len(l) - 1):
      s += l[i] + ', '
    s += l[len(l) - 1]
    return s
