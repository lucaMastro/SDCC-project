from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp, QSpacerItem
import sys

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
            curr_label = QLabel(usersList[i]) 
            curr_label.setFixedHeight(50)
            labelLis.append(curr_label)
            vLayout.addWidget(labelLis[i])
        
        # this block is meant to show lables properly if they are less than 6
        if len(labelLis) < 6:
            height = len(labelLis) * 50
            verticalSpacer = QSpacerItem(0, 
                    400 - height, 
                    QtWidgets.QSizePolicy.Fixed,
                    QtWidgets.QSizePolicy.Expanding)
            vLayout.addItem(verticalSpacer)
            

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
