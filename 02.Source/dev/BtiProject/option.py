from PySide2 import QtGui, QtWidgets, QtCore


class option(QtWidgets.QWidget):
    def __init__(self, ui):
        self.ui = ui

    def set_directory(self, button):
        selected_directory = QtWidgets.QFileDialog.getExistingDirectory()
        print(button.objectName())

        if button.objectName() == "pushButton_6":
            self.ui.lineEdit.setText(selected_directory)
        elif button.objectName() is "pushButton_7":
            self.ui.lineEdit_2.setText(selected_directory)

    def get_coord(self):
        return self.ui.spinBox.value(), self.ui.spinBox_2.value()

    def get_buffertime(self):
        return self.ui.comboBox_4.currentText()
