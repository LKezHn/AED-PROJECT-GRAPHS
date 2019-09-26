# -*- coding: utf-8 -*-

import sys
from ChildWindow import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from TableWindow import *
from Instructions import *
form_class = uic.loadUiType("MainWindow.ui")[0]

class MainWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        #Importando el archivo .css
        instructions = Instructions()
        with open("MainWindow.css") as f:
            self.setStyleSheet(f.read())
        self.setupUi(self)
        self.setWindowIcon(QIcon("logo.png"))
        self.instructions = QLabelClickable("Instrucciones...")
        self.instructions.clicked.connect(lambda:instructions.show())
        self.layout.addWidget(self.instructions)
        #Lo que va a aparecer en cada QPlainText cuando esté vacío
        self.array = ""
        self.roads = ""
        self.edge_labels = {}
        self.characters.setTabStopWidth(self.characters.fontMetrics().width(" ")*10)
        self.characters.setPlaceholderText("Ingrese vértices, aristas y caracteristicas.")
        self.root_node.setPlaceholderText("Nodo Origen")
        self.last_node.setPlaceholderText("Nodo Destino")
        self.load_file.clicked.connect(self.loadFile)
        self.create_map.clicked.connect(self.passToOpen)
        self.create_table.clicked.connect(self.openTable)
        self.setFocus()
    

    def passToOpen(self):#Funcion para pasar el texto ingresado a openChild
        if(self.printPlainText() == "" or self.root_node.toPlainText() == "" or self.last_node.toPlainText() == ""):
            warning = Warning(1,parent = self).exec_()#print("hello")
        else:    
            self.openChild(self.printPlainText())
   
    def openChild(self,text):#Funcion que abre la childwindow y envia el texto ingresado
        self.array = text
        self.child = ChildWindow(parent = self)#Instancia de la ChildWindow pasando el self de la MainWindow como parametro
        self.child.show()
        self.roads = self.child.createGraph()
        

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

    def openTable(self):
        if(self.printPlainText() == "" or self.root_node.toPlainText() == "" or self.last_node.toPlainText() == ""):
            warning = Warning(1,parent = self).exec_()
        elif(self.roads == ""):
            warning = Warning(2,parent = self).exec_()
        else:
            self.table = TableWindow(parent = self)#Instancia de la TableWindow pasando el self de la MainWindow como parametro
            self.table.show()
        self.roads = ""

class Warning(QDialog):
    def __init__(self,key,parent):
        super(Warning, self).__init__()
        self.setWindowTitle("Advertencia")
        with open("MainWindow.css") as f:
            self.setStyleSheet(f.read())
        layout = QVBoxLayout()#Creo un layout
        label = QLabel() #Creo el label
        self.setFixedSize(440, 70)
        label.setText("Debe rellenar todos los espacios con la informacion necesaria")#TExto del label
        label.setAlignment(Qt.AlignAbsolute)
        layout.addWidget(label)#Agrego el label al layout
        self.setLayout(layout)#Para que se muestre en pantalla
        button = QPushButton("Aceptar",self)
        button.clicked.connect(self.ok)
        button.move(172,33)
        if(key == 2):#Si la key es igual a 2 modifico la ventana y el mensaje que aparece
            self.setFixedSize(237, 70)
            label.setText("Debe generar el mapa primero")
            button.move(67,33)

    def ok(self):
        self.close()

class QLabelClickable(QLabel):
    clicked = pyqtSignal()

    def __init__(self,*args):
        QLabel.__init__(self,*args)

    def mouseReleaseEvent(self, ev):
        self.clicked.emit()


aplicacion = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
    
sys.exit(aplicacion.exec_())         