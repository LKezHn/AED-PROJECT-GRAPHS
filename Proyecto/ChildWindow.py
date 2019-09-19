import sys
import os
import networkx as nx 
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPlainTextEdit
from PyQt5.QtGui import QIcon, QPixmap
from Graph import *



class ChildWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ChildWindow.ui",self)
        self.parent = parent
        self.setWindowTitle("Mapa")
        self.setFocus()
        self.createGraph()
        
    def createGraph(self):
        G = Graph()#Creo una instancia de grafo para poder enviar la informacion del qplaintext e ingresarla
        graph = G.convert(self.parent.array)
        self.printGraph(graph)#Llamo a la funcion que crea la imagen del grafo

    def printGraph(self,graph):
        D = nx.DiGraph()
        for vertex, edges in graph.items():
            D.add_node("%s"%vertex)
            for edge in edges:
                D.add_node("%s"%"".join(edge))
                D.add_edge("%s" %vertex,"%s"%"".join(edge),weight=15)
                #print("'%s' se conecta con '%s'"%(vertex,edge))
        nx.draw(D, with_labels=True, node_size = 4000, node_color = "darkgray", edge_weigth = "bold", font_size = 20, font_weight = "bold")#Dibuja el grafo
        plt.savefig("image.png", dpi = 55)#Guarda el dibujo del grafo
        plt.clf()#Para que al agregar nueva info se borre el grafo anterior y no aparezca repetido en la ventana
        self.showGraph()
        os.remove("image.png")#Para que no se cree el archivo en la carpeta del proyecto

    def showGraph(self): #Funcion para que aparezca la imagen en la ventana
        label = QLabel(self)
        pixmap = QPixmap('image.png')
        label.resize(pixmap.width(),pixmap.height())       
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        