# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class TableWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("TableWindow.ui",self)
        self.parent = parent
        self.setWindowTitle("Tabla")
        self.setFocus()
        self.table.setReadOnly(True)

"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""