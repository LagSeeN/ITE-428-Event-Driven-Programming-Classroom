import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox

from NewBMIUI import Ui_Dialog


class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Event
        self.ui.btnBMI.clicked.connect(self.ShowResult)
        self.ui.btnExit.clicked.connect(QtCore.QCoreApplication.quit)

    def ShowResult(self):
        if self.ui.weightInput.text().__len__() == 0 or not self.ui.weightInput.text().isdigit():
            QMessageBox.about(self, "ERROR", "โปรดป้อนน้ำหนักให้ถูกต้อง")
        if self.ui.heightInput.text().__len__() == 0 or not self.ui.heightInput.text().isdigit():
            QMessageBox.about(self, "ERROR", "โปรดป้อนส่วนสูงให้ถูกต้อง")
        if self.ui.weightInput.text().isdigit() and self.ui.heightInput.text().isdigit():
            w = float(self.ui.weightInput.text())
            h = float(self.ui.heightInput.text()) / 100
            if self.ui.radioButtonRed.isChecked():
                self.ui.showBMI.setStyleSheet("color: rgb(255, 0, 0);")
                self.ui.showStatus.setStyleSheet("color: rgb(255, 0, 0);")
            elif self.ui.radioButtonGreen.isChecked():
                self.ui.showBMI.setStyleSheet("color: rgb(0, 255, 0);")
                self.ui.showStatus.setStyleSheet("color: rgb(0, 255, 0);")
            elif self.ui.radioButtonYellow.isChecked():
                self.ui.showBMI.setStyleSheet("color: rgb(255, 255, 0);")
                self.ui.showStatus.setStyleSheet("color: rgb(255, 255, 0);")
            else:
                self.ui.showBMI.setStyleSheet("color: rgb(0, 0, 0);")
                self.ui.showStatus.setStyleSheet("color: rgb(0, 0, 0);")
            if self.ui.comboBoxSelectDIgit.currentIndex() == 0:
                num_digit = 0
            elif self.ui.comboBoxSelectDIgit.currentIndex() == 1:
                num_digit = 1
            elif self.ui.comboBoxSelectDIgit.currentIndex() == 2:
                num_digit = 2
            elif self.ui.comboBoxSelectDIgit.currentIndex() == 3:
                num_digit = 3
            bmi = w / pow(h, 2)
            self.ui.showBMI.setText('Your BMI = {:.{}f}'.format(bmi, num_digit))
            if self.ui.checkShowStatus.isChecked():
                self.ui.showStatus.show()
                if bmi >= 30:
                    status = 'อ้วนมาก'
                elif bmi >= 25:
                    status = 'อ้วน'
                elif bmi >= 23:
                    status = 'ท้วม'
                elif bmi >= 18.5:
                    status = 'ปกติ'
                else:
                    status = 'ผอมเกินไป'
                self.ui.showStatus.setText('Status : {}'.format(status))
            else:
                self.ui.showStatus.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindows()
    form.show()
    app.exec_()
