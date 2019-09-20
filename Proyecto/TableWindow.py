# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(389, 319)
        self.table = QtWidgets.QPlainTextEdit(Form)
        self.table.setGeometry(QtCore.QRect(0, 0, 391, 321))
        self.table.setObjectName("table")
        self.table.setReadOnly(True)
        self.table.insertPlainText("self.printSomething")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Tabla", "Tabla"))

    def printSomething(self):
        print(Hola)    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
