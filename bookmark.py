# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Browser\bookmark.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(375, 439)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.listWBM = QtWidgets.QListView(Form)
        self.listWBM.setObjectName("listWBM")
        self.gridLayout.addWidget(self.listWBM, 0, 0, 1, 2)
        self.btnBClr = QtWidgets.QPushButton(Form)
        self.btnBClr.setObjectName("btnBClr")
        self.gridLayout.addWidget(self.btnBClr, 1, 0, 1, 1)
        self.btnBClrAll = QtWidgets.QPushButton(Form)
        self.btnBClrAll.setObjectName("btnBClrAll")
        self.gridLayout.addWidget(self.btnBClrAll, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bookmark"))
        self.btnBClr.setText(_translate("Form", "Clear"))
        self.btnBClrAll.setText(_translate("Form", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

