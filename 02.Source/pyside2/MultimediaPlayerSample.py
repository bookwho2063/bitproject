#!/usr/bin/env python

"""PySide2 Multimedia player example"""

import sys
from PySide2.QtCore import SLOT, QStandardPaths, Qt
from PySide2.QtGui import QIcon, QKeySequence
from PySide2.QtWidgets import (QAction, QApplication, QDialog, QFileDialog,
    QMainWindow, QMenu, QMenuBar, QSlider, QStyle, QToolBar)
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide2.QtMultimediaWidgets import QVideoWidget



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.playlist = QMediaPlaylist()
        self.player = QMediaPlayer()

        # Setting QToolBar
        toolBar = QToolBar()
        self.addToolBar(toolBar)

        fileMenu = self.menuBar().addMenu("&File")
        openAction = QAction(QIcon.fromTheme("document-open"),
                             "&Open...", self, shortcut=QKeySequence.Open,
                             triggered=self.open)
        fileMenu.addAction(openAction)
        exitAction = QAction(QIcon.fromTheme("application-exit"), "E&xit",
                             self, shortcut="Ctrl+Q", triggered=self.close)
        fileMenu.addAction(exitAction)

        playMenu = self.menuBar().addMenu("&Play")
        playIcon = self.style().standardIcon(QStyle.SP_MediaPlay)
        self.playAction = toolBar.addAction(playIcon, "Play")
        self.playAction.triggered.connect(self.player.play)
        playMenu.addAction(self.playAction)

        previousIcon = self.style().standardIcon(QStyle.SP_MediaSkipBackward)
        self.previousAction = toolBar.addAction(previousIcon, "Previous")
        self.previousAction.triggered.connect(self.previousClicked)
        playMenu.addAction(self.previousAction)

        pauseIcon = self.style().standardIcon(QStyle.SP_MediaPause)
        self.pauseAction = toolBar.addAction(pauseIcon, "Pause")
        self.pauseAction.triggered.connect(self.player.pause)
        playMenu.addAction(self.pauseAction)

        nextIcon = self.style().standardIcon(QStyle.SP_MediaSkipForward)
        self.nextAction = toolBar.addAction(nextIcon, "Next")
        self.nextAction.triggered.connect(self.playlist.next)
        playMenu.addAction(self.nextAction)

        stopIcon = self.style().standardIcon(QStyle.SP_MediaStop)
        self.stopAction = toolBar.addAction(stopIcon, "Stop")
        self.stopAction.triggered.connect(self.player.stop)
        playMenu.addAction(self.stopAction)

        # Setting the QSlider
        self.volSlider = QSlider()
        self.volSlider.setOrientation(Qt.Horizontal)
        self.volSlider.setMinimum(0)
        self.volSlider.setMaximum(100)
        self.volSlider.setFixedWidth(120)
        self.volSlider.setValue(self.player.volume())
        self.volSlider.setTickInterval(10)
        self.volSlider.setTickPosition(QSlider.TicksBelow)
        self.volSlider.setToolTip("Volume")
        self.volSlider.valueChanged.connect(self.player.setVolume)
        toolBar.addWidget(self.volSlider)

        aboutMenu = self.menuBar().addMenu("&About")
        aboutQtAct = QAction("About &Qt", self, triggered=QApplication.aboutQt)
        aboutMenu.addAction(aboutQtAct)

        self.videoWidget = QVideoWidget()
        self.setCentralWidget(self.videoWidget)
        self.player.setPlaylist(self.playlist);
        self.player.stateChanged.connect(self.updateButtons)
        self.player.setVideoOutput(self.videoWidget);

        self.updateButtons(self.player.state())

    def open(self):
        fileDialog = QFileDialog(self)
        supportedMimeTypes = ["video/mp4", "*.*"]
        fileDialog.setMimeTypeFilters(supportedMimeTypes)
        moviesLocation = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        fileDialog.setDirectory(moviesLocation)
        if fileDialog.exec_() == QDialog.Accepted:
            self.playlist.addMedia(fileDialog.selectedUrls()[0])
            self.player.play()

    def previousClicked(self):
        # Go to previous track if we are within the first 5 seconds of playback
        # Otherwise, seek to the beginning.
        if self.player.position() <= 5000:
            self.playlist.previous();
        else:
            self.player.setPosition(0);

    def updateButtons(self, state):
        mediaCount = self.playlist.mediaCount()
        self.playAction.setEnabled(mediaCount > 0
            and state != QMediaPlayer.PlayingState)
        self.pauseAction.setEnabled(state == QMediaPlayer.PlayingState)
        self.stopAction.setEnabled(state != QMediaPlayer.StoppedState)
        self.previousAction.setEnabled(self.player.position() > 0)
        self.nextAction.setEnabled(mediaCount > 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.resize(800, 600)
    mainWin.show()
    sys.exit(app.exec_())