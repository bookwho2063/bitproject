import sys
from PySide2.QtCore    import *
from PySide2.QtGui     import *
from PySide2.QtWidgets import *

class Label(QLabel):
    def __init__(self, *args, antialiasing=True, **kwargs):
        super(Label, self).__init__(*args, **kwargs)
        self.Antialiasing = antialiasing
        self.setMaximumSize(100, 100)
        self.setMinimumSize(100, 100)
        self.radius = 100

        self.target = QPixmap(self.size())
        self.target.fill(Qt.transparent)

        # p = QPixmap("D:/sampleImg/image2.jpg").scaled(
        #     50, 50, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        p = QPixmap("D:/sampleImg/image2.jpg").scaled(100, 100)

        painter = QPainter(self.target)
        if self.Antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(
            0, 0, self.width(), self.height(), self.radius, self.radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.setPixmap(self.target)

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        layout.addWidget(Label(self))
        # layout.addWidget(Label(self, antialiasing=False))
        self.setStyleSheet("background: blue;")

    def createThumnail(self, qImage, width, height, radius, antialiasing=True):
        """
        qImage 형식의 img 데이터를 이용하여 width/height 크기로
        원형 썸네일 QPixmap 생성 후 Label에 입력하여 리턴
        :param qImage:
        :param width:
        :param height:
        :return: img in Label(QPixmap)
        """

        resultLabel = QLabel()
        resultLabel.setMaximumSize(width, height)
        resultLabel.setMinimumSize(width, height)
        target = QPixmap(resultLabel.size())
        target.fill(Qt.transparent)

        opt_radius = 25
        opt_antialiasing = True

        # imgData = QtGui.QPixmap(QtGui.QImage(qImage))\
        #     .scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

        imgData = QPixmap(QImage(qImage)).scaled(width, height)
        painter = QPainter(target)
        if antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(
            0, 0, resultLabel.width(), resultLabel.height(), radius, radius
        )

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, imgData)
        resultLabel.setPixmap(target)

        return resultLabel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())