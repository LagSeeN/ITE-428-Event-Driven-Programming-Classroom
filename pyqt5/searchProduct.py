import sys

import pymongo
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem

from searchProductUi import Ui_dialog


class App(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        # Event
        self.display({})
        self.ui.btnSearch.clicked.connect(self.searchProduct)

    def display(self, condition):
        with pymongo.MongoClient(server) as conn:
            db = conn.get_database('TniShop')
            where = condition
            order_by = [('price', -1)]
            count = db['Products'].count_documents(where)
            cursor = db['Products'].find(where).sort(order_by)
            # Table
            self.ui.tblProduct.setRowCount(count)
            self.ui.tblProduct.setColumnCount(5)
            header1 = QtWidgets.QTableWidgetItem('ID')
            header2 = QtWidgets.QTableWidgetItem('Type')
            header3 = QtWidgets.QTableWidgetItem('Name')
            header4 = QtWidgets.QTableWidgetItem('Price')
            header5 = QtWidgets.QTableWidgetItem('Stock')
            self.ui.tblProduct.setHorizontalHeaderItem(0, header1)
            self.ui.tblProduct.setHorizontalHeaderItem(1, header2)
            self.ui.tblProduct.setHorizontalHeaderItem(2, header3)
            self.ui.tblProduct.setHorizontalHeaderItem(3, header4)
            self.ui.tblProduct.setHorizontalHeaderItem(4, header5)

            row = 0
            stock = 0
            for i in cursor:
                self.ui.tblProduct.setItem(row, 0, QTableWidgetItem("{}".format(i['id'])))
                self.ui.tblProduct.setItem(row, 1, QTableWidgetItem("{}".format(i['type'])))
                self.ui.tblProduct.setItem(row, 2, QTableWidgetItem("{}".format(i['name'])))
                self.ui.tblProduct.setItem(row, 3, QTableWidgetItem("{}".format(i['price'])))
                self.ui.tblProduct.setItem(row, 4, QTableWidgetItem("{}".format(i['stock'])))
                stock += i['price'] * i['stock']
                row += 1
            self.ui.lblResult.setText("Found = {} Records (Value in Stock = {:,.2f})".format(count, stock))

    def searchProduct(self):
        options = '$gt' if self.ui.comboBoxPrice.currentIndex() == 0 else '$lt'
        if self.ui.txtName.text().__len__() > 0 and self.ui.textPrice.text().__len__() > 0:
            self.display({'$and': [{'name': {'$regex': self.ui.txtName.text(), '$options': 'i'}},
                                   {'price': {options: int(self.ui.textPrice.text())}}]})
        elif self.ui.txtName.text().__len__() > 0:
            self.display({'name': {'$regex': self.ui.txtName.text(), '$options': 'i'}})
        elif self.ui.textPrice.text().__len__() > 0:
            self.display({'price': {options: int(self.ui.textPrice.text())}})
        else:
            self.display({})


if __name__ == '__main__':
    server = 'mongodb+srv://adisak:RPGnqPNGypIy6bQJ@cluster0.ffnxq.mongodb.net/<dbname>?retryWrites=true&w=majority'
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()
