from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
from PyQt5.QtCore import pyqtSignal, QObject

import sys
sys.path.append('..')
import functionalities.readMessages as read 
import functionalities.Message as mess
import gui_support.support_functions as supp 



class ReadNewMessages(object):
    backScene = 'loggedHome'    
    
    def __init__(self, WidgetStack=None):
        super().__init__()
        self.widgetStack = WidgetStack


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

        self.backButton.clicked.connect(self.backClicked)
        self.nextButton.clicked.connect(self.nextClicked)
        self.deleteButton.clicked.connect(self.deleteClicked)
    
        # conencting spinbox on change value:
        self.spinBox.valueChanged.connect(self.jumpMessage)
    

    def startUseCase(self):
        # setting empty labels:
        self.fromField.setText('')
        self.objectField.setText('')
        self.bodyField.setPlainText('')
        read.getMessages(self.username,all_=False,graphic=True)
        # creating a list of Message objects, based on the read.messagesList
        if len(read.messagesList) == 0:
            supp.showPopup(self.widgetStack, 'No message found', 
                "You don't have any new message", None, False)
            return

        # this will show first message
        self.spinBox.setMinimum(1)

    def jumpMessage(self, n):
        if n == 0:
            # updating spin box value to 0 means there was a mess which has
            # been deleted
            return

        self.toDisplayIndex = n - 1
        self.toDisplayIndex %= len(read.messagesList)
        self.spinBox.setMaximum(len(read.messagesList))
        self.showMessage()

    def showMessage(self):
        toDisplayMessage = read.messagesList[self.toDisplayIndex]
        self.fromField.setText(toDisplayMessage.from_)
        self.objectField.setText(toDisplayMessage.object_)
        self.bodyField.setPlainText(toDisplayMessage.text)

        # updating read.readMessages
        read.messagesList[self.toDisplayIndex].read = True


    def nextClicked(self):
        # updating spinbox text, automated invocation of jump n
        self.spinBox.setValue(self.spinBox.value() + 1)

    def deleteClicked(self):
        read.messagesList.delete(self.toDisplayIndex)

        if len(read.messagesList) != 0:
            if self.toDisplayIndex == len(read.messagesList):
                # this means i've just deleted the last element
                # showing the 'new' last element by modifyin the spinbox.max
                self.spinBox.setMaximum(self.toDisplayIndex)
            else:
                # otherwise keep showing n-th
                self.showMessage()
        else:
            self.fromField.setText('')
            self.objectField.setText('')
            self.bodyField.setPlainText('')
            self.spinBox.setMinimum(0)
            self.spinBox.setMaximum(0)
            supp.showPopup(self.widgetStack, 'No other message found',
                    "You don't have messages anymore", None, False)


    def backClicked(self):
        self.deleteAndMark()
        self.widgetStack.setCurrentIndex(
                self.widgetStack.sceneDict[self.backScene])

    def deleteAndMark(self):
        read.prepareAndInvokeDelete()

    # when login done, set the username. It's a signal-slot function
    def updateUsername(self, usr):
        self.username = usr

    def retranslateUi(self, ReadNewMessages):
        _translate = QtCore.QCoreApplication.translate
        ReadNewMessages.setWindowTitle(_translate("ReadNewMessages", "Read new messages page"))
        self.nextButton.setText(_translate("ReadNewMessages", "Next"))
        self.label_3.setText(_translate("ReadNewMessages", "Read new messages"))
        self.label_7.setText(_translate("ReadNewMessages", "Message body:"))
        self.label_2.setText(_translate("ReadNewMessages", "From:"))
        self.label_4.setText(_translate("ReadNewMessages", "Object:"))


if __name__ == '__main__':
    main()
