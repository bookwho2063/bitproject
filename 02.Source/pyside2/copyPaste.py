"""
# DATE : 19.08.20
# USER : JW
# NOTE : 미디어플레이어 UI 생성 및 미디어 실행 샘플
"""

#!/usr/bin/env python

from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PySide2.QtCore import QObject, SIGNAL, SLOT, QUrl
import cv2
from PySide2.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
        QMainWindow, QPushButton, QSlider, QVBoxLayout, QWidget)


def main():
    # useGUI = not '-no-gui' in sys.argv
    # app = QtWidgets.QApplication.activeWindow() if useGUI else QtCore.QCoreApplication(sys.argv)
    # app.show()

    player = QtMultimedia.QMediaPlayer()
    player.setMedia(QUrl.fromLocalFile("D:/SampleData/albamonSample.mp4"))
    player.setVideoOutput

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Sample Test!!")

    main()

    sys.exit(app.exec_())