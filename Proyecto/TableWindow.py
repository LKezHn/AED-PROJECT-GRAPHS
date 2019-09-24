# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *

class TableWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("TableWindow.ui",self)
        self.parent = parent
        self.setWindowTitle("Tabla")
        self.setFocus()
        self.origin = self.parent.root_node.toPlainText()
        self.end = self.parent.last_node.toPlainText()
        self.table.setReadOnly(True)
        self.showTable()

    def showTable(self):
        self.table.setFont(QFont("monospace",8))
        self.table.setPlainText("-"*57)
        self.table.appendPlainText("%sTabla de Rutas de %s a %s"%(" "*17,self.origin,self.end))
        self.table.appendPlainText("-"*57)
        self.table.appendPlainText("\n\n")
        self.table.appendPlainText("-"*57)
        self.table.appendPlainText("|%sRuta%s|%sPeso%s|"%(" "*12," "*12," "*11," "*11))
        self.table.appendPlainText("-"*57)
        self.parent.roads.sort(key = lambda x:len(x),reverse = True)
        for i in range(len(self.parent.roads)):
            self.table.appendPlainText('{3}{0:12s}{1:16s}{3}{0:11s}{2:.1f}{0:11s}{3}'.format(" ",",".join(self.parent.roads[i]),self.totalWeigth(self.parent.roads[i]), '|'))#"%s%s%s|%s%s"%(" "*18,," "*7," "*7,))
            self.table.appendPlainText("-"*57)

    def totalWeigth(self,array):
        current = array[0]
        totalWeight = 0.00
        print(self.parent.edge_labels.get(("A","B")))
        for i in range(1,len(array)):
            key = (current,array[i])
            value = self.parent.edge_labels.get(key)
            print(key)
            totalWeight = totalWeight + value
            current = array[i]
        return round(totalWeight,2)