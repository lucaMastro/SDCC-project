from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, \
QGroupBox, QLabel, QPushButton, QFormLayout, QMessageBox, qApp
import sys
from PyQt5.QtCore import pyqtSignal, QObject
import functionalities.readMessages as read
import gui_support.support_functions as supp 



#----------------------------------------------------------------------------------------------
# this class is needed to override close event method. I need to have the
# equivalent of ctrl c in gui for read message, to show read messages to aws 
class WidgetStack(QtWidgets.QStackedWidget):

    sceneDict = {'home' : 0,
            'signin' : 1,
            'login' : 2,
            'loggedHome' : 3,
            'sendMessage' : 4,
            'readMessages' : 5,
            'readNewMessages' : 6
        }

    def __init__(self,parent=None):
        super().__init__(parent)

    def closeEvent(self, event):
        if self.currentIndex() == self.sceneDict['readMessages'] or \
                self.currentIndex() == self.sceneDict['readNewMessages']:
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            read.signalHandler(True, None, None)
        event.accept()

if __name__ == '__main__':
    main()