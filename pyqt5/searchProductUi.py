# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchProduct.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1011, 768)
        self.btnSearch = QtWidgets.QPushButton(dialog)
        self.btnSearch.setGeometry(QtCore.QRect(30, 670, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")
        self.lblResult = QtWidgets.QLabel(dialog)
        self.lblResult.setGeometry(QtCore.QRect(270, 670, 701, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblResult.setFont(font)
        self.lblResult.setText("")
        self.lblResult.setObjectName("lblResult")
        self.tblProduct = QtWidgets.QTableWidget(dialog)
        self.tblProduct.setGeometry(QtCore.QRect(10, 120, 991, 531))
        self.tblProduct.setObjectName("tblProduct")
        self.tblProduct.setColumnCount(0)
        self.tblProduct.setRowCount(0)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtName = QtWidgets.QLineEdit(dialog)
        self.txtName.setGeometry(QtCore.QRect(100, 20, 481, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtName.setFont(font)
        self.txtName.setObjectName("txtName")
        self.textPrice = QtWidgets.QLineEdit(dialog)
        self.textPrice.setGeometry(QtCore.QRect(100, 70, 481, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textPrice.setFont(font)
        self.textPrice.setObjectName("textPrice")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBoxPrice = QtWidgets.QComboBox(dialog)
        self.comboBoxPrice.setGeometry(QtCore.QRect(620, 70, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxPrice.setFont(font)
        self.comboBoxPrice.setObjectName("comboBoxPrice")
        self.comboBoxPrice.addItem("")
        self.comboBoxPrice.addItem("")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "TNI Shop"))
        self.btnSearch.setText(_translate("dialog", "ค้นหา Product"))
        self.label.setText(_translate("dialog", "ชื่อสินค้า"))
        self.label_2.setText(_translate("dialog", "ราคา"))
        self.comboBoxPrice.setItemText(0, _translate("dialog", "มากกว่า"))
        self.comboBoxPrice.setItemText(1, _translate("dialog", "น้อยกว่า"))