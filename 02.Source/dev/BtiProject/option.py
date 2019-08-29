from PySide2 import QtGui, QtWidgets, QtCore


class Option(object):
    def __init__(self, ui):
        self.ui = ui

    def set_directory(self, button):
        selected_directory = QtWidgets.QFileDialog.getExistingDirectory()
        print(button.objectName())

        if button.objectName() == "opt_pushButton_urlDownDir":
            self.ui.opt_lineEdit_urlSaveDir.setText(selected_directory)
        elif button.objectName() == "opt_pushButton_saveDir":
            self.ui.opt_lineEdit_saveDir.setText(selected_directory)

    def get_urlSaveDir(self):
        return self.ui.opt_lineEdit_urlSaveDir.Text()

    def get_SaveDir(self):
        return self.ui.opt_lineEdit_saveDir.Text()

    def get_coord(self):
        return self.ui.opt_spinBox_widthValue.value(), self.ui.opt_spinBox_heightValue.value()

    def get_buffertime(self):
        return self.ui.opt_comboBox_bufTime.currentText()

    def get_downFileFmt(self):
        return self.ui.opt_comboBox_downFileFmt.currentText()

    def get_downloadFileDef(self):
        return self.ui.opt_comboBox_downFileDef.currentText()

    def get_coordFileFmt(self):
        return self.ui.opt_comboBox_coordFmt.currentText()
