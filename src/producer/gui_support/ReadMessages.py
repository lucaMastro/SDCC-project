from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
from PyQt5.QtCore import pyqtSignal, QObject
#---------------------------------------------
import sys
sys.path.append('..')
#---------------------------------------------
import functionalities.readMessages as read 
import functionalities.Message as mess
import gui_support.support_functions as supp 
#---------------------------------------------

class ReadMessages(QObject):
    backScene = 'loggedHome'    
    replySignal = pyqtSignal(dict)

    def __init__(self, WidgetStack=None):
        super().__init__()
        self.widgetStack = WidgetStack

    def setupUi(self, ReadMessages, SendMessage):
        ReadMessages.setObjectName("ReadMessages")
        ReadMessages.setEnabled(True)
        ReadMessages.resize(720, 480)
        ReadMessages.setStyleSheet("QDialog{\n"
"  background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #ffffff;\n"
"}")
        self.replyButton = QtWidgets.QPushButton(ReadMessages)
        self.replyButton.setGeometry(QtCore.QRect(564, 430, 106, 30))
        self.replyButton.setStyleSheet("QPushButton\n"
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
        self.replyButton.setObjectName("replyButton")

        self.replyAllButton = QtWidgets.QPushButton(ReadMessages)
        self.replyAllButton.setGeometry(QtCore.QRect(422, 430, 106, 30))
        self.replyAllButton.setStyleSheet("QPushButton\n"
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
        self.replyAllButton.setObjectName("replyAllButton")
        self.label_3 = QtWidgets.QLabel(ReadMessages)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 699, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.backButton = QtWidgets.QPushButton(ReadMessages)
        self.backButton.setGeometry(QtCore.QRect(50, 430, 106, 30))
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
        self.formLayoutWidget = QtWidgets.QWidget(ReadMessages)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 104, 671, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.fromField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fromField.setWhatsThis("")
        self.fromField.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.fromField.setPlaceholderText("")
        self.fromField.setObjectName("fromField")
        self.fromField.setReadOnly(True)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fromField)
        self.objectField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.objectField.setObjectName("objectField")
        self.objectField.setReadOnly(True)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.objectField)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.toField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.toField.setObjectName("toField")
        self.toField.setReadOnly(True)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.toField)
        self.bodyField = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.bodyField.setReadOnly(True)
        self.bodyField.setObjectName("bodyField")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.bodyField)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spinBox = QtWidgets.QSpinBox(ReadMessages)
        self.spinBox.setGeometry(QtCore.QRect(139, 390, 52, 30))
        self.spinBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.spinBox.setObjectName("spinBox")
        self.deleteButton = QtWidgets.QPushButton(ReadMessages)
        self.deleteButton.setGeometry(QtCore.QRect(514, 390, 50, 30))
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
        icon1.addPixmap(QtGui.QPixmap("gui_support/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QtCore.QSize(20, 20))
        self.deleteButton.setObjectName("deleteButton")
        self.newButtonLabel = QtWidgets.QPushButton(ReadMessages)
        self.newButtonLabel.setGeometry(QtCore.QRect(336,390, 60, 30))
        self.newButtonLabel.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #10151f;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"}\n"
"\n"
"")
        self.newButtonLabel.setVisible(False)
        self.newButtonLabel.setObjectName("newButtonLabel")
        self.spinBox.setMinimum(1)

        self.retranslateUi(ReadMessages)
        QtCore.QMetaObject.connectSlotsByName(ReadMessages)

        #missing spin box change and next button clicked
        self.backButton.clicked.connect(self.backClicked)
        self.replyButton.clicked.connect(self.replyClicked)
        self.replyAllButton.clicked.connect(self.replyAllClicked)
        self.deleteButton.clicked.connect(self.deleteClicked)

        # connecting signal
        self.replySignal.connect(SendMessage.replyHandler)
        # conencting spinbox on change value:
        self.spinBox.valueChanged.connect(self.jumpMessage)

    def retranslateUi(self, ReadMessages):
        _translate = QtCore.QCoreApplication.translate
        ReadMessages.setWindowTitle(_translate("ReadMessages", "Read messages page"))
        self.replyButton.setText(_translate("ReadMessages", "Reply"))
        self.replyAllButton.setText(_translate("ReadMessages", "Reply All"))
        self.label_3.setText(_translate("ReadMessages", "Read messages"))
        self.label_7.setText(_translate("ReadMessages", "Message body:"))
        self.label_2.setText(_translate("ReadMessages", "From:"))
        self.label_4.setText(_translate("ReadMessages", "Object:"))
        self.label.setText(_translate("ReadMessages", "To:"))
        self.newButtonLabel.setText(_translate("ReadMessages", "New!"))
#---------------------------------------------
# defining same operation of the CLI read use-case

    def replyClicked(self):
        dict_param = dict()
        dict_param['to'] = [self.fromField.text()]
        dict_param['object'] = 'RE: ' + self.objectField.text()
      
        # updating status. here it's needed because the gui doesnt return on
        # this page, but send page is kept.
        read.prepareAndInvokeDelete()

        # passing params
        self.replySignal.emit(dict_param)
        self.widgetStack.setCurrentIndex(self.widgetStack.sceneDict['sendMessage'])
        return

    def replyAllClicked(self):
        dict_param = dict()
        # getting all original receivers. there is me in this list:
        oldReceivers = self.toField.text()
        # splitting and deleting me:
        new_receivers = oldReceivers.split(', ')
        new_receivers.remove(self.username)
        # adding sender:
        if self.fromField.text() not in new_receivers:
            new_receivers.append(self.fromField.text())

        dict_param['to'] = new_receivers
        dict_param['object'] = 'RE: ' + self.objectField.text()

        # updating status
        read.prepareAndInvokeDelete()

        self.replySignal.emit(dict_param)
        self.widgetStack.setCurrentIndex(self.widgetStack.sceneDict['sendMessage'])
        return
        
    def startUseCase(self):
        # setting empty labels:
        self.fromField.setText('')
        self.objectField.setText('')
        self.bodyField.setPlainText('')
        self.toField.setText('')

        # retrieving messages
        read.getMessages(self.username,graphic=True)

        if len(read.messagesList) == 0:
            supp.showPopup(self.widgetStack, 'No message found', 
                "You don't have any message", None, False)
            return
        
        # this will show first message
        self.toDisplayIndex = 0
        self.showMessage()

        self.spinBox.setMaximum(len(read.messagesList))

    def jumpMessage(self, n):
        if n == 0:
            # updating spin box value to 0 means there was a message which has
            # been deleted
            return
        self.toDisplayIndex = n - 1
        # some message can be delete. Then the max of spin box should be
        # updated
        self.spinBox.setMaximum(len(read.messagesList))
        self.showMessage()

    def showMessage(self):
        # setting up gui labels
        toDisplayMessage = read.messagesList[self.toDisplayIndex]
        self.fromField.setText(toDisplayMessage.from_)
        self.objectField.setText(toDisplayMessage.object_)
        self.bodyField.setPlainText(toDisplayMessage.text)
        self.toField.setText(toDisplayMessage.to)
        self.newButtonLabel.setVisible(toDisplayMessage.isNew)

        # updating read.readMessages
        read.messagesList[self.toDisplayIndex].read = True


    def deleteClicked(self):
        # mark the message as deleted
        read.messagesList.delete(self.toDisplayIndex)

        if len(read.messagesList) != 0:
            if self.toDisplayIndex == len(read.messagesList):
                # this means i've just deleted the last element
                # showing the 'new' last element by modifying the spinbox.max
                self.spinBox.setMaximum(self.toDisplayIndex)
            else:
                # otherwise i've just deleted the n-th message.
                # keep showing the 'new' n-th one
                self.showMessage()
        else:
            # no other message in the list
            self.fromField.setText('')
            self.objectField.setText('')
            self.bodyField.setPlainText('')
            self.toField.setText('')
            self.spinBox.setMinimum(0)
            self.spinBox.setMaximum(0)
            supp.showPopup(self.widgetStack, 'No other message found',
                    "You don't have messages anymore", None, False)

    def backClicked(self):
        # update aws status
        read.prepareAndInvokeDelete()
        # showing logged home page
        self.widgetStack.setCurrentIndex(
                self.widgetStack.sceneDict[self.backScene])

    # when login done, set the username. It's a signal-slot function
    def updateUsername(self, usr):
        self.username = usr
