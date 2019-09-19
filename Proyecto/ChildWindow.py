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
        
        
        #print(char)
        
        #os.remove("image.png")#Elimina la imagen al cerrar la ventana
        
    def createGraph(self):
        G = Graph()#Creo una instancia de grafo para poder enviar la informacion del qplaintext e ingresarla
        #G.graph.clear()
        graph = G.convert(self.parent.array)
        self.printGraph(graph)#Llamo a la funcion que crea la imagen del grafo

    def printGraph(self,grafo):
        D = nx.DiGraph()
        for vertex, edges in grafo.items():
            D.add_node("%s"%vertex)
            for edge in edges:
                D.add_node("%s"%edge)
                D.add_edge("%s" %vertex,"%s"%edge,weight=15)
                #print("'%s' se conecta con '%s'"%(vertex,edge))
        nx.draw(D, with_labels=True, node_size = 4000, node_color = "darkgray", edge_size = 300, font_size = 20, font_weight = "bold")
        plt.savefig("image.png", dpi = 55)
        plt.clf()#Para que al agregar nueva info se borre el grafo anterior
        self.showGraph()
        os.remove("image.png")
        #D.remove_nodes_from(grafo)

    def showGraph(self): #Funcion para que aparezca la imagen en la ventana
        label = QLabel(self)
        pixmap = QPixmap('image.png')#.scaled(390,320)
        label.resize(pixmap.width(),pixmap.height())       
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        