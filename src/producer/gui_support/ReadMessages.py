from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
from PyQt5.QtCore import pyqtSignal, QObject

import sys
sys.path.append('..')
import functionalities.readMessages as read 
import functionalities.Message as mess
import gui_support.support_functions as supp 

class ReadMessages(object):
    backScene = 'loggedHome'    
    
    def __init__(self, WidgetStack=None):
        super().__init__()
        self.widgetStack = WidgetStack

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

        # conencting spinbox on change value:
        self.spinBox.valueChanged.connect(self.jumpMessage)
 
    def jumpMessage(self, n):
        # n is the new value on spinBox
        #
        # -2 because a +1 occurs in showNext, and the n-th mess
        # is in (n-1)-th position
        self.toDisplayIndex = n - 2
        self.nextClicked()
        
    def startUseCase(self):
        # setting empty labels:
        self.fromField.setText('')
        self.objectField.setText('')
        self.bodyField.setPlainText('')
        read.getMessages(self.username,graphic=True)
        # creating a list of Message objects, based on the read.messagesList
        if len(read.messagesList) == 0:
            supp.showPopup(('No message found', "You don't have any message",\
                    None, 0))
            return
        
        # init to -1 to use nextClicked function to initialize first view
        self.toDisplayIndex = -1
        self.nextClicked()


    def nextClicked(self):
        self.toDisplayIndex += 1
        # this condition may become True after deleting objects
        if len(read.messagesList) != 0:
            self.toDisplayIndex %= len(read.messagesList)
            self.spinBox.setMinimum(1)
            self.spinBox.setMaximum(len(read.messagesList))
        else:
            self.fromField.setText('')
            self.objectField.setText('')
            self.bodyField.setPlainText('')
            self.spinBox.setMinimum(0)
            self.spinBox.setMaximum(0)
            supp.showPopup(('No other message found', "You don't have messages"
            +" anymore", None, 0))
            return


        toDisplayMessage = read.messagesList[self.toDisplayIndex]
        self.fromField.setText(toDisplayMessage.from_)
        self.objectField.setText(toDisplayMessage.object_)
        self.bodyField.setPlainText(toDisplayMessage.text)

        # updating spinBox number:
        self.spinBox.setValue(self.toDisplayIndex + 1)

        # updating read.readMessages
        read.messagesList[self.toDisplayIndex].read = True

    def deleteClicked(self):
        read.messagesList.delete(self.toDisplayIndex)

        # showing the enxt one: i need do show the new self.toDisplayIndex.
        # this value is incremented as first operation in show next, that's why
        # i'm going to decrement by 1 that value here 
        self.toDisplayIndex -= 1
        self.nextClicked()
        return

    def backClicked(self):
        self.deleteAndMark()
        self.widgetStack.setCurrentIndex(
                self.widgetStack.sceneDict[self.backScene])

    def deleteAndMark(self):
        read.prepareAndInvokeDelete()

    # when login done, set the username. It's a signal-slot function
    def updateUsername(self, usr):
        self.username = usr

    def retranslateUi(self, ReadMessages):
        _translate = QtCore.QCoreApplication.translate
        ReadMessages.setWindowTitle(_translate("ReadMessages", "Read messages page"))
        self.nextButton.setText(_translate("ReadMessages", "Next"))
        self.label_3.setText(_translate("ReadMessages", "Read messages"))
        self.label_7.setText(_translate("ReadMessages", "Message body:"))
        self.label_2.setText(_translate("ReadMessages", "From:"))
        self.label_4.setText(_translate("ReadMessages", "Object:"))



if __name__ == '__main__':
    main()
