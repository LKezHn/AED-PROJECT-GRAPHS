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
        QtWidgets.QMainWindow.__init__(self, parent)
        #Importando el archivo .css
        child = ChildWindow(parent = self)
        with open("MainWindow.css") as f:
            self.setStyleSheet(f.read())
        self.setupUi(self)
        self.content = ""
        #Lo que va a aparecer en cada QPlianText cuando esté vacío
        self.characters.setPlaceholderText("Ingrese vértices, aristas y caracteristicas")
        self.root_node.setPlaceholderText("Nodo Origen")
        self.last_node.setPlaceholderText("Nodo Destino")
        self.load_file.clicked.connect(self.loadFile)
        self.create_map.clicked.connect(lambda:child.show())
        self.create_table.clicked.connect(lambda: self.printPlainText)
        self.setFocus()

   

        

    def loadFile(self):#Funcion para abrir la ventana de busqueda y cargar un archivo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Seleccione un Archivo", "","Todos los Archivos (*);;Archivos de Texto Plano (*.txt)", options=options)
        if fileName:
            f = open(fileName,"r")
            content = f.read()
            self.characters.setPlainText(content)
            self.content = content
            #print(self.content)
            #print("-"*40)     

    def printPlainText(self):
        t = self.characters.toPlainText()
        print(t)
                      

aplicacion = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
    
sys.exit(aplicacion.exec_())        