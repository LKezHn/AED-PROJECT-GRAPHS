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
        self.table.appendPlainText("Tabla de Rutas de %s a %s son:"%(self.origin,self.end))
        self.table.appendPlainText("-"*84)
        for i in range(len(self.parent.roads)):
            self.table.appendPlainText("%s"%",".join(self.parent.roads[i]))

"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""