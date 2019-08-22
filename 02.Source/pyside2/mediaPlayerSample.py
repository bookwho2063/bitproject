"""
# DATE : 19.08.20
# USER : JW
# NOTE : 미디어플레이어 UI 생성 및 미디어 실행 샘플
"""

#!/usr/bin/env python

from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
import cv2
from PySide2.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
        QMainWindow, QPushButton, QSlider, QVBoxLayout, QWidget)



#class MediaArea(QtMultimediaWidgets.QVideoWidget):
class MediaArea(QMainWindow):
    def __init__(self, parent=None):
        super(MediaArea, self).__init__(parent)


        # self.createDockWidget()



    def createDockWidget(self):
        """
        # Create Dock Example
        # (별도의 도커를 만들어 메인 안에 붙인다, 메뉴바가 있어서 팝업처럼 쓸수 있는데 필요없을듯
        :return:
        """
        tLabel = QLabel("asdasdasd")
        dockWidget = QtWidgets.QDockWidget(QObject.tr(self,"Dock Widget"), self)
        dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dockWidget.setWidget(tLabel)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)



if __name__ == "__main__":
    import sys

    testApp = QApplication(sys.argv)
    testApp.setApplicationName("영상나오니?")
    mainWindow = MediaArea()
    mainWindow.resize(400,300)

    tLabel = QLabel(mainWindow)
    tLabel.resize(300,200)

    vWidget = QtMultimediaWidgets.QVideoWidget(mainWindow)
    vWidget.resize(mainWindow.size())
    # vWidget = QtMultimediaWidgets.QVideoWidget(tLabel)




    # media area
    player = QtMultimedia.QMediaPlayer(mainWindow)
    # player = QtMultimedia.QMediaPlayer(tLabel)
    player.setMedia(QUrl.fromLocalFile("D:\\SampleData\\albamonSample.mp4"))
    # player.setMedia(QUrl.fromLocalFile("D:\\videoSample\\E01.mp4"))

    player.setVideoOutput(vWidget)
    # playList = QtMultimedia.QMediaPlaylist(player)
    # playList.addMedia(QUrl.fromLocalFile("D:/SampleData/albamonSample.mp4"))

    # frame = QtMultimedia.QVideoFrame(player)


    ## Running
    mainWindow.show()
    player.play()
    testApp.exec_()