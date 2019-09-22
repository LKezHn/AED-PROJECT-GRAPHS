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
        self.G = Graph()
        self.setWindowTitle("Mapa")
        self.setFocus()
        self.createGraph()
        
    def createGraph(self):
        graph = self.G.convert(self.parent.array)
        a = self.parent.root_node.toPlainText()
        b = self.parent.last_node.toPlainText()
        self.printGraph(graph)#Llamo a la funcion que crea la imagen del grafo
        return list(self.dfs_paths(self.G.toRoad,a,b))

    def printGraph(self,graph):
        D = nx.DiGraph()
        for vertex, edges in graph.items():
            D.add_node("%s"%vertex)
            for edge in edges:
                D.add_node("%s"%"".join(edge))
                D.add_edge("%s" %vertex,"%s"%"".join(edge))
                #D.add_edge("%s"%"".join(edge),"%s"%vertex)
                #print("'%s' se conecta con '%s'"%(vertex,edge))
                #print(pos)
        pos = nx.drawing.layout.shell_layout(D)
        nx.draw(D,pos, with_labels=True, node_size = 4000, arrowsize = 20, node_color = "darkgray", width = 3.0 , font_size = 20, font_weight = "bold")#Dibuja el grafo
        nx.draw_networkx_edge_labels(D,pos,edge_labels=self.getFeatures(self.G.graph),font_color='darkblue', font_size = 20)
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

        # Define stack variabledef dfs_paths(graph, start, end):
    def dfs_paths(self, graph, start, end):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == end:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))        
    
    def getFeatures(self,graph):
        for k,v in graph.items():#Ingreso al grafo principal osea el G.graph()
            if(isinstance(v,list)):#Ingreso al value que es una lista
                for i in range(len(v)):
                    if(isinstance(v[i],dict)):#En la lista el primer elemento es un grafo
                        for x,y in v[i].items():#Ingreso a los elementos de ese grafo
                            if(isinstance(y,dict)):#En este punto me encuentro en el grafo donde se encuentran las caracteristicas
                                weigth = self.weightOf(y)
                                #for a,b in y.items():
                                #    print("%s: %s"%(a,b))
                            self.parent.edge_labels[(k,x)] = weigth
        return self.parent.edge_labels
                            
    def weightOf(self, dictionary):
        distance = dictionary.get("distancia")
        bandwidth = dictionary.get("anchoDeBanda")
        connectUsers = dictionary.get("usuariosConectados")
        traffic = dictionary.get("cantidadDeTrafico")
        mediaType = dictionary.get("tipoDeMedio")
        mediaValue = self.findMediaValue(mediaType)
        conf = self.findConfiability(mediaType,distance)
        weight = (int(bandwidth)/int(distance)) * mediaValue
        weightlossForTraffic = int(traffic) * 0.0002 * weight
        weightlossForUsers = int(connectUsers) * 0.0002 * weight
        netWeight = (weight - weightlossForTraffic - weightlossForUsers) * conf
        return round(netWeight,2)
        
    def findMediaValue(self,mediaType):
        mediaValue = 0
        if(mediaType == "CAT5"):
            mediaValue = 1
        elif(mediaType == "CAT6"):
            mediaValue = 8
        elif(mediaType == "Fibra-Óptica" or mediaType == "Fibra-Optica"):
            mediaValue = 10 
        elif(mediaType == "WIFI"):
            mediaValue = 0.5
        elif(mediaType == "Coaxial"):
            mediaValue = 1.5
        elif(mediaType == "Par-Trenzado"):
            mediaValue = 0.9
        return mediaValue

    def findConfiability(self,mediaType,distance):
        confiability = 0
        if(mediaType == "CAT5"):
            confiability = 0.98
            decrease = 0.02
            if(distance >= "50"):
                confiability = confiability - (int(distance) * decrease)
        elif(mediaType == "CAT6"):
            confiability = 0.98
            decrease = 0.01
            if(distance >= "50"):
                confiability = confiability - (int(distance) * decrease)
        elif(mediaType == "Fibra-Óptica" or mediaType == "Fibra-Optica"):
            confiability = 0.90
            decrease = 0.05
            if(distance >= "100"):
                confiability = confiability - (int(distance) * decrease)
        elif(mediaType == "WIFI"):
            confiability = 0.7
            decrease = 0.6
            if(distance >= "6"):
                confiability = confiability - (int(distance) * decrease)
        elif(mediaType == "Coaxial"):
            confiability = 1
            decrease = 0.04
            if(distance >= "100"):
                confiability = confiability - (int(distance) * decrease)
        elif(mediaType == "Par-Trenzado"):
            confiability = 1
            decrease = 0.01
            if(distance >= "100"):
                confiability = confiability - (int(distance) * decrease)
        return confiability

"""    def dfs_paths(self,graph, start, goal):
        # Define stack variable
        stack = [[start]]
        # Do the process while there are paths to follow
        while stack:
            path = stack.pop()
            node = path[-1]
            for next in graph[node] - get(path):
                # If a correct path is founded, then return the path with the generator
                # else write a new path and follow iterating.
                if next == goal:
                    yield path + [next]
                else:
                    stack.append(path + [next])

# Print paths
#print list(dfs_paths(graph, 'A', 'F'))"""