# -*- coding: utf-8 -*-

import sys
from ChildWindow import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
form_class = uic.loadUiType("MainWindow.ui")[0]

class MainWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        #Importando el archivo .css
        with open("MainWindow.css") as f:
            self.setStyleSheet(f.read())
        self.setupUi(self)
        #Lo que va a aparecer en cada QPlainText cuando esté vacío
        self.text = ""
        self.characters.setPlaceholderText("Ingrese vértices, aristas y caracteristicas")
        self.root_node.setPlaceholderText("Nodo Origen")
        self.last_node.setPlaceholderText("Nodo Destino")
        self.load_file.clicked.connect(self.loadFile)
        self.create_map.clicked.connect(self.passToOpen)
        self.setFocus()

    def passToOpen(self):#Funcion para pasar el texto ingresado a openChild
        self.openChild(self.printPlainText())
   
    def openChild(self,text):#Funcion que abre la childwindow y envia el texto ingresado
        self.text = text
        self.child = ChildWindow(parent = self)
        self.child.show()
        

    def loadFile(self):#Funcion para abrir la ventana de busqueda y cargar un archivo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Seleccione un Archivo", "","Todos los Archivos (*);;Archivos de Texto Plano (*.txt)", options=options)
        if fileName:
            f = open(fileName,"r")
            content = f.read()
            self.characters.setPlainText(content)
            self.content = content     

    def printPlainText(self):
        t = self.characters.toPlainText()
        return t
                      

aplicacion = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
    
sys.exit(aplicacion.exec_())        