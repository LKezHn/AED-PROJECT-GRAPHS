import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

form_class = uic.loadUiType("InstructionsWindow.ui")[0]

class Instructions(QtWidgets.QMainWindow, form_class):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)
        #Importando el archivo .css
        with open("MainWindow.css") as f:
            self.setStyleSheet(f.read())
        self.setupUi(self)
        self.setWindowTitle("Instrucciones")
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.ok.clicked.connect(lambda:self.close())
        self.center()

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(screen.width(), (screen.height() - size.height())/2)
