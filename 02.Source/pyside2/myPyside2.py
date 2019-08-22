#-------------------------------------------------
# Made By jw
# Date : 19.08.14
# Title : First pyside Sample
#-------------------------------------------------

import sys
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2 import QtCore, QtGui, QtWidgets

class Main(object):
    def setupUi(self, Form):
        ...

    def retranslateUi(self, Form):
        ...


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Main()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())