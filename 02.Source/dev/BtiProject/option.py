from PySide2 import QtGui, QtWidgets, QtCore


class option(QtWidgets.QWidget):
    def __init__(self, ui):
        self.ui = ui

    def set_directory(self, button):
        selected_directory = QtWidgets.QFileDialog.getExistingDirectory()
        print(button.objectName())

        if button.objectName() == "opt_pushButton_6":
            self.ui.opt_lineEdit.setText(selected_directory)
        elif button.objectName() == "opt_pushButton_7":
            self.ui.opt_lineEdit_2.setText(selected_directory)

    def get_coord(self):
        return self.ui.opt_spinBox.value(), self.ui.opt_spinBox_2.value()

    def get_buffertime(self):
        return self.ui.opt_comboBox_4.currentText()
