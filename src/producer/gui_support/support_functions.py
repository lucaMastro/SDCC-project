from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp, QDialog
#---------------------------------------------
import sys
#---------------------------------------------

def showPopup(parent, title, baseMsg, msg, critical, blocking=True):
    # this function just create a popup to be shown
    mbox = QMessageBox(parent)

    if critical:
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
    if not blocking:
        mbox.setWindowModality(QtCore.Qt.NonModal)
    mbox.show()
