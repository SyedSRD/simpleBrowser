# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Browser\History.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(385, 418)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.listWHistory = QtWidgets.QListView(Form)
        self.listWHistory.setObjectName("listWHistory")
        self.gridLayout.addWidget(self.listWHistory, 0, 0, 1, 2)
        self.btnClr = QtWidgets.QPushButton(Form)
        self.btnClr.setObjectName("btnClr")
        self.gridLayout.addWidget(self.btnClr, 1, 0, 1, 1)
        self.btnClrAll = QtWidgets.QPushButton(Form)
        self.btnClrAll.setObjectName("btnClrAll")
        self.gridLayout.addWidget(self.btnClrAll, 1, 1, 1, 1)
        self.listWHistory.raise_()
        self.btnClr.raise_()
        self.btnClrAll.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "History"))
        self.btnClr.setText(_translate("Form", "Clear"))
        self.btnClrAll.setText(_translate("Form", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

