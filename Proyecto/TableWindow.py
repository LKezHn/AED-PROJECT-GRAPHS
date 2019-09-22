# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, uic


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
        self.table.setPlainText("-"*84)
        self.table.appendPlainText("%sTabla de Rutas de %s a %s"%(" "*28,self.origin,self.end))
        self.table.appendPlainText("-"*84)
        self.table.appendPlainText("%sRuta%s|%sPeso"%(" "*30," "*15," "*15))
        self.table.appendPlainText("-"*84)
        for i in range(len(self.parent.roads)):
            self.table.appendPlainText("%s%s%s%s"%(" "*31,",".join(self.parent.roads[i])," "*31,self.totalWeigth(self.parent.roads[i])))
            self.table.appendPlainText("-"*84)

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