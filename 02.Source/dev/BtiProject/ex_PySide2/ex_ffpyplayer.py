from PySide2 import QtCore, QtGui, QtWidgets
import cv2, time
from ffpyplayer.player import MediaPlayer

class Thread(QtCore.QThread):
    changePixmap = QtCore.Signal(QtGui.QImage)


    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent=parent)
        self.file_path = "d:/extractSection/test.mp4"
        self.openVideo()
        self.play = True

    def run(self):
        while True:

            if self.play:
                self.player.set_pause(False)
                ret,frame = self.cap.read()
                # audio_frame,val = self.player.get_frame()

                if ret:
                    rgbImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    h,w,ch = rgbImage.shape
                    bytesPerLine = ch * w
                    convertToQtFormat = QtGui.QImage(rgbImage.data,w,h,bytesPerLine,QtGui.QImage.Format_RGB888)
                    p = convertToQtFormat.scaled(640,480,QtCore.Qt.KeepAspectRatio)
                    self.changePixmap.emit(p)

            time.sleep(0.025)



    def pauseVideo(self):
        self.play = False
        self.player.set_pause(True)

    def playVideo(self):
        self.play = True
        # self.player.set_pause(False)

    def stopVideo(self):
        pass

    def openVideo(self):
        self.cap = cv2.VideoCapture(self.file_path)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,1)
        self.player = MediaPlayer(self.file_path)
        self.player.set_pause(True)



class Ui_Form(QtCore.QObject):

    def setupUi(self, Form):
        Form.setObjectName("Player")
        Form.resize(640, 480)
        self.horizontalLayout = QtWidgets.QVBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # label
        self.label = QtWidgets.QLabel(Form)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("Background-color: #000;")
        self.horizontalLayout.addWidget(self.label)
        self.button = QtWidgets.QPushButton(Form)
        self.button.setText("open")
        self.button.name = "open"
        self.horizontalLayout.addWidget(self.button)

        # tool bar

        self.toolLayout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        self.toolLayout.setContentsMargins(0,0,0,0)
        self.toolbar = QtWidgets.QToolBar()
        self.toolLayout.addWidget(self.toolbar)

        self.playAction = QtWidgets.QAction("&Play",self)
        self.playAction.setIcon(QtGui.QIcon("icon/play.png"))
        self.toolbar.addAction(self.playAction)


        self.pauseAction = QtWidgets.QAction("&Pause",self)

        self.pauseAction.setIcon(QtGui.QIcon("icon/pause.png"))
        self.toolbar.addAction(self.pauseAction)

        self.stopAction = QtWidgets.QAction("&Stop", self)
        self.stopAction.setIcon(QtGui.QIcon("icon/stop.png"))
        self.toolbar.addAction(self.stopAction)



        self.horizontalLayout.addLayout(self.toolLayout)

        self.th = Thread(self)
        self.th.changePixmap.connect(lambda p: self.setPixMap(p))

        self.button.clicked.connect(self.buttonClicked)
        self.playAction.triggered.connect(self.actionTriggered)
        self.pauseAction.triggered.connect(self.actionTriggered)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def actionTriggered(self):
        action = self.sender()
        print(action.objectName())

        if self.th.play:
            self.th.pauseVideo()
        else:
            self.th.playVideo()


    def buttonClicked(self):
        self.th.start()
        # button = self.sender()
        # cap = cv2.imread("C:/Users/bit/Documents/mycode/extractSection/test.mp4")
        #
        # while True:
        #     ret, frame = cap.read()
        #     frame = frame.astype(np.uint8, order='C')
        #
        #     if ret:
        #         rgbImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        #         h,w,ch = rgbImage.shape
        #         bytesPerLine = ch * w
        #         convertToQtFormat = QtGui.QImage(rgbImage.data,w,h,bytesPerLine,QtGui.QImage.Format_RGB888)
        #         p = convertToQtFormat.scaled(640,480, QtCore.Qt.KeepAspectRatio)
        #         pixmap = QtGui.QPixmap.fromImage(p)
        #         print(pixmap)
        #         self.label.setPixmap(pixmap)
        #
        #         # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #         # img = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QtGui.QImage.Format_RGB888)
        #         # img = QtGui.QPixmap.fromImage(img)
        #         # pixmap = QtGui.QPixmap(img)
        #         # print(pixmap)
        #         # # self.label.setPixmap(pixmap)
        #         time.sleep(2)


    @QtCore.Slot(QtGui.QImage)
    def setPixMap(self,p):
        p = QtGui.QPixmap.fromImage(p)
        p = p.scaled(640,480, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(p)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Player", "Player", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Player", "IMAGE", None, -1))

    def closeEvent(self, event):
        self.th.quit()
        self.th.wait()
        super(Ui_Form, self).closeEvent(event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

