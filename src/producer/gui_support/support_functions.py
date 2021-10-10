from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
from PyQt5.QtCore import pyqtSignal, QObject
import sys

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
    app = QtWidgets.QApplication(sys.argv)
    showPopup(('title', 'base', 'msg', 0))
    sys.exit(app.exec_())
