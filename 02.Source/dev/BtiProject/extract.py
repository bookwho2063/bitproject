from PySide2 import QtGui, QtWidgets, QtCore

class extract(object):

    def __init__(self, ui):
        self.table = ui.tableWidget

    def add_list(self):
        # list = [4, "01:13", 3, "아이린", "...", "4"]
        count_row = self.table.rowCount()

        self.table.insertRow(count_row)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(count_row,0,item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(count_row,1,item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(count_row,2,item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(count_row,3,item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(count_row,4,item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(count_row,5,item)

        self.table.item(count_row,0).setText(QtWidgets.QApplication.translate("Form","3",None,-1))
        self.table.item(count_row,1).setText(QtWidgets.QApplication.translate("Form","01:13-01:18",None,-1))
        self.table.item(count_row,2).setText(QtWidgets.QApplication.translate("Form","3",None,-1))
        self.table.item(count_row,3).setText(QtWidgets.QApplication.translate("Form","아이린",None,-1))
        self.table.item(count_row,4).setText(QtWidgets.QApplication.translate("Form","...",None,-1))
        self.table.item(count_row,5).setText(QtWidgets.QApplication.translate("Form","3",None,-1))