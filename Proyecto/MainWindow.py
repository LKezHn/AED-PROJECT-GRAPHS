# -*- coding: utf-8 -*-

import sys
from ChildWindow import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from TableWindow import *
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
        self.array = ""
        self.characters.setPlaceholderText("Ingrese vértices, aristas y caracteristicas")
        self.root_node.setPlaceholderText("Nodo Origen")
        self.last_node.setPlaceholderText("Nodo Destino")
        self.load_file.clicked.connect(self.loadFile)
        self.create_map.clicked.connect(self.passToOpen)
        self.create_table.clicked.connect(self.tableWindow)
        #self.converter()
        self.setFocus()

    def passToOpen(self):#Funcion para pasar el texto ingresado a openChild
        self.openChild(self.printPlainText())
   
    def openChild(self,text):#Funcion que abre la childwindow y envia el texto ingresado
        self.array = text
        self.child = ChildWindow(parent = self)#Instancia de la ChildWindow pasando el self de la MainWindow como parametro
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
        t = t.replace("\n"," ")#Quito los saltos de linea
        list_content = t.split(" ")#Quito los espacios y convierto el texto en lista
        return list_content

    def tableWindow(self):
        table = QtWidgets.QPlainTextEdit()
        ui = Ui_Form()
        ui.setupUi(table)
        table.show()
        table.exec_()   

                                             

aplicacion = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
    
sys.exit(aplicacion.exec_())         