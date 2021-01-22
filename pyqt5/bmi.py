# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BMI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblBMI = QtWidgets.QLabel(Dialog)
        self.lblBMI.setGeometry(QtCore.QRect(20, 90, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblBMI.setFont(font)
        self.lblBMI.setText("")
        self.lblBMI.setObjectName("lblBMI")
        self.textWeight = QtWidgets.QTextEdit(Dialog)
        self.textWeight.setGeometry(QtCore.QRect(90, 10, 131, 31))
        self.textWeight.setObjectName("textWeight")
        self.textHeight = QtWidgets.QTextEdit(Dialog)
        self.textHeight.setGeometry(QtCore.QRect(90, 50, 131, 31))
        self.textHeight.setObjectName("textHeight")
        self.btnShowBMI = QtWidgets.QPushButton(Dialog)
        self.btnShowBMI.setGeometry(QtCore.QRect(90, 130, 121, 41))
        self.btnShowBMI.setToolTip("")
        self.btnShowBMI.setObjectName("btnShowBMI")
        self.btnReset = QtWidgets.QPushButton(Dialog)
        self.btnReset.setGeometry(QtCore.QRect(230, 130, 121, 41))
        self.btnReset.setObjectName("btnReset")
        self.btnOpenProducts = QtWidgets.QPushButton(Dialog)
        self.btnOpenProducts.setGeometry(QtCore.QRect(90, 190, 121, 41))
        self.btnOpenProducts.setToolTip("")
        self.btnOpenProducts.setObjectName("btnOpenProducts")

        self.btnShowBMI.clicked.connect(self.ShowResult)
        self.btnReset.clicked.connect(self.resetButton)
        self.btnOpenProducts.clicked.connect(self.openProduct)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "น้ำหนัก"))
        self.label_2.setText(_translate("Dialog", "ส่วนสูง"))
        self.btnShowBMI.setText(_translate("Dialog", "คำนวณ BMI"))
        self.btnReset.setText(_translate("Dialog", "ล้างข้อมูล"))
        self.btnOpenProducts.setText(_translate("Dialog", "เปิดหน้าจอ Products"))

    def ShowResult(self):
        w = float(self.textWeight.toPlainText())
        h = float(self.textHeight.toPlainText()) / 100
        bmi = w / pow(h, 2)
        text = 'BMI = {:.2f}'.format(bmi)
        if bmi >= 30:
            text += '\t อ้วนมาก'
        elif bmi >= 25:
            text += '\t อ้วน'
        elif bmi >= 23:
            text += '\t ท้วม'
        elif bmi >= 18.5:
            text += '\t ปกติ'
        else:
            text += '\t ผอมเกินไป'
        self.lblBMI.setText('{}'.format(text))

    def resetButton(self):
        self.textHeight.clear()
        self.textWeight.clear()
        self.lblBMI.clear()
        self.textWeight.setFocus()

    def openProduct(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = tnishop.Ui_TNISHOP()
        self.ui.setupUi(self.window)
        self.window.show()




if __name__ == "__main__":
    import sys
    import tnishop

    app = QtWidgets.QApplication(sys.argv)
    bmi = QtWidgets.QDialog()
    ui = Ui_BMI()
    ui.setupUi(bmi)
    bmi.show()
    sys.exit(app.exec_())
