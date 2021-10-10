from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
import sys
from PyQt5.QtCore import pyqtSignal, QObject

import functionalities.getUsrList as usr 

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



if __name__ == '__main__':
    main()
