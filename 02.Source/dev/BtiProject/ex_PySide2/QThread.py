from PySide2 import QtCore, QtGui, QtWidgets
import time

class Worker(QtCore.QObject):
    error = QtCore.Signal()

    @QtCore.Slot(str)
    def moveLeftIncrement(self, controller):
        if controller == "Controller 1":
            time.sleep(2)
        elif controller == "Controller 2":
            time.sleep(2)
        elif controller == "Controller 3":
            time.sleep(2)
        else:
            self.error.emit("No such controller found!")

    @QtCore.Slot(str)
    def moveRightIncrement(self, controller):
        if controller == "Controller 1":
            time.sleep(2)
        elif controller == "Controller 2":
            time.sleep(2)
        elif controller == "Controller 3":
            time.sleep(2)
        else:
            self.error.emit("No such controller found!")

    @QtCore.Slot(str)
    def moveForwardIncrement(self, controller):
        if controller == "Controller 1":
            time.sleep(2)
        elif controller == "Controller 2":
            time.sleep(2)
        elif controller == "Controller 3":
            time.sleep(2)
        else:
            self.error.emit("No such controller found!")

    @QtCore.Slot(str)
    def moveBackwardIncrement(self, controller):
        print(controller)
        if controller == "Controller 1":
            print("Controller 1 Backward move")
            time.sleep(2)
            print("Controller 1 Backward end")
        elif controller == "Controller 2":
            print("Controller 2 Backward move")
            time.sleep(2)
            print("Controller 2 Backward end")
        elif controller == "Controller 3":
            time.sleep(2)
        else:
            self.error.emit("No such controller found!")

class Window(QtWidgets.QWidget):
    leftClicked = QtCore.Signal(str)
    rightClicked = QtCore.Signal(str)
    forwardClicked = QtCore.Signal(str)
    backwardClicked = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        # self.CONTINUOUS_MOVE_SWITCH = False
        self.title = 'Control Controllers'
        self.left, self.top, self.width, self.height = 10, 10, 320, 100

        self.initUI()

        self.thread = QtCore.QThread(self)
        self.thread.start()
        self.obj = Worker()
        self.obj.moveToThread(self.thread)
        self.leftClicked.connect(self.obj.moveLeftIncrement)
        self.rightClicked.connect(self.obj.moveRightIncrement)
        self.forwardClicked.connect(self.obj.moveForwardIncrement)
        self.backwardClicked.connect(self.obj.moveBackwardIncrement)
        self.obj.error.connect(self.on_error)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        Comp1 = self.createGridLayout("Controller 1")
        Comp2 = self.createGridLayout("Controller 2")
        windowLayout = QtWidgets.QGridLayout(self)
        windowLayout.addWidget(Comp1, 0, 0)
        windowLayout.addWidget(Comp2,0,1)

    def createGridLayout(self, controller):
        """Creates a grid layout for the buttons"""
        box_size = QtCore.QSize(640, 440)
        HGroupBox = QtWidgets.QGroupBox(controller)
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.createButton("left", controller), 2, 1)
        layout.addWidget(self.createButton("right", controller), 2, 3)
        layout.addWidget(self.createButton("forward", controller), 1, 2)
        layout.addWidget(self.createButton("backward", controller), 3, 2)
        HGroupBox.setLayout(layout)
        HGroupBox.setFixedSize(box_size)

        return HGroupBox

    def createButton(self, name, controller):
        button_size = QtCore.QSize(100, 40)
        icon_size = 40
        button = QtWidgets.QPushButton()
        button.Name = name
        button.Controller = controller
        button.Moving = 0
        button.clicked.connect(self.buttonPresssed)
        button.setFixedSize(button_size)
        return button

    # @QtCore.Slot()
    def buttonPresssed(self):
        button = self.sender()

        name = button.Name
        if hasattr(button, 'Controller'):
            controller = button.Controller
            print("The controller selected is", controller)
            if name == 'left':
                self.leftClicked.emit(controller)
            elif name == 'right':
                print("Moved controller right for a single step")
                self.rightClicked.emit(controller)
            elif name == 'forward':
                print("Moved controller forward for a single step")
                self.forwardClicked.emit(controller)
            elif name == 'backward':
                print("Moved controller backward for a single step")
                self.backwardClicked.emit(controller)

    @QtCore.Slot(str)
    def on_error(self, error):
        print(error)

    def closeEvent(self, event):
        self.thread.quit()
        self.thread.wait()
        super(Window, self).closeEvent(event)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())