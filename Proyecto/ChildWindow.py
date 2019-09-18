import sys
import os
import networkx as nx 
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPlainTextEdit
from PyQt5.QtGui import QIcon, QPixmap
from Graph import *


G = nx.DiGraph()

grafo = {"A":["C","B","D"],
        "B":["C","E","A"]}

for vertex, edges in grafo.items():
    G.add_node("%s"%vertex)
    for edge in edges:
        G.add_node("%s"%edge)
        G.add_edge("%s" %vertex,"%s"%edge,weight=15)
        #print("'%s' se conecta con '%s'"%(vertex,edge))

nx.draw(G, with_labels=True, node_size = 4000, node_color = "darkgray", edge_size = 300, font_size = 20, font_weight = "bold")
plt.savefig("image.png", dpi = 55)

class ChildWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ChildWindow.ui",self)
<<<<<<< HEAD
        self.setWindowTitle("Mapa")
=======
        self.parent = parent
        self.setWindowTitle("Mapa")
        self.printText()
>>>>>>> 83c73689e0a1461c6d325d3a3da0b0c762a20c43
        self.setFocus()
        self.drawGraph()
        self.showGraph()
        os.remove("image.png")#Elimina la imagen al cerrar la ventana
        
<<<<<<< HEAD
=======
        #print(char)
        
        os.remove("image.png")#Elimina la imagen al cerrar la ventana
        
    def printText(self):#Probando si se envia el contenido del QPlainText
        c = self.parent.text
        print(c)

    def drawGraph(self):
        pass#print(content)    

>>>>>>> 83c73689e0a1461c6d325d3a3da0b0c762a20c43
    def showGraph(self): #Funcion para que aparezca la imagen en la ventana
        label = QLabel(self)
        pixmap = QPixmap('image.png')#.scaled(390,320)
        label.resize(pixmap.width(),pixmap.height())       
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        