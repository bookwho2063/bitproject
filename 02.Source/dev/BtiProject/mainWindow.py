# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bit/PycharmProjects/BtiProject/ui/mainWindow.ui',
# licensing of 'C:/Users/bit/PycharmProjects/BtiProject/ui/mainWindow.ui' applies.
#
# Created: Tue Sep  3 14:13:37 2019
#      by: pyside2-uic  running on PySide2 5.9.0~a1
#
# WARNING! All changes made in this file will be lost!

"""
#   TEAM        : 휴먼, 미쳐도 괜찮아 (박준욱, 송원빈)
#   CLASSNAME   : common_190923.py
#   COMMENT     : 공통 함수 및 변수 클래스
#   LASY MOD    : 19.08.27
"""

from PySide2 import QtCore, QtGui, QtWidgets
from common import common,cv_video_player
from extract import Extract
from option import Option
from time import sleep
import datetime
import os

class Ui_Form(QtCore.QObject):
    def setupUi(self, Form):
        ########
        #	Main Form Default
        #	- 메인 폼
        ########
        Form.setObjectName("Form")
        Form.resize(1280, 840)
        Form.setMinimumSize(QtCore.QSize(1280, 840))
        # self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.stackedLayout = QtWidgets.QStackedLayout(Form)
        self.stackedLayout.setObjectName("stackedLayout")
        self.stackedLayout.setStackingMode(QtWidgets.QStackedLayout.StackAll)

        #####################################
        #### 로딩 창
        # 0 : loading 창
        # 1 : mainTab
        #####################################
        self.loading_label = QtWidgets.QLabel("loading_label")
        self.loading_label.setStyleSheet("background-color: rgba(25,25,25,70%);")
        movie = QtGui.QMovie("icon/loading.gif")
        movie.start()
        self.loading_label.setMovie(movie)
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stackedLayout.addWidget(self.loading_label)

        ########
        #	Main tab Default
        #	- 탭 전체 공통 옵션
        ########
        self.mainTabWidget = QtWidgets.QTabWidget(Form)
        self.mainTabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("나눔고딕코딩")
        font.setPointSize(14)
        self.mainTabWidget.setFont(font)
        self.mainTabWidget.setObjectName("mainTabWidget")

        ########
        #	extTab Default
        #	- 영상검출탭
        ########
        self.tab_ext = QtWidgets.QWidget()
        self.tab_ext.setEnabled(True)
        self.tab_ext.setObjectName("tab_ext")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_ext)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ext_verticalLayout_top = QtWidgets.QVBoxLayout()
        self.ext_verticalLayout_top.setObjectName("ext_verticalLayout_top")
        self.ext_horizontalLayout_top = QtWidgets.QHBoxLayout()
        self.ext_horizontalLayout_top.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.ext_horizontalLayout_top.setObjectName("ext_horizontalLayout_top")
        self.ext_pushButton_localUpload = QtWidgets.QPushButton(self.tab_ext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_pushButton_localUpload.sizePolicy().hasHeightForWidth())
        self.ext_pushButton_localUpload.setSizePolicy(sizePolicy)
        self.ext_pushButton_localUpload.setMinimumSize(QtCore.QSize(0, 57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ext_pushButton_localUpload.setFont(font)
        self.ext_pushButton_localUpload.setObjectName("ext_pushButton_localUpload")
        self.ext_horizontalLayout_top.addWidget(self.ext_pushButton_localUpload)
        self.ext_pushButton_urlUpload = QtWidgets.QPushButton(self.tab_ext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_pushButton_urlUpload.sizePolicy().hasHeightForWidth())
        self.ext_pushButton_urlUpload.setSizePolicy(sizePolicy)
        self.ext_pushButton_urlUpload.setMinimumSize(QtCore.QSize(0, 57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ext_pushButton_urlUpload.setFont(font)
        self.ext_pushButton_urlUpload.setObjectName("ext_pushButton_urlUpload")
        self.ext_horizontalLayout_top.addWidget(self.ext_pushButton_urlUpload)
        self.ext_pushButton_startExt = QtWidgets.QPushButton(self.tab_ext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_pushButton_startExt.sizePolicy().hasHeightForWidth())
        self.ext_pushButton_startExt.setSizePolicy(sizePolicy)
        self.ext_pushButton_startExt.setMaximumSize(QtCore.QSize(16777215, 57))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ext_pushButton_startExt.setFont(font)
        self.ext_pushButton_startExt.setObjectName("ext_pushButton_startExt")
        self.ext_horizontalLayout_top.addWidget(self.ext_pushButton_startExt)
        self.ext_pushButton_mdDown = QtWidgets.QPushButton(self.tab_ext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_pushButton_mdDown.sizePolicy().hasHeightForWidth())
        self.ext_pushButton_mdDown.setSizePolicy(sizePolicy)
        self.ext_pushButton_mdDown.setMinimumSize(QtCore.QSize(0, 57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ext_pushButton_mdDown.setFont(font)
        self.ext_pushButton_mdDown.setObjectName("ext_pushButton_mdDown")
        self.ext_horizontalLayout_top.addWidget(self.ext_pushButton_mdDown)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ext_horizontalLayout_top.addItem(spacerItem)
        self.ext_tableWidget_classList = QtWidgets.QTableWidget(self.tab_ext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_tableWidget_classList.sizePolicy().hasHeightForWidth())
        self.ext_tableWidget_classList.setSizePolicy(sizePolicy)
        self.ext_tableWidget_classList.setMinimumSize(QtCore.QSize(630,80))
        self.ext_tableWidget_classList.setMaximumSize(QtCore.QSize(16777215, 80))
        self.ext_tableWidget_classList.setObjectName("ext_tableWidget_classList")

        self.ext_tableWidget_classList.setColumnCount(10)
        self.ext_tableWidget_classList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ext_tableWidget_classList.setRowCount(1)
        self.ext_tableWidget_classList.horizontalHeader().hide()
        self.ext_tableWidget_classList.verticalHeader().hide()
        self.ext_tableWidget_classList.setShowGrid(False)
        self.ext_tableWidget_classList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.ext_horizontalLayout_top.addWidget(self.ext_tableWidget_classList)
        self.ext_verticalLayout_top.addLayout(self.ext_horizontalLayout_top)
        self.verticalLayout_8.addLayout(self.ext_verticalLayout_top)
        self.ext_splitter_Md = QtWidgets.QSplitter(self.tab_ext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_splitter_Md.sizePolicy().hasHeightForWidth())
        self.ext_splitter_Md.setSizePolicy(sizePolicy)
        self.ext_splitter_Md.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ext_splitter_Md.setOrientation(QtCore.Qt.Horizontal)
        self.ext_splitter_Md.setOpaqueResize(True)
        self.ext_splitter_Md.setChildrenCollapsible(False)
        self.ext_splitter_Md.setObjectName("ext_splitter_Md")
        self.ext_widget_video_Md = QtWidgets.QWidget(self.ext_splitter_Md)
        self.ext_widget_video_Md.setObjectName("ext_widget_video_Md")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ext_widget_video_Md)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ext_label_extMd = QtWidgets.QLabel(self.ext_widget_video_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_label_extMd.sizePolicy().hasHeightForWidth())
        self.ext_label_extMd.setSizePolicy(sizePolicy)
        self.ext_label_extMd.setMinimumSize(QtCore.QSize(480, 0))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.ext_label_extMd.setFont(font)
        self.ext_label_extMd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ext_label_extMd.setAlignment(QtCore.Qt.AlignCenter)
        self.ext_label_extMd.setObjectName("ext_label_extMd")
        self.ext_label_extMd.setStyleSheet("border: 1px solid gray; background-color: QColor(25,25,25);")
        self.verticalLayout_7.addWidget(self.ext_label_extMd)
        self.ext_horizontalLayout_mid1 = QtWidgets.QHBoxLayout()
        self.ext_horizontalLayout_mid1.setObjectName("ext_horizontalLayout_mid1")
        self.ext_horizontalLayout_mid2 = QtWidgets.QHBoxLayout()
        self.ext_horizontalLayout_mid2.setObjectName("ext_horizontalLayout_mid2")
        self.ext_pushButton_play = QtWidgets.QPushButton(self.ext_widget_video_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_pushButton_play.sizePolicy().hasHeightForWidth())
        self.ext_pushButton_play.setSizePolicy(sizePolicy)
        self.ext_pushButton_play.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ext_pushButton_play.setIcon(icon)
        self.ext_pushButton_play.setIconSize(QtCore.QSize(32, 32))
        self.ext_pushButton_play.setObjectName("ext_pushButton_play")
        self.ext_horizontalLayout_mid2.addWidget(self.ext_pushButton_play)
        self.ext_pushButton_pause = QtWidgets.QPushButton(self.ext_widget_video_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_pushButton_pause.sizePolicy().hasHeightForWidth())
        self.ext_pushButton_pause.setSizePolicy(sizePolicy)
        self.ext_pushButton_pause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ext_pushButton_pause.setIcon(icon1)
        self.ext_pushButton_pause.setIconSize(QtCore.QSize(32, 32))
        self.ext_pushButton_pause.setObjectName("ext_pushButton_pause")
        self.ext_horizontalLayout_mid2.addWidget(self.ext_pushButton_pause)
        self.ext_pushButton_stop = QtWidgets.QPushButton(self.ext_widget_video_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_pushButton_stop.sizePolicy().hasHeightForWidth())
        self.ext_pushButton_stop.setSizePolicy(sizePolicy)
        self.ext_pushButton_stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ext_pushButton_stop.setIcon(icon2)
        self.ext_pushButton_stop.setIconSize(QtCore.QSize(32, 32))
        self.ext_pushButton_stop.setObjectName("ext_pushButton_stop")
        self.ext_horizontalLayout_mid2.addWidget(self.ext_pushButton_stop)
        self.ext_horizontalLayout_mid1.addLayout(self.ext_horizontalLayout_mid2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ext_horizontalLayout_mid1.addItem(spacerItem1)
        self.ext_video_time = QtWidgets.QLabel(self.ext_widget_video_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_video_time.sizePolicy().hasHeightForWidth())
        self.ext_video_time.setSizePolicy(sizePolicy)
        self.ext_video_time.setTextFormat(QtCore.Qt.AutoText)
        self.ext_video_time.setScaledContents(False)
        self.ext_video_time.setMargin(0)
        self.ext_video_time.setObjectName("ext_video_time")
        self.ext_horizontalLayout_mid1.addWidget(self.ext_video_time)
        self.verticalLayout_7.addLayout(self.ext_horizontalLayout_mid1)
        self.ext_widget_result_Md = QtWidgets.QWidget(self.ext_splitter_Md)
        self.ext_widget_result_Md.setStyleSheet("border: 1px solid gray;")
        self.ext_widget_result_Md.setObjectName("ext_widget_result_Md")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ext_widget_result_Md)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ext_tableView_extResultList = QtWidgets.QTableView(self.ext_widget_result_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_tableView_extResultList.sizePolicy().hasHeightForWidth())
        self.ext_tableView_extResultList.setSizePolicy(sizePolicy)
        self.ext_tableView_extResultList.setMinimumSize(QtCore.QSize(480, 0))
        self.ext_tableView_extResultList.setObjectName("ext_tableView_extResultList")

        self.ext_tableView_extResultList.setIconSize(QtCore.QSize(50,50))

        # 테이블 Row 데이터 색상
        self.ext_tableView_extResultList.setAlternatingRowColors(False)

        # 추출결과테이블 헤더정보 설정
        self.ext_default_tHeader_setting()

        # 테이블 Row Grid show()
        self.ext_tableView_extResultList.setShowGrid(False)

        self.verticalLayout_6.addWidget(self.ext_tableView_extResultList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 34, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ext_pushButton_allClear = QtWidgets.QPushButton(self.ext_widget_result_Md)
        self.ext_pushButton_allClear.setMinimumSize(QtCore.QSize(0, 34))
        self.ext_pushButton_allClear.setMaximumSize(QtCore.QSize(16777215, 57))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ext_pushButton_allClear.setFont(font)
        self.ext_pushButton_allClear.setIconSize(QtCore.QSize(32, 32))
        self.ext_pushButton_allClear.setObjectName("ext_pushButton_allClear")
        self.horizontalLayout.addWidget(self.ext_pushButton_allClear)
        self.ext_pushButton_selectDelete = QtWidgets.QPushButton(self.ext_widget_result_Md)
        self.ext_pushButton_selectDelete.setMaximumSize(QtCore.QSize(16777215, 57))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ext_pushButton_selectDelete.setFont(font)
        self.ext_pushButton_selectDelete.setObjectName("ext_pushButton_selectDelete")
        self.horizontalLayout.addWidget(self.ext_pushButton_selectDelete)
        # self.ext_pushButton_allSave = QtWidgets.QPushButton(self.ext_widget_result_Md)
        # self.ext_pushButton_allSave.setMaximumSize(QtCore.QSize(16777215, 57))
        # font = QtGui.QFont()
        # font.setPointSize(9)
        # self.ext_pushButton_allSave.setFont(font)
        # self.ext_pushButton_allSave.setObjectName("ext_pushButton_allSave")
        # self.horizontalLayout.addWidget(self.ext_pushButton_allSave)
        # self.ext_pushButton_selectSave = QtWidgets.QPushButton(self.ext_widget_result_Md)
        # self.ext_pushButton_selectSave.setMaximumSize(QtCore.QSize(16777215, 57))
        # font = QtGui.QFont()
        # font.setPointSize(9)
        # self.ext_pushButton_selectSave.setFont(font)
        # self.ext_pushButton_selectSave.setObjectName("ext_pushButton_selectSave")
        # self.horizontalLayout.addWidget(self.ext_pushButton_selectSave)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_8.addWidget(self.ext_splitter_Md)
        self.mainTabWidget.addTab(self.tab_ext, "영상클립")

        ########
        #	afcTab Default
        #	- 오토포커싱탭
        ########
        self.tab_afc = QtWidgets.QWidget()
        self.tab_afc.setObjectName("tab_afc")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_afc)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.afc_verticalLayout_top = QtWidgets.QVBoxLayout()
        self.afc_verticalLayout_top.setObjectName("afc_verticalLayout_top")
        self.afc_horizontalLayout_top = QtWidgets.QHBoxLayout()
        self.afc_horizontalLayout_top.setObjectName("afc_horizontalLayout_top")
        self.afc_pushButton_localUpload = QtWidgets.QPushButton(self.tab_afc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_pushButton_localUpload.sizePolicy().hasHeightForWidth())
        self.afc_pushButton_localUpload.setSizePolicy(sizePolicy)
        self.afc_pushButton_localUpload.setMinimumSize(QtCore.QSize(0, 0))
        self.afc_pushButton_localUpload.setMaximumSize(QtCore.QSize(16777215, 57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.afc_pushButton_localUpload.setFont(font)
        self.afc_pushButton_localUpload.setObjectName("afc_pushButton_localUpload")
        self.afc_horizontalLayout_top.addWidget(self.afc_pushButton_localUpload)
        self.afc_pushButton_urlUpload = QtWidgets.QPushButton(self.tab_afc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_pushButton_urlUpload.sizePolicy().hasHeightForWidth())
        self.afc_pushButton_urlUpload.setSizePolicy(sizePolicy)
        self.afc_pushButton_urlUpload.setMinimumSize(QtCore.QSize(0, 0))
        self.afc_pushButton_urlUpload.setMaximumSize(QtCore.QSize(16777215, 57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.afc_pushButton_urlUpload.setFont(font)
        self.afc_pushButton_urlUpload.setObjectName("afc_pushButton_urlUpload")
        self.afc_horizontalLayout_top.addWidget(self.afc_pushButton_urlUpload)
        self.afc_pushButton_startExt = QtWidgets.QPushButton(self.tab_afc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_pushButton_startExt.sizePolicy().hasHeightForWidth())
        self.afc_pushButton_startExt.setSizePolicy(sizePolicy)
        self.afc_pushButton_startExt.setMinimumSize(QtCore.QSize(0, 0))
        self.afc_pushButton_startExt.setMaximumSize(QtCore.QSize(16777215, 57))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.afc_pushButton_startExt.setFont(font)
        self.afc_pushButton_startExt.setObjectName("afc_pushButton_startExt")
        self.afc_horizontalLayout_top.addWidget(self.afc_pushButton_startExt)
        self.afc_pushButton_mdDown = QtWidgets.QPushButton(self.tab_afc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_pushButton_mdDown.sizePolicy().hasHeightForWidth())
        self.afc_pushButton_mdDown.setSizePolicy(sizePolicy)
        self.afc_pushButton_mdDown.setMinimumSize(QtCore.QSize(0, 0))
        self.afc_pushButton_mdDown.setMaximumSize(QtCore.QSize(16777215, 57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.afc_pushButton_mdDown.setFont(font)
        self.afc_pushButton_mdDown.setObjectName("afc_pushButton_mdDown")
        self.afc_pushButton_mdDown.setVisible(True)
        self.afc_horizontalLayout_top.addWidget(self.afc_pushButton_mdDown)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.afc_horizontalLayout_top.addItem(spacerItem3)
        self.afc_tableWidget_classList = QtWidgets.QTableWidget(self.tab_afc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_tableWidget_classList.sizePolicy().hasHeightForWidth())
        self.afc_tableWidget_classList.setSizePolicy(sizePolicy)
        self.afc_tableWidget_classList.setMinimumSize(QtCore.QSize(625,80))
        self.afc_tableWidget_classList.setMaximumSize(QtCore.QSize(16777215, 80))
        self.afc_tableWidget_classList.setSizeIncrement(QtCore.QSize(0, 80))
        self.afc_tableWidget_classList.setObjectName("afc_tableWidget_classList")

        self.afc_tableWidget_classList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.afc_tableWidget_classList.setColumnCount(10)
        self.afc_tableWidget_classList.setRowCount(1)
        self.afc_tableWidget_classList.horizontalHeader().hide()
        self.afc_tableWidget_classList.verticalHeader().hide()
        self.afc_tableWidget_classList.setShowGrid(False)
        self.afc_tableWidget_classList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.afc_horizontalLayout_top.addWidget(self.afc_tableWidget_classList)
        self.afc_verticalLayout_top.addLayout(self.afc_horizontalLayout_top)
        self.verticalLayout_5.addLayout(self.afc_verticalLayout_top)
        self.afc_splitter_Md = QtWidgets.QSplitter(self.tab_afc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_splitter_Md.sizePolicy().hasHeightForWidth())
        self.afc_splitter_Md.setSizePolicy(sizePolicy)
        self.afc_splitter_Md.setOrientation(QtCore.Qt.Horizontal)
        self.afc_splitter_Md.setChildrenCollapsible(False)
        self.afc_splitter_Md.setObjectName("afc_splitter_Md")
        self.afc_widget_before_Md = QtWidgets.QWidget(self.afc_splitter_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_widget_before_Md.sizePolicy().hasHeightForWidth())
        self.afc_widget_before_Md.setSizePolicy(sizePolicy)
        self.afc_widget_before_Md.setStyleSheet("border: 1px solid gray;")
        self.afc_widget_before_Md.setObjectName("afc_widget_before_Md")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.afc_widget_before_Md)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.afc_label_before_Md = QtWidgets.QLabel(self.afc_widget_before_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_label_before_Md.sizePolicy().hasHeightForWidth())
        self.afc_label_before_Md.setSizePolicy(sizePolicy)
        self.afc_label_before_Md.setMinimumSize(QtCore.QSize(628, 450))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.afc_label_before_Md.setFont(font)
        self.afc_label_before_Md.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.afc_label_before_Md.setStyleSheet("border: 1px solid gray; background-color: QColor(25,25,25)")
        self.afc_label_before_Md.setAlignment(QtCore.Qt.AlignCenter)
        self.afc_label_before_Md.setObjectName("afc_label_before_Md")
        self.verticalLayout.addWidget(self.afc_label_before_Md)
        self.afc_horizontalLayout_mid1 = QtWidgets.QHBoxLayout()
        self.afc_horizontalLayout_mid1.setObjectName("afc_horizontalLayout_mid1")
        self.afc_horizontalLayout_mid2 = QtWidgets.QHBoxLayout()
        self.afc_horizontalLayout_mid2.setObjectName("afc_horizontalLayout_mid2")
        self.afc_pushButton_play = QtWidgets.QPushButton(self.afc_widget_before_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_pushButton_play.sizePolicy().hasHeightForWidth())
        self.afc_pushButton_play.setSizePolicy(sizePolicy)
        self.afc_pushButton_play.setText("")
        self.afc_pushButton_play.setIcon(icon)
        self.afc_pushButton_play.setIconSize(QtCore.QSize(32, 32))
        self.afc_pushButton_play.setObjectName("afc_pushButton_play")
        self.afc_horizontalLayout_mid2.addWidget(self.afc_pushButton_play)
        self.afc_pushButton_pause = QtWidgets.QPushButton(self.afc_widget_before_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_pushButton_pause.sizePolicy().hasHeightForWidth())
        self.afc_pushButton_pause.setSizePolicy(sizePolicy)
        self.afc_pushButton_pause.setText("")
        self.afc_pushButton_pause.setIcon(icon1)
        self.afc_pushButton_pause.setIconSize(QtCore.QSize(32, 32))
        self.afc_pushButton_pause.setObjectName("afc_pushButton_pause")
        self.afc_horizontalLayout_mid2.addWidget(self.afc_pushButton_pause)
        self.afc_pushButton_stop = QtWidgets.QPushButton(self.afc_widget_before_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_pushButton_stop.sizePolicy().hasHeightForWidth())
        self.afc_pushButton_stop.setSizePolicy(sizePolicy)
        self.afc_pushButton_stop.setText("")
        self.afc_pushButton_stop.setIcon(icon2)
        self.afc_pushButton_stop.setIconSize(QtCore.QSize(32, 32))
        self.afc_pushButton_stop.setObjectName("afc_pushButton_stop")
        self.afc_horizontalLayout_mid2.addWidget(self.afc_pushButton_stop)
        self.afc_horizontalLayout_mid1.addLayout(self.afc_horizontalLayout_mid2)
        spacerItem4 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Minimum)
        self.afc_horizontalLayout_mid1.addItem(spacerItem4)
        self.afc_horizontalSlider = QtWidgets.QSlider(self.tab_afc)
        self.afc_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.afc_horizontalSlider.setObjectName("afc_horizontalSlider")

        # 슬라이드바 hidden 처리
        self.afc_horizontalSlider.setVisible(True)
        self.afc_horizontalLayout_mid1.addWidget(self.afc_horizontalSlider)
        spacerItem5 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Minimum)
        self.afc_horizontalLayout_mid1.addItem(spacerItem5)
        self.afc_before_time = QtWidgets.QLabel(self.afc_widget_before_Md)
        self.afc_before_time.setObjectName("afc_before_time")
        self.afc_horizontalLayout_mid1.addWidget(self.afc_before_time)
        # self.verticalLayout.addLayout(self.afc_horizontalLayout_mid1)
        self.afc_widget_after_Md = QtWidgets.QWidget(self.afc_splitter_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_widget_after_Md.sizePolicy().hasHeightForWidth())
        self.afc_widget_after_Md.setSizePolicy(sizePolicy)
        self.afc_widget_after_Md.setStyleSheet("border: 1px solid gray; background-color: QColor(25,25,25)")
        self.afc_widget_after_Md.setObjectName("afc_widget_after_Md")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.afc_widget_after_Md)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.afc_label_after_Md = QtWidgets.QLabel(self.afc_widget_after_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afc_label_after_Md.sizePolicy().hasHeightForWidth())
        self.afc_label_after_Md.setSizePolicy(sizePolicy)
        self.afc_label_after_Md.setMinimumSize(QtCore.QSize(628, 450))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.afc_label_after_Md.setFont(font)
        self.afc_label_after_Md.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.afc_label_after_Md.setStyleSheet("border: 1px solid gray;")
        self.afc_label_after_Md.setAlignment(QtCore.Qt.AlignCenter)
        self.afc_label_after_Md.setObjectName("afc_label_after_Md")
        self.verticalLayout_2.addWidget(self.afc_label_after_Md)

        ###########
        # 이전버전 ui 소스
        ###########
        # self.afc_horizontalLayout_mid1_2 = QtWidgets.QHBoxLayout()
        # self.afc_horizontalLayout_mid1_2.setSpacing(0)
        # self.afc_horizontalLayout_mid1_2.setObjectName("afc_horizontalLayout_mid1_2")
        # self.afc_horizontalLayout_mid2_2 = QtWidgets.QHBoxLayout()
        # self.afc_horizontalLayout_mid2_2.setObjectName("afc_horizontalLayout_mid2_2")
        # self.afc_pushButton_play_2 = QtWidgets.QPushButton(self.afc_widget_after_Md)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.afc_pushButton_play_2.sizePolicy().hasHeightForWidth())
        # self.afc_pushButton_play_2.setSizePolicy(sizePolicy)
        # self.afc_pushButton_play_2.setText("")
        # self.afc_pushButton_play_2.setIcon(icon)
        # self.afc_pushButton_play_2.setIconSize(QtCore.QSize(32, 32))
        # self.afc_pushButton_play_2.setObjectName("afc_pushButton_play_2")
        # self.afc_horizontalLayout_mid2_2.addWidget(self.afc_pushButton_play_2)
        # self.afc_pushButton_pause_2 = QtWidgets.QPushButton(self.afc_widget_after_Md)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.afc_pushButton_pause_2.sizePolicy().hasHeightForWidth())
        # self.afc_pushButton_pause_2.setSizePolicy(sizePolicy)
        # self.afc_pushButton_pause_2.setText("")
        # self.afc_pushButton_pause_2.setIcon(icon1)
        # self.afc_pushButton_pause_2.setIconSize(QtCore.QSize(32, 32))
        # self.afc_pushButton_pause_2.setObjectName("afc_pushButton_pause_2")
        # self.afc_horizontalLayout_mid2_2.addWidget(self.afc_pushButton_pause_2)
        # self.afc_pushButton_stop_2 = QtWidgets.QPushButton(self.afc_widget_after_Md)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.afc_pushButton_stop_2.sizePolicy().hasHeightForWidth())
        # self.afc_pushButton_stop_2.setSizePolicy(sizePolicy)
        # self.afc_pushButton_stop_2.setText("")
        # self.afc_pushButton_stop_2.setIcon(icon2)
        # self.afc_pushButton_stop_2.setIconSize(QtCore.QSize(32, 32))
        # self.afc_pushButton_stop_2.setObjectName("afc_pushButton_stop_2")
        # self.afc_horizontalLayout_mid2_2.addWidget(self.afc_pushButton_stop_2)
        # self.afc_horizontalLayout_mid1_2.addLayout(self.afc_horizontalLayout_mid2_2)
        # spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.afc_horizontalLayout_mid1_2.addItem(spacerItem5)
        # self.afc_after_time = QtWidgets.QLabel(self.afc_widget_after_Md)
        # self.afc_after_time.setObjectName("afc_after_time")
        # self.afc_horizontalLayout_mid1_2.addWidget(self.afc_after_time)
        # self.verticalLayout_2.addLayout(self.afc_horizontalLayout_mid1_2)
        self.verticalLayout_5.addWidget(self.afc_splitter_Md)
        self.verticalLayout_5.addLayout(self.afc_horizontalLayout_mid1)
        self.mainTabWidget.addTab(self.tab_afc, "오토포커싱")

        ########
        # alrTab Default
        # - 수동학습 탭
        #######

        self.tab_alr = QtWidgets.QWidget()
        self.tab_alr.setObjectName("tab_alr")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_alr)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.alr_horizontalLayout_top = QtWidgets.QHBoxLayout()
        self.alr_horizontalLayout_top.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.alr_horizontalLayout_top.setObjectName("alr_horizontalLayout_top")
        self.alr_pushButton_localUpload = QtWidgets.QPushButton(self.tab_alr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_pushButton_localUpload.sizePolicy().hasHeightForWidth())
        self.alr_pushButton_localUpload.setSizePolicy(sizePolicy)
        self.alr_pushButton_localUpload.setMinimumSize(QtCore.QSize(0,57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.alr_pushButton_localUpload.setFont(font)
        self.alr_pushButton_localUpload.setObjectName("alr_pushButton_localUpload")
        self.alr_horizontalLayout_top.addWidget(self.alr_pushButton_localUpload)
        self.alr_pushButton_extImage = QtWidgets.QPushButton(self.tab_alr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_pushButton_extImage.sizePolicy().hasHeightForWidth())
        self.alr_pushButton_extImage.setSizePolicy(sizePolicy)
        self.alr_pushButton_extImage.setMinimumSize(QtCore.QSize(0,57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.alr_pushButton_extImage.setFont(font)
        self.alr_pushButton_extImage.setObjectName("alr_pushButton_extImage")
        self.alr_horizontalLayout_top.addWidget(self.alr_pushButton_extImage)
        self.alr_pushButton_openFolder = QtWidgets.QPushButton(self.tab_alr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_pushButton_openFolder.sizePolicy().hasHeightForWidth())
        self.alr_pushButton_openFolder.setSizePolicy(sizePolicy)
        self.alr_pushButton_openFolder.setMaximumSize(QtCore.QSize(16777215,57))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.alr_pushButton_openFolder.setFont(font)
        self.alr_pushButton_openFolder.setObjectName("alr_pushButton_openFolder")
        self.alr_horizontalLayout_top.addWidget(self.alr_pushButton_openFolder)
        self.alr_pushButton_startLearning = QtWidgets.QPushButton(self.tab_alr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_pushButton_startLearning.sizePolicy().hasHeightForWidth())
        self.alr_pushButton_startLearning.setSizePolicy(sizePolicy)
        self.alr_pushButton_startLearning.setMinimumSize(QtCore.QSize(0,57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.alr_pushButton_startLearning.setFont(font)
        self.alr_pushButton_startLearning.setObjectName("alr_pushButton_startLearning")
        self.alr_horizontalLayout_top.addWidget(self.alr_pushButton_startLearning)
        spacerItem6 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.alr_horizontalLayout_top.addItem(spacerItem6)
        self.alr_tableWidget_classList = QtWidgets.QTableWidget(self.tab_alr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_tableWidget_classList.sizePolicy().hasHeightForWidth())
        self.alr_tableWidget_classList.setSizePolicy(sizePolicy)
        self.alr_tableWidget_classList.setMinimumSize(QtCore.QSize(640,0))
        self.alr_tableWidget_classList.setMaximumSize(QtCore.QSize(16777215,80))
        self.alr_tableWidget_classList.setObjectName("alr_tableWidget_classList")

        self.alr_tableWidget_classList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.alr_tableWidget_classList.setColumnCount(10)
        self.alr_tableWidget_classList.setRowCount(1)
        self.alr_tableWidget_classList.horizontalHeader().hide()
        self.alr_tableWidget_classList.verticalHeader().hide()
        self.alr_tableWidget_classList.setShowGrid(False)
        self.alr_tableWidget_classList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.alr_horizontalLayout_top.addWidget(self.alr_tableWidget_classList)
        self.verticalLayout_15.addLayout(self.alr_horizontalLayout_top)
        self.alr_widget_video_Md = QtWidgets.QWidget(self.tab_alr)
        self.alr_widget_video_Md.setObjectName("alr_widget_video_Md")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.alr_widget_video_Md)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setContentsMargins(0,0,0,0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.alr_label_extMd = QtWidgets.QLabel(self.tab_alr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_label_extMd.sizePolicy().hasHeightForWidth())
        self.alr_label_extMd.setSizePolicy(sizePolicy)
        self.alr_label_extMd.setMinimumSize(QtCore.QSize(1260,669))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.alr_label_extMd.setFont(font)
        self.alr_label_extMd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.alr_label_extMd.setStyleSheet("border: 1px solid gray; background-color: QColor(25,25,25);")
        self.alr_label_extMd.setText("")
        self.alr_label_extMd.setAlignment(QtCore.Qt.AlignCenter)
        self.alr_label_extMd.setObjectName("alr_label_extMd")
        self.verticalLayout_15.addWidget(self.alr_label_extMd)
        # self.verticalLayout_14.addWidget(self.alr_label_extMd)
        self.alr_horizontalLayout_mid1 = QtWidgets.QHBoxLayout()
        self.alr_horizontalLayout_mid1.setObjectName("alr_horizontalLayout_mid1")
        self.alr_horizontalLayout_mid2 = QtWidgets.QHBoxLayout()
        self.alr_horizontalLayout_mid2.setObjectName("alr_horizontalLayout_mid2")
        self.alr_pushButton_play = QtWidgets.QPushButton(self.alr_widget_video_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_pushButton_play.sizePolicy().hasHeightForWidth())
        self.alr_pushButton_play.setSizePolicy(sizePolicy)
        self.alr_pushButton_play.setText("")
        self.alr_pushButton_play.setIcon(icon)
        self.alr_pushButton_play.setIconSize(QtCore.QSize(32,32))
        self.alr_pushButton_play.setObjectName("alr_pushButton_play")
        self.alr_horizontalLayout_mid2.addWidget(self.alr_pushButton_play)
        self.alr_pushButton_pause = QtWidgets.QPushButton(self.alr_widget_video_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_pushButton_pause.sizePolicy().hasHeightForWidth())
        self.alr_pushButton_pause.setSizePolicy(sizePolicy)
        self.alr_pushButton_pause.setText("")
        self.alr_pushButton_pause.setIcon(icon1)
        self.alr_pushButton_pause.setIconSize(QtCore.QSize(32,32))
        self.alr_pushButton_pause.setObjectName("alr_pushButton_pause")
        self.alr_horizontalLayout_mid2.addWidget(self.alr_pushButton_pause)
        self.alr_pushButton_stop = QtWidgets.QPushButton(self.alr_widget_video_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_pushButton_stop.sizePolicy().hasHeightForWidth())
        self.alr_pushButton_stop.setSizePolicy(sizePolicy)
        self.alr_pushButton_stop.setText("")
        self.alr_pushButton_stop.setIcon(icon2)
        self.alr_pushButton_stop.setIconSize(QtCore.QSize(32,32))
        self.alr_pushButton_stop.setObjectName("alr_pushButton_stop")
        self.alr_horizontalLayout_mid2.addWidget(self.alr_pushButton_stop)
        self.alr_horizontalLayout_mid1.addLayout(self.alr_horizontalLayout_mid2)
        spacerItem7 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.alr_horizontalLayout_mid1.addItem(spacerItem7)
        self.alr_video_time = QtWidgets.QLabel(self.alr_widget_video_Md)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alr_video_time.sizePolicy().hasHeightForWidth())
        self.alr_video_time.setSizePolicy(sizePolicy)
        self.alr_video_time.setTextFormat(QtCore.Qt.AutoText)
        self.alr_video_time.setScaledContents(False)
        self.alr_video_time.setMargin(0)
        self.alr_video_time.setObjectName("alr_video_time")
        self.alr_horizontalLayout_mid1.addWidget(self.alr_video_time)
        self.verticalLayout_14.addLayout(self.alr_horizontalLayout_mid1)
        self.verticalLayout_15.addWidget(self.alr_widget_video_Md)
        self.mainTabWidget.addTab(self.tab_alr,"학습")


        ########
        #	optTab Default
        #	- 옵션설정 탭
        ########
        self.tab_opt = QtWidgets.QWidget()
        self.tab_opt.setObjectName("tab_opt")

        ######## 설정.공통옵션설정 start
        ###########
        # 이전버전 ui 소스
        ###########
        # self.opt_groupBox_top = QtWidgets.QGroupBox(self.tab_opt)
        # self.opt_groupBox_top.setGeometry(QtCore.QRect(60, 40, 1161, 171))
        # self.opt_groupBox_top.setObjectName("opt_groupBox_top")
        # self.layoutWidget = QtWidgets.QWidget(self.opt_groupBox_top)
        # self.layoutWidget.setGeometry(QtCore.QRect(130, 110, 204, 24))
        # self.layoutWidget.setObjectName("layoutWidget")
        # self.opt_horizontalLayout3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        # self.opt_horizontalLayout3.setContentsMargins(0, 0, 0, 0)
        # self.opt_horizontalLayout3.setObjectName("opt_horizontalLayout3")
        # self.opt_label_saveFmt = QtWidgets.QLabel(self.layoutWidget)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.opt_label_saveFmt.setFont(font)
        # self.opt_label_saveFmt.setScaledContents(False)
        # self.opt_label_saveFmt.setAlignment(QtCore.Qt.AlignCenter)
        # self.opt_label_saveFmt.setWordWrap(True)
        # self.opt_label_saveFmt.setObjectName("opt_label_saveFmt")
        # self.opt_horizontalLayout3.addWidget(self.opt_label_saveFmt)
        # self.opt_comboBox_downFileFmt = QtWidgets.QComboBox(self.layoutWidget)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # self.opt_comboBox_downFileFmt.setFont(font)
        # self.opt_comboBox_downFileFmt.setEditable(False)
        # self.opt_comboBox_downFileFmt.setCurrentText("확장자 선택")
        # self.opt_comboBox_downFileFmt.setModelColumn(0)
        # self.opt_comboBox_downFileFmt.setObjectName("opt_comboBox_downFileFmt")
        # self.opt_comboBox_downFileFmt.addItem("")
        # self.opt_comboBox_downFileFmt.addItem("")
        # self.opt_horizontalLayout3.addWidget(self.opt_comboBox_downFileFmt)
        # self.layoutWidget1 = QtWidgets.QWidget(self.opt_groupBox_top)
        # self.layoutWidget1.setGeometry(QtCore.QRect(750, 110, 239, 24))
        # self.layoutWidget1.setObjectName("layoutWidget1")
        # self.opt_horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        # self.opt_horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        # self.opt_horizontalLayout_5.setObjectName("opt_horizontalLayout_5")
        # self.opt_label_coordFmt = QtWidgets.QLabel(self.layoutWidget1)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.opt_label_coordFmt.setFont(font)
        # self.opt_label_coordFmt.setScaledContents(False)
        # self.opt_label_coordFmt.setAlignment(QtCore.Qt.AlignCenter)
        # self.opt_label_coordFmt.setWordWrap(True)
        # self.opt_label_coordFmt.setObjectName("opt_label_coordFmt")
        # self.opt_horizontalLayout_5.addWidget(self.opt_label_coordFmt)
        # self.opt_comboBox_coordFmt = QtWidgets.QComboBox(self.layoutWidget1)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # self.opt_comboBox_coordFmt.setFont(font)
        # self.opt_comboBox_coordFmt.setCurrentText("확장자 선택")
        # self.opt_comboBox_coordFmt.setObjectName("opt_comboBox_coordFmt")
        # self.opt_comboBox_coordFmt.addItem("")
        # self.opt_horizontalLayout_5.addWidget(self.opt_comboBox_coordFmt)
        # self.layoutWidget2 = QtWidgets.QWidget(self.opt_groupBox_top)
        # self.layoutWidget2.setGeometry(QtCore.QRect(440, 110, 213, 24))
        # self.layoutWidget2.setObjectName("layoutWidget2")
        # self.opt_horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        # self.opt_horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        # self.opt_horizontalLayout_4.setObjectName("opt_horizontalLayout_4")
        # self.opt_label_saveMdQual = QtWidgets.QLabel(self.layoutWidget2)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.opt_label_saveMdQual.setFont(font)
        # self.opt_label_saveMdQual.setScaledContents(False)
        # self.opt_label_saveMdQual.setAlignment(QtCore.Qt.AlignCenter)
        # self.opt_label_saveMdQual.setWordWrap(True)
        # self.opt_label_saveMdQual.setObjectName("opt_label_saveMdQual")
        # self.opt_horizontalLayout_4.addWidget(self.opt_label_saveMdQual)
        # self.opt_comboBox_downFileDef = QtWidgets.QComboBox(self.layoutWidget2)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # self.opt_comboBox_downFileDef.setFont(font)
        # self.opt_comboBox_downFileDef.setCurrentText("화질 선택")
        # self.opt_comboBox_downFileDef.setObjectName("opt_comboBox_downFileDef")
        # self.opt_comboBox_downFileDef.addItem("")
        # self.opt_horizontalLayout_4.addWidget(self.opt_comboBox_downFileDef)
        # self.layoutWidget3 = QtWidgets.QWidget(self.opt_groupBox_top)
        # self.layoutWidget3.setGeometry(QtCore.QRect(100, 50, 413, 30))
        # self.layoutWidget3.setObjectName("layoutWidget3")
        # self.opt_horizontalLayout_1 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        # self.opt_horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        # self.opt_horizontalLayout_1.setObjectName("opt_horizontalLayout_1")
        # self.opt_label_urlSaveDir = QtWidgets.QLabel(self.layoutWidget3)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.opt_label_urlSaveDir.setFont(font)
        # self.opt_label_urlSaveDir.setScaledContents(False)
        # self.opt_label_urlSaveDir.setAlignment(QtCore.Qt.AlignCenter)
        # self.opt_label_urlSaveDir.setWordWrap(True)
        # self.opt_label_urlSaveDir.setObjectName("opt_label_urlSaveDir")
        # self.opt_horizontalLayout_1.addWidget(self.opt_label_urlSaveDir)
        # self.opt_lineEdit_urlSaveDir = QtWidgets.QLineEdit(self.layoutWidget3)
        # self.opt_lineEdit_urlSaveDir.setEnabled(True)
        # self.opt_lineEdit_urlSaveDir.setObjectName("opt_lineEdit_urlSaveDir")
        # self.opt_horizontalLayout_1.addWidget(self.opt_lineEdit_urlSaveDir)
        # self.opt_pushButton_urlDownDir = QtWidgets.QPushButton(self.layoutWidget3)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # self.opt_pushButton_urlDownDir.setFont(font)
        # self.opt_pushButton_urlDownDir.setObjectName("opt_pushButton_urlDownDir")
        # self.opt_horizontalLayout_1.addWidget(self.opt_pushButton_urlDownDir)
        # self.layoutWidget4 = QtWidgets.QWidget(self.opt_groupBox_top)
        # self.layoutWidget4.setGeometry(QtCore.QRect(610, 50, 399, 30))
        # self.layoutWidget4.setObjectName("layoutWidget4")
        # self.opt_horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        # self.opt_horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.opt_horizontalLayout_2.setObjectName("opt_horizontalLayout_2")
        # self.opt_label_localSaveDir = QtWidgets.QLabel(self.layoutWidget4)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.opt_label_localSaveDir.setFont(font)
        # self.opt_label_localSaveDir.setScaledContents(False)
        # self.opt_label_localSaveDir.setAlignment(QtCore.Qt.AlignCenter)
        # self.opt_label_localSaveDir.setWordWrap(True)
        # self.opt_label_localSaveDir.setObjectName("opt_label_localSaveDir")
        # self.opt_horizontalLayout_2.addWidget(self.opt_label_localSaveDir)
        # self.opt_lineEdit_saveDir = QtWidgets.QLineEdit(self.layoutWidget4)
        # self.opt_lineEdit_saveDir.setObjectName("opt_lineEdit_saveDir")
        # self.opt_horizontalLayout_2.addWidget(self.opt_lineEdit_saveDir)
        # self.opt_pushButton_saveDir = QtWidgets.QPushButton(self.layoutWidget4)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # self.opt_pushButton_saveDir.setFont(font)
        # self.opt_pushButton_saveDir.setObjectName("opt_pushButton_saveDir")
        # self.opt_horizontalLayout_2.addWidget(self.opt_pushButton_saveDir)
        self.opt_groupBox_top = QtWidgets.QGroupBox(self.tab_opt)
        self.opt_groupBox_top.setGeometry(QtCore.QRect(60,40,1161,171))
        self.opt_groupBox_top.setObjectName("opt_groupBox_top")
        self.layoutWidget = QtWidgets.QWidget(self.opt_groupBox_top)
        self.layoutWidget.setGeometry(QtCore.QRect(90,50,413,30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.opt_horizontalLayout_1 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.opt_horizontalLayout_1.setContentsMargins(0,0,0,0)
        self.opt_horizontalLayout_1.setObjectName("opt_horizontalLayout_1")
        self.opt_label_urlSaveDir = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_urlSaveDir.setFont(font)
        self.opt_label_urlSaveDir.setScaledContents(False)
        self.opt_label_urlSaveDir.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_urlSaveDir.setWordWrap(True)
        self.opt_label_urlSaveDir.setObjectName("opt_label_urlSaveDir")
        self.opt_horizontalLayout_1.addWidget(self.opt_label_urlSaveDir)
        self.opt_lineEdit_urlSaveDir = QtWidgets.QLineEdit(self.layoutWidget)
        self.opt_lineEdit_urlSaveDir.setEnabled(True)
        self.opt_lineEdit_urlSaveDir.setObjectName("opt_lineEdit_urlSaveDir")
        self.opt_horizontalLayout_1.addWidget(self.opt_lineEdit_urlSaveDir)
        self.opt_pushButton_urlDownDir = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.opt_pushButton_urlDownDir.setFont(font)
        self.opt_pushButton_urlDownDir.setObjectName("opt_pushButton_urlDownDir")
        self.opt_horizontalLayout_1.addWidget(self.opt_pushButton_urlDownDir)
        self.layoutWidget1 = QtWidgets.QWidget(self.opt_groupBox_top)
        self.layoutWidget1.setGeometry(QtCore.QRect(650,50,441,31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.opt_horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.opt_horizontalLayout_2.setContentsMargins(0,0,0,0)
        self.opt_horizontalLayout_2.setObjectName("opt_horizontalLayout_2")
        self.opt_label_localSaveDir = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_localSaveDir.setFont(font)
        self.opt_label_localSaveDir.setScaledContents(False)
        self.opt_label_localSaveDir.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_localSaveDir.setWordWrap(True)
        self.opt_label_localSaveDir.setObjectName("opt_label_localSaveDir")
        self.opt_horizontalLayout_2.addWidget(self.opt_label_localSaveDir)
        self.opt_lineEdit_saveDir = QtWidgets.QLineEdit(self.layoutWidget1)
        self.opt_lineEdit_saveDir.setObjectName("opt_lineEdit_saveDir")
        self.opt_horizontalLayout_2.addWidget(self.opt_lineEdit_saveDir)
        self.opt_pushButton_saveDir = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.opt_pushButton_saveDir.setFont(font)
        self.opt_pushButton_saveDir.setObjectName("opt_pushButton_saveDir")
        self.opt_horizontalLayout_2.addWidget(self.opt_pushButton_saveDir)
        self.widget = QtWidgets.QWidget(self.opt_groupBox_top)
        self.widget.setGeometry(QtCore.QRect(90,110,1001,31))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0,0,0,0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.opt_horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.opt_horizontalLayout3.setObjectName("opt_horizontalLayout3")
        self.opt_label_saveFmt = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_saveFmt.setFont(font)
        self.opt_label_saveFmt.setScaledContents(False)
        self.opt_label_saveFmt.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_saveFmt.setWordWrap(True)
        self.opt_label_saveFmt.setObjectName("opt_label_saveFmt")
        self.opt_horizontalLayout3.addWidget(self.opt_label_saveFmt)
        self.opt_comboBox_downFileFmt = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.opt_comboBox_downFileFmt.setFont(font)
        self.opt_comboBox_downFileFmt.setEditable(False)
        self.opt_comboBox_downFileFmt.setCurrentText("확장자 선택")
        self.opt_comboBox_downFileFmt.setModelColumn(0)
        self.opt_comboBox_downFileFmt.setObjectName("opt_comboBox_downFileFmt")
        self.opt_comboBox_downFileFmt.addItem("")
        self.opt_comboBox_downFileFmt.addItem("")
        self.opt_horizontalLayout3.addWidget(self.opt_comboBox_downFileFmt)
        self.horizontalLayout_2.addLayout(self.opt_horizontalLayout3)
        spacerItem6 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.opt_horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.opt_horizontalLayout_4.setObjectName("opt_horizontalLayout_4")
        self.opt_label_saveMdQual = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_saveMdQual.setFont(font)
        self.opt_label_saveMdQual.setScaledContents(False)
        self.opt_label_saveMdQual.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_saveMdQual.setWordWrap(True)
        self.opt_label_saveMdQual.setObjectName("opt_label_saveMdQual")
        self.opt_horizontalLayout_4.addWidget(self.opt_label_saveMdQual)
        self.opt_comboBox_downFileDef = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.opt_comboBox_downFileDef.setFont(font)
        self.opt_comboBox_downFileDef.setCurrentText("화질 선택")
        self.opt_comboBox_downFileDef.setObjectName("opt_comboBox_downFileDef")
        self.opt_comboBox_downFileDef.addItem("")
        self.opt_horizontalLayout_4.addWidget(self.opt_comboBox_downFileDef)
        self.horizontalLayout_2.addLayout(self.opt_horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.opt_horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.opt_horizontalLayout_5.setObjectName("opt_horizontalLayout_5")
        self.opt_label_coordFmt = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_coordFmt.setFont(font)
        self.opt_label_coordFmt.setScaledContents(False)
        self.opt_label_coordFmt.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_coordFmt.setWordWrap(True)
        self.opt_label_coordFmt.setObjectName("opt_label_coordFmt")
        self.opt_horizontalLayout_5.addWidget(self.opt_label_coordFmt)
        self.opt_comboBox_coordFmt = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.opt_comboBox_coordFmt.setFont(font)
        self.opt_comboBox_coordFmt.setCurrentText("확장자 선택")
        self.opt_comboBox_coordFmt.setObjectName("opt_comboBox_coordFmt")
        self.opt_comboBox_coordFmt.addItem("")
        self.opt_horizontalLayout_5.addWidget(self.opt_comboBox_coordFmt)
        self.horizontalLayout_2.addLayout(self.opt_horizontalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(88,32,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.opt_horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.opt_horizontalLayout_9.setObjectName("opt_horizontalLayout_9")
        self.opt_label_bbox = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_bbox.setFont(font)
        self.opt_label_bbox.setScaledContents(False)
        self.opt_label_bbox.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_bbox.setWordWrap(True)
        self.opt_label_bbox.setObjectName("opt_label_bbox")
        self.opt_horizontalLayout_9.addWidget(self.opt_label_bbox)
        self.opt_comboBox_bbox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.opt_comboBox_bbox.setFont(font)
        self.opt_comboBox_bbox.setCurrentText("활성화 선택")
        self.opt_comboBox_bbox.setObjectName("opt_comboBox_coordFmt_3")
        self.opt_comboBox_bbox.addItem("")

        self.opt_horizontalLayout_9.addWidget(self.opt_comboBox_bbox)
        self.horizontalLayout_2.addLayout(self.opt_horizontalLayout_9)
        ######## 설정.공통옵션설정 end

        ######## 설정.영상 검출 옵션 설정 start
        self.opt_groupBox_mid = QtWidgets.QGroupBox(self.tab_opt)
        self.opt_groupBox_mid.setGeometry(QtCore.QRect(60, 235, 1161, 171))
        self.opt_groupBox_mid.setObjectName("opt_groupBox_mid")
        self.opt_groupBox_4 = QtWidgets.QGroupBox(self.opt_groupBox_mid)
        self.opt_groupBox_4.setGeometry(QtCore.QRect(250, 170, 1161, 171))
        self.opt_groupBox_4.setObjectName("opt_groupBox_4")
        self.opt_label_cn1 = QtWidgets.QLabel(self.opt_groupBox_mid)
        self.opt_label_cn1.setGeometry(QtCore.QRect(340, 54, 731, 75))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.opt_label_cn1.setFont(font)
        self.opt_label_cn1.setScaledContents(False)
        self.opt_label_cn1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.opt_label_cn1.setWordWrap(True)
        self.opt_label_cn1.setObjectName("opt_label_cn1")
        self.layoutWidget5 = QtWidgets.QWidget(self.opt_groupBox_mid)
        self.layoutWidget5.setGeometry(QtCore.QRect(50, 80, 238, 24))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.opt_horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.opt_horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.opt_horizontalLayout_6.setObjectName("opt_horizontalLayout_6")
        self.opt_label_extButTm = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_extButTm.setFont(font)
        self.opt_label_extButTm.setScaledContents(False)
        self.opt_label_extButTm.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_extButTm.setWordWrap(True)
        self.opt_label_extButTm.setObjectName("opt_label_extButTm")
        self.opt_horizontalLayout_6.addWidget(self.opt_label_extButTm)
        self.opt_comboBox_bufTime = QtWidgets.QComboBox(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.opt_comboBox_bufTime.setFont(font)
        self.opt_comboBox_bufTime.setCurrentText("5초")
        self.opt_comboBox_bufTime.setObjectName("opt_comboBox_bufTime")
        self.opt_comboBox_bufTime.addItem("")
        self.opt_comboBox_bufTime.addItem("")
        self.opt_comboBox_bufTime.addItem("")
        self.opt_comboBox_bufTime.addItem("")
        self.opt_horizontalLayout_6.addWidget(self.opt_comboBox_bufTime)
        ######## 설정.영상 검출 옵션 설정 end

        ######## 설정.오토 포커싱 옵션 설정 start
        self.opt_groupBox_mid2 = QtWidgets.QGroupBox(self.tab_opt)
        self.opt_groupBox_mid2.setGeometry(QtCore.QRect(60,429,1161,171))
        self.opt_groupBox_mid2.setObjectName("opt_groupBox_mid2")
        self.opt_label_cn2 = QtWidgets.QLabel(self.opt_groupBox_mid2)
        self.opt_label_cn2.setGeometry(QtCore.QRect(50, 120, 591, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.opt_label_cn2.setFont(font)
        self.opt_label_cn2.setScaledContents(False)
        self.opt_label_cn2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.opt_label_cn2.setWordWrap(True)
        self.opt_label_cn2.setObjectName("opt_label_cn2")
        self.layoutWidget6 = QtWidgets.QWidget(self.opt_groupBox_mid2)
        self.layoutWidget6.setGeometry(QtCore.QRect(50, 40, 177, 25))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.opt_horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.opt_horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.opt_horizontalLayout_7.setObjectName("opt_horizontalLayout_7")
        self.opt_label_afcBoxHei = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_afcBoxHei.setFont(font)
        self.opt_label_afcBoxHei.setScaledContents(False)
        self.opt_label_afcBoxHei.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_afcBoxHei.setWordWrap(True)
        self.opt_label_afcBoxHei.setObjectName("opt_label_afcBoxHei")
        self.opt_horizontalLayout_7.addWidget(self.opt_label_afcBoxHei)
        self.opt_spinBox_heightValue = QtWidgets.QSpinBox(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_spinBox_heightValue.setFont(font)
        self.opt_spinBox_heightValue.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_spinBox_heightValue.setMaximum(2000)
        self.opt_spinBox_heightValue.setProperty("value", 600)
        self.opt_spinBox_heightValue.setObjectName("opt_spinBox_heightValue")
        self.opt_horizontalLayout_7.addWidget(self.opt_spinBox_heightValue)
        self.layoutWidget7 = QtWidgets.QWidget(self.opt_groupBox_mid2)
        self.layoutWidget7.setGeometry(QtCore.QRect(50, 80, 177, 25))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.opt_horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.opt_horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.opt_horizontalLayout_8.setObjectName("opt_horizontalLayout_8")
        self.opt_label_afcBoxWid = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_afcBoxWid.setFont(font)
        self.opt_label_afcBoxWid.setScaledContents(False)
        self.opt_label_afcBoxWid.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_afcBoxWid.setWordWrap(True)
        self.opt_label_afcBoxWid.setObjectName("opt_label_afcBoxWid")
        self.opt_horizontalLayout_8.addWidget(self.opt_label_afcBoxWid)
        self.opt_spinBox_widthValue = QtWidgets.QSpinBox(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_spinBox_widthValue.setFont(font)
        self.opt_spinBox_widthValue.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_spinBox_widthValue.setMaximum(2000)
        self.opt_spinBox_widthValue.setProperty("value", 300)
        self.opt_spinBox_widthValue.setObjectName("opt_spinBox_widthValue")
        self.opt_horizontalLayout_8.addWidget(self.opt_spinBox_widthValue)

        ######## 설정.오토 포커싱 옵션 설정 end

        ######## 설정.학습 옵션 설정 start
        self.opt_groupBox_bot = QtWidgets.QGroupBox(self.tab_opt)
        self.opt_groupBox_bot.setGeometry(QtCore.QRect(60,620,1161,171))
        self.opt_groupBox_bot.setObjectName("opt_groupBox_bot")
        self.opt_groupBox_5 = QtWidgets.QGroupBox(self.opt_groupBox_bot)
        self.opt_groupBox_5.setGeometry(QtCore.QRect(250,170,1161,171))
        self.opt_groupBox_5.setObjectName("opt_groupBox_5")
        self.opt_label_cn1_2 = QtWidgets.QLabel(self.opt_groupBox_bot)
        self.opt_label_cn1_2.setGeometry(QtCore.QRect(49,90,731,75))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.opt_label_cn1_2.setFont(font)
        self.opt_label_cn1_2.setScaledContents(False)
        self.opt_label_cn1_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.opt_label_cn1_2.setWordWrap(True)
        self.opt_label_cn1_2.setObjectName("opt_label_cn1_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.opt_groupBox_bot)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40,60,441,31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.opt_horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.opt_horizontalLayout_3.setContentsMargins(0,0,0,0)
        self.opt_horizontalLayout_3.setObjectName("opt_horizontalLayout_3")
        self.opt_label_saveImgDir = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opt_label_saveImgDir.setFont(font)
        self.opt_label_saveImgDir.setScaledContents(False)
        self.opt_label_saveImgDir.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_saveImgDir.setWordWrap(True)
        self.opt_label_saveImgDir.setObjectName("opt_label_saveImgDir")
        self.opt_horizontalLayout_3.addWidget(self.opt_label_saveImgDir)
        self.opt_lineEdit_saveImgDir = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.opt_lineEdit_saveImgDir.setObjectName("opt_lineEdit_saveImgDir")
        self.opt_horizontalLayout_3.addWidget(self.opt_lineEdit_saveImgDir)
        self.opt_pushButton_saveImgDir = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.opt_pushButton_saveImgDir.setFont(font)
        self.opt_pushButton_saveImgDir.setObjectName("opt_pushButton_saveImgDir")
        self.opt_horizontalLayout_3.addWidget(self.opt_pushButton_saveImgDir)
        ######## 설정.학습 옵션 설정 end

        ######## 검출, 오토포커싱 공통 옵션 설정
        # 검출대상리스트 헤더 및 기본 설정 (검출 / 오토포커싱 공통)
        self.comm_tableWidget_classList_tHeader_setting()


        ######## 탭 정보 생성 처리
        self.mainTabWidget.addTab(self.tab_opt, "설정")

        ######## 폼 액션 처리
        self.stackedLayout.addWidget(self.mainTabWidget)
        self.action = QtWidgets.QAction(Form)
        self.action.setObjectName("action")
        self.retranslateUi(Form)
        self.mainTabWidget.setCurrentIndex(0)
        self.opt_comboBox_bufTime.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #####
        # 로딩 이미지 라벨 위젯 셋팅
        self.loadingLabel = QtWidgets.QLabel()
        self.loadingImg = QtGui.QMovie("./icon/ajax-loader.gif")
        # gifImg.setScaledSize(QtCore.QSize(1280, 840))
        self.loadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingLabel.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        self.loadingLabel.setMovie(self.loadingImg)
        self.stackedLayout.addWidget(self.loadingLabel)

        ######## tab key로 인한 이동 순서 설정 start / Form.setTabOrder(A, B) -> Form.setTabOrder(B, C)
        Form.setTabOrder(self.ext_pushButton_localUpload, self.ext_pushButton_mdDown)
        Form.setTabOrder(self.ext_pushButton_mdDown, self.ext_pushButton_allClear)
        Form.setTabOrder(self.ext_pushButton_allClear, self.ext_pushButton_selectDelete)
        # Form.setTabOrder(self.ext_pushButton_selectDelete, self.ext_pushButton_allSave)
        # Form.setTabOrder(self.ext_pushButton_allSave, self.ext_pushButton_selectSave)
        Form.setTabOrder(self.ext_pushButton_selectDelete,self.ext_tableWidget_classList)
        Form.setTabOrder(self.ext_tableWidget_classList, self.opt_lineEdit_urlSaveDir)
        Form.setTabOrder(self.opt_lineEdit_urlSaveDir, self.opt_pushButton_urlDownDir)
        Form.setTabOrder(self.opt_pushButton_urlDownDir, self.opt_lineEdit_saveDir)
        Form.setTabOrder(self.opt_lineEdit_saveDir, self.opt_pushButton_saveDir)
        Form.setTabOrder(self.opt_pushButton_saveDir, self.opt_comboBox_downFileFmt)
        Form.setTabOrder(self.opt_comboBox_downFileFmt, self.opt_comboBox_downFileDef)
        Form.setTabOrder(self.opt_comboBox_downFileDef, self.opt_comboBox_coordFmt)
        Form.setTabOrder(self.opt_comboBox_coordFmt, self.opt_comboBox_bufTime)
        Form.setTabOrder(self.opt_comboBox_bufTime, self.opt_spinBox_heightValue)
        Form.setTabOrder(self.opt_spinBox_heightValue, self.opt_spinBox_widthValue)
        ######## tab key로 인한 이동 순서 설정 end




    def retranslateUi(self, Form):
        """
            # 테이블 데이터 / 버튼명 데이터  label text 데이터 입력 처리부
            # 확인 후 해당 형태로 데이터 입력
         """

        # 메인 stacedLayout index 설정(메인탭 상위)
        self.stackedLayout.setCurrentIndex(1)

        # 어플리케이션 네임
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Human?", None, -1))

        # 영상검출 버튼 및  비디오 제어 라벨 설정
        self.ext_pushButton_localUpload.setText(QtWidgets.QApplication.translate("Form", "로컬 업로드", None, -1))
        self.ext_pushButton_urlUpload.setText(QtWidgets.QApplication.translate("Form", "URL 업로드", None, -1))
        self.ext_pushButton_startExt.setText(QtWidgets.QApplication.translate("Form", "검출 시작", None, -1))
        self.ext_pushButton_mdDown.setText(QtWidgets.QApplication.translate("Form", "영상 내려받기", None, -1))
        self.ext_pushButton_mdDown.setVisible(True)
        # self.ext_label_extMd.setText(QtWidgets.QApplication.translate("Form", "Video Area", None, -1))
        self.ext_video_time.setText(QtWidgets.QApplication.translate("Form", "00:00:00 / 00:00:00", None, -1))
        self.ext_pushButton_allClear.setText(QtWidgets.QApplication.translate("Form", "검출 내역 초기화", None, -1))
        self.ext_pushButton_selectDelete.setText(QtWidgets.QApplication.translate("Form", "검출 내역 선택 삭제", None, -1))
        # self.ext_pushButton_allSave.setText(QtWidgets.QApplication.translate("Form", "전체 내려받기", None, -1))
        # self.ext_pushButton_selectSave.setText(QtWidgets.QApplication.translate("Form", "선택 내려받기", None, -1))

        # 오토 포커싱탭 버튼 및 라벨 설정
        self.afc_pushButton_localUpload.setText(QtWidgets.QApplication.translate("Form", "로컬 업로드", None, -1))
        self.afc_pushButton_urlUpload.setText(QtWidgets.QApplication.translate("Form", "URL 업로드", None, -1))
        self.afc_pushButton_startExt.setText(QtWidgets.QApplication.translate("Form", "검출 시작", None, -1))
        self.afc_pushButton_mdDown.setText(QtWidgets.QApplication.translate("Form", "영상 내려받기", None, -1))
        # self.afc_label_before_Md.setText(QtWidgets.QApplication.translate("Form", "Video Area", None, -1))
        self.afc_before_time.setText(QtWidgets.QApplication.translate("Form", "00:00:00 / 00:00:00", None, -1))
        # self.afc_label_after_Md.setText(QtWidgets.QApplication.translate("Form", "Video Area", None, -1))
        # self.afc_after_time.setText(QtWidgets.QApplication.translate("Form", "00:00:00 / 00:00:00", None, -1))

        # 수동학습 탭 버튼 및 라벨 설정
        self.alr_pushButton_localUpload.setText(QtWidgets.QApplication.translate("Form","로컬 업로드",None,-1))
        self.alr_pushButton_extImage.setText(QtWidgets.QApplication.translate("Form","이미지 추출",None,-1))
        self.alr_pushButton_openFolder.setText(QtWidgets.QApplication.translate("Form","폴더 열기",None,-1))
        self.alr_pushButton_startLearning.setText(QtWidgets.QApplication.translate("Form","학습 시작",None,-1))
        self.alr_video_time.setText(QtWidgets.QApplication.translate("Form","00:00:00 / 00:00:00",None,-1))

        # 설정탭 버튼 및 라벨
        self.opt_groupBox_top.setTitle(QtWidgets.QApplication.translate("Form", "공통 옵션 설정", None, -1))
        self.opt_label_saveFmt.setText(QtWidgets.QApplication.translate("Form", "내려받기 확장자", None, -1))
        self.opt_comboBox_downFileFmt.setItemText(0, QtWidgets.QApplication.translate("Form", "확장자 선택", None, -1))
        self.opt_comboBox_downFileFmt.setItemText(1, QtWidgets.QApplication.translate("Form", "mp4", None, -1))
        self.opt_label_coordFmt.setText(QtWidgets.QApplication.translate("Form", "좌표파일 확장자 선택", None, -1))
        self.opt_comboBox_coordFmt.setItemText(0, QtWidgets.QApplication.translate("Form", "확장자 선택", None, -1))
        self.opt_label_saveMdQual.setText(QtWidgets.QApplication.translate("Form", "내려받기 화질 선택", None, -1))
        self.opt_comboBox_downFileDef.setItemText(0, QtWidgets.QApplication.translate("Form", "화질 선택", None, -1))
        self.opt_label_urlSaveDir.setText(QtWidgets.QApplication.translate("Form", "URL 저장 파일 경로", None, -1))
        self.opt_pushButton_urlDownDir.setText(QtWidgets.QApplication.translate("Form", "폴더찾기", None, -1))
        self.opt_label_localSaveDir.setText(QtWidgets.QApplication.translate("Form", "내려받기 저장 경로", None, -1))
        self.opt_pushButton_saveDir.setText(QtWidgets.QApplication.translate("Form", "폴더찾기", None, -1))
        self.opt_groupBox_mid.setTitle(QtWidgets.QApplication.translate("Form", "영상 검출 옵션 설정", None, -1))
        self.opt_groupBox_4.setTitle(QtWidgets.QApplication.translate("Form", "GroupBox", None, -1))
        self.opt_label_bbox.setText(QtWidgets.QApplication.translate("Form","BBOX",None,-1))
        self.opt_comboBox_bbox.setItemText(1,QtWidgets.QApplication.translate("Form","On",None,-1))
        self.opt_comboBox_bbox.setItemText(1,QtWidgets.QApplication.translate("Form","Off",None,-1))
        self.opt_comboBox_bbox.setItemText(0,QtWidgets.QApplication.translate("Form","활성화 선택",None,-1))
        self.opt_label_cn1.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">※ 검출 내역 한 건당 설정 할 수 있는 버퍼의 범위는 00:01 ~ 00:05 초 사이로 설정 할 수 있습니다.</span></p></body></html>", None, -1))
        self.opt_label_extButTm.setText(QtWidgets.QApplication.translate("Form", "추출 영상 버퍼 시간", None, -1))
        self.opt_comboBox_bufTime.setItemText(0, QtWidgets.QApplication.translate("Form", "버퍼(초)선택", None, -1))
        self.opt_comboBox_bufTime.setItemText(1, QtWidgets.QApplication.translate("Form", "1초", None, -1))
        self.opt_comboBox_bufTime.setItemText(2, QtWidgets.QApplication.translate("Form", "3초", None, -1))
        self.opt_comboBox_bufTime.setItemText(3, QtWidgets.QApplication.translate("Form", "5초", None, -1))
        self.opt_groupBox_mid2.setTitle(QtWidgets.QApplication.translate("Form","오토 포커싱 옵션 설정",None,-1))
        self.opt_label_cn2.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">※ 포커싱 박스의 넓이 및 높이는 포커싱 영상의 해상도 보다 클 수 없습니다.</span></p></body></html>", None, -1))
        self.opt_label_afcBoxHei.setText(QtWidgets.QApplication.translate("Form", "포커싱 박스 높이", None, -1))
        self.opt_label_afcBoxWid.setText(QtWidgets.QApplication.translate("Form", "포커싱 박스 넓이", None, -1))
        self.opt_groupBox_bot.setTitle(QtWidgets.QApplication.translate("Form","학습 옵션 설정",None,-1))
        self.opt_groupBox_5.setTitle(QtWidgets.QApplication.translate("Form","GroupBox",None,-1))
        self.opt_label_cn1_2.setText(QtWidgets.QApplication.translate("Form",
                                                                      "<html><head/><body><p><span style=\" color:#ff0000;\">※ 새롭게 학습될 인물의 이미지가 저장될 경로입니다.</span></p></body></html>",
                                                                      None,-1))
        self.opt_label_saveImgDir.setText(QtWidgets.QApplication.translate("Form","이미지 저장 경로",None,-1))
        self.opt_pushButton_saveImgDir.setText(QtWidgets.QApplication.translate("Form","폴더찾기",None,-1))
        self.action.setText(QtWidgets.QApplication.translate("Form", "테스트", None, -1))
        self.action.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>툴팁화면</p></body></html>", None, -1))

        # self.opt_lineEdit_urlSaveDir.setEnabled(False)
        # self.opt_lineEdit_saveDir.setEnabled(False)
        # self.opt_lineEdit_urlSaveDir.setText("Input Path Add")
        # self.opt_lineEdit_saveDir.setText("Input Path Add")

        ## 설정탭 콤보박스 및 디폴트 데이터 셋팅
        self.opt_lineEdit_urlSaveDir.setEnabled(True)
        self.opt_lineEdit_saveDir.setEnabled(True)
        self.opt_lineEdit_saveDir.setEnabled(True)
        self.opt_lineEdit_urlSaveDir.setText("업로드 경로")
        self.opt_lineEdit_saveDir.setText("업로드 경로")
        self.opt_lineEdit_saveImgDir.setReadOnly(True)
        self.opt_lineEdit_urlSaveDir.setReadOnly(True)
        self.opt_lineEdit_saveDir.setReadOnly(True)
        self.opt_lineEdit_urlSaveDir.setStyleSheet("font:12pt")
        self.opt_lineEdit_saveDir.setStyleSheet("font:12pt")
        self.opt_lineEdit_saveImgDir.setStyleSheet("font:12pt")

        self.opt_comboBox_downFileFmt.clear()
        self.opt_comboBox_downFileFmt.setEnabled(True)
        self.opt_comboBox_downFileFmt.addItem(".avi")
        self.opt_comboBox_downFileFmt.addItem(".mp4")
        self.opt_comboBox_downFileFmt.setCurrentIndex(0)
        self.opt_comboBox_downFileFmt.setStyleSheet("font:12pt")

        self.opt_comboBox_downFileDef.clear()
        self.opt_comboBox_downFileDef.setEnabled(True)
        self.opt_comboBox_downFileDef.addItem("360p")
        self.opt_comboBox_downFileDef.addItem("240p")
        self.opt_comboBox_downFileDef.addItem("480p")
        self.opt_comboBox_downFileDef.addItem("720p")
        self.opt_comboBox_downFileDef.addItem("1080p")
        self.opt_comboBox_downFileDef.setCurrentIndex(0)
        self.opt_comboBox_downFileDef.setStyleSheet("font:12pt")

        self.opt_comboBox_coordFmt.clear()
        self.opt_comboBox_coordFmt.setEnabled(True)
        self.opt_comboBox_coordFmt.addItem("CSV")
        self.opt_comboBox_coordFmt.addItem("JSON")
        self.opt_comboBox_coordFmt.setStyleSheet("font:12pt")

        self.opt_comboBox_bbox.clear()
        self.opt_comboBox_bbox.setEnabled(True)
        self.opt_comboBox_bbox.addItem("On")
        self.opt_comboBox_bbox.addItem("Off")
        self.opt_comboBox_bbox.setStyleSheet("font:12pt")

        self.opt_comboBox_bufTime.clear()
        self.opt_comboBox_bufTime.setEnabled(True)
        self.opt_comboBox_bufTime.addItem("1초")
        self.opt_comboBox_bufTime.addItem("2초")
        self.opt_comboBox_bufTime.addItem("3초")
        self.opt_comboBox_bufTime.addItem("4초")
        self.opt_comboBox_bufTime.addItem("5초")
        self.opt_comboBox_bufTime.setCurrentIndex(0)
        self.opt_comboBox_bufTime.setStyleSheet("font:12pt")


        ###########
        # 설정.콤보박스 이벤트 핸들러 설정
        ###########
        self.opt_comboBox_downFileFmt.currentIndexChanged.connect(self.change_opt_comboBox_downFileFmt)
        self.opt_comboBox_downFileDef.currentIndexChanged.connect(self.change_opt_comboBox_downFileDef)
        self.opt_comboBox_coordFmt.currentIndexChanged.connect(self.change_opt_comboBox_coordFmt)
        self.opt_comboBox_bufTime.currentIndexChanged.connect(self.change_opt_comboBox_bufTime)

        ###########
        # 영상검출탭 클릭이벤트 핸들러 설정
        ###########
        QtCore.QObject.connect(self.tab_ext,QtCore.SIGNAL('clicked()'),self.click_tab_ext)
        self.ext_pushButton_localUpload.clicked.connect(self.click_ext_pushButton_localUpload)
        self.ext_pushButton_urlUpload.clicked.connect(self.click_ext_pushButton_urlUpload)
        self.ext_pushButton_play.clicked.connect(self.click_ext_pushButton_play)
        self.ext_pushButton_pause.clicked.connect(self.click_ext_pushButton_pause)
        self.ext_pushButton_stop.clicked.connect(self.click_ext_pushButton_stop)
        self.ext_pushButton_allClear.clicked.connect(self.click_ext_pushButton_allClear)
        self.ext_pushButton_selectDelete.clicked.connect(self.click_ext_pushButton_selectDelete)
        # self.ext_pushButton_allSave.clicked.connect(self.click_ext_pushButton_allSave)
        # self.ext_pushButton_selectSave.clicked.connect(self.click_ext_pushButton_selectSave)
        self.ext_pushButton_startExt.clicked.connect(self.click_ext_pushButton_startExt)
        self.ext_pushButton_mdDown.clicked.connect(self.click_ext_pushButton_mdDown)
        # 영상 검출 내역 더블클릭 이벤트
        self.ext_tableView_extResultList.doubleClicked.connect(self.click_ext_tableView_extResultList)

        ###########
        # 오토포커싱탭 클릭이벤트 핸들러 설정
        ###########
        QtCore.QObject.connect(self.tab_afc,QtCore.SIGNAL('clicked()'),self.click_tab_afc)
        self.afc_pushButton_localUpload.clicked.connect(self.click_afc_pushButton_localUpload)
        self.afc_pushButton_mdDown.clicked.connect(self.click_afc_pushButton_mdDown)
        self.afc_pushButton_urlUpload.clicked.connect(self.click_afc_pushButton_urlUpload)
        self.afc_pushButton_play.clicked.connect(self.click_afc_pushButton_play)
        self.afc_pushButton_pause.clicked.connect(self.click_afc_pushButton_pause)
        self.afc_pushButton_stop.clicked.connect(self.click_afc_pushButton_stop)
        self.afc_pushButton_startExt.clicked.connect(self.click_afc_pushButton_startExt)
        self.afc_horizontalSlider.sliderReleased.connect(self.chaened_afc_horizontalSlider)

        ###########
        # 수동학습탭 클릭이벤트 핸들러 설정
        ###########

        self.alr_pushButton_localUpload.clicked.connect(self.click_alr_pushButton_localUpload)
        self.alr_pushButton_extImage.clicked.connect(self.click_alr_pushButton_extImage)
        self.alr_pushButton_openFolder.clicked.connect(self.click_alr_pushButton_openFolder)
        self.alr_pushButton_startLearning.clicked.connect(self.click_alr_pushButton_startLearning)
        self.alr_pushButton_play.clicked.connect(self.click_alr_pushButton_play)
        self.alr_pushButton_pause.clicked.connect(self.click_alr_pushButton_pause)
        self.alr_pushButton_stop.clicked.connect(self.click_alr_pushButton_stop)

        ###########
        # 설정탭 클릭이벤트 핸들러 설정
        ###########
        self.mainTabWidget.currentChanged.connect(self.click_tab)
        self.mainTabWidget.tabBar().installEventFilter(self)
        self.mainTabWidget.tabBar().preIndex = 0

        self.opt_pushButton_urlDownDir.clicked.connect(self.click_opt_pushButton_urlDownDir)
        self.opt_pushButton_saveDir.clicked.connect(self.click_opt_pushButton_saveDir)
        self.opt_pushButton_saveImgDir.clicked.connect(self.click_opt_pushButton_saveImgDir)

        # 작업 클래스 생성
        self.afc = Autofocus()
        self.cm = common(self)
        self.extClass = Extract(self)
        self.opt = Option(self)

        # 검출 대상 리스트 생성(검출탭, 포커싱탭, 학습탭)
        self.ext_btnGrp = self.cm.createTargetClassList("ext")
        self.afc_btnGrp = self.cm.createTargetClassList("afc")
        self.alr_btnGrp = self.cm.createTargetClassList("alr")

        # print("self.ext_btnGrp :: ", self.ext_btnGrp)
        # print("self.afc_btnGrp :: ", self.afc_btnGrp)
        # print("self.alr_btnGrp :: ", self.alr_btnGrp)

        # 검출 대상 리스트 이벤트 핸들러 추가
        self.ext_btnGrp.buttonClicked.connect(self.click_ext_btnGrp)
        self.afc_btnGrp.buttonClicked.connect(self.click_afc_btnGrp)


        # 영상 추출
        self.cm.video_player.changeTime.connect(self.set_time)
        self.cm.video_player.setTotalTime.connect(self.set_afc_totalTime)
        self.cm.video_player.changePixmap.connect(self.setPixMap)
        self.cm.video_player.changeExtFrame.connect(self.insertAtResultListData)
        self.cm.video_player.endExt.connect(self.endExtProcSetting)
        self.cm.video_player.saveFaceInitAlr.connect(self.saveFaceInitAlr)

        # 오토포커싱
        self.cm.video_player.changeTime.connect(self.set_afc_before_time)
        self.cm.video_player.changePixmap.connect(self.set_before_PixMap)
        # self.afc.changePixmap.connect(self.process_afc)
        self.cm.video_player.afc.changePixmap.connect(self.process_afc)
        self.cm.video_player.finishAfc.connect(self.enabled_afc_horizontalSlider)
        # 수동학습
        self.cm.video_player.changePixmap.connect(self.setAlrPixMap)
        self.cm.video_player.changeTime.connect(self.set_alr_time)
        self.cm.video_player.alrExtEnd.connect(self.endAlrExt)

    def click_ext_btnGrp(self):
        '''
        영상 clip의 클래스 선택 checkbox buttongroup을 클릭할 시 동작한다.
        :return:
        '''
        # TODO : 19.10.21 Select Target Class Sort
        print("click_ext_btnGrp")
        print("현재 선택된 class : {}".format(self.cm.getSelectedClassList('ext')))

        # 클래스 리스트 체크박스 초기화
        selectClass = self.cm.getSelectedClassList('ext')

        if len(self.cm.video_player.totalExtData) <= 0:
            self.cm.create_massage_box("confirm", text='검색 내역이 존재하지않습니다.')
            return

        compareList = list()
        if self.extClass.clearRowData():
            sortingDataList = list()        # 생성 데이터 리스트
            for targetFrameList in self.cm.video_player.totalExtData:       # 전체 프레임 데이터 리스트
                for targetIdx in range(len(targetFrameList)-1):
                    # 선택한 클래스 있는지 확인
                    for target in selectClass:
                        if str(targetFrameList[targetIdx]['labelname']) == str(target) and str(targetFrameList[-1]) not in compareList:
                            compareList.append(targetFrameList[-1])
                            # 소팅 데이터 및 대상 썸네일 이미지 정리
                            self.extClass.extAddRowData(self.cm.video_player.totalExtImgs[targetIdx], targetFrameList)
        else:
            print("테이블 내역 초기화에 실패하였습니다.")


    def click_afc_btnGrp(self):
        '''
        영상 clip의 클래스 선택 checkbox buttongroup을 클릭할 시 동작한다.
        :return:
        '''

        # print("click_afc_btnGrp")
        # print("selected Class")
        self.cm.video_player.pauseVideo()
        changed_className = self.cm.getSelectedClassList('afc')

        if not self.afc.getClassName() == changed_className:
            # print("Change Class Name")
            self.afc.setClassName(changed_className)

        # 클래스 변경 전 일시정지 -> 이름 변경 -> 검출시작 버튼 클릭 순
        # 영상재생 상태 1 -> 선택처리
        if self.cm.video_player.afc_state == 1:
            # print("검출 클래스 변경!!")
            self.cm.video_player.pauseVideo()
            self.click_afc_pushButton_startExt()

    def change_opt_comboBox_downFileFmt(self):
        """
        MEMO : 내려받기 확장자 변경 이벤트
        :return:
        """
        # print("opt_comboBox_bufTime_Change 변경 값 ::",self.opt_comboBox_bufTime.currentText())

    def change_opt_comboBox_downFileDef(self):
        """
        MEMO : 내려받기 화질 선택 변경 이벤트
        :return:
        """
        # print("opt_comboBox_bufTime_Change 변경 값 ::",self.opt_comboBox_bufTime.currentText())

    def change_opt_comboBox_coordFmt(self):
        """
        MEMO : 좌표파일 확장자 선택 변경 이벤트
        :return:
        """
        # print("opt_comboBox_bufTime_Change 변경 값 ::",self.opt_comboBox_bufTime.currentText())

    def change_opt_comboBox_bufTime(self):
        """
        MEMO : 추출 영상 버퍼시간 변경 이벤트
        :return:
        """
        # print("opt_comboBox_bufTime_Change 변경 값 ::",self.opt_comboBox_bufTime.currentText())


    def comm_tableWidget_classList_tHeader_setting(self):
        """
        MEMO : 추출 -> 검출대상리스트 테이블 기본 모델정보 셋팅
        :return:
        """
        # 헤더 사이즈 고정 (영상검출)
        self.ext_tableWidget_classList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ext_tableWidget_classList.verticalHeader().hide()              # header name hide
        self.ext_tableWidget_classList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed) # Size fixed

        # 헤더 사이즈 고정 (오토포커스)
        self.afc_tableWidget_classList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.afc_tableWidget_classList.verticalHeader().hide()
        self.afc_tableWidget_classList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        # 헤더 사이즈 고정 (학습탭)
        self.alr_tableWidget_classList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.alr_tableWidget_classList.verticalHeader().hide()
        self.alr_tableWidget_classList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        # 컬럼 높이 테이블 고정사이즈로 변경
        self.ext_tableWidget_classList.setRowHeight(0, int(self.ext_tableWidget_classList.maximumHeight()))
        self.afc_tableWidget_classList.setRowHeight(0, int(self.afc_tableWidget_classList.maximumHeight()))
        self.alr_tableWidget_classList.setRowHeight(0, int(self.alr_tableWidget_classList.maximumHeight()))

    def ext_default_tHeader_setting(self):
        """
        MEMO : 추출 -> 결과내역 테이블 헤더 및 기본 모델정보 셋팅
        :return:
        """
        # QStandardItemModel 로 모델 생성
        self.modelAttr = QtGui.QStandardItemModel()
        self.modelAttr = QtGui.QStandardItemModel()
        self.modelAttr.setColumnCount(7)
        self.modelAttr.setHeaderData(0, QtCore.Qt.Horizontal, "선택")
        self.modelAttr.setHeaderData(1, QtCore.Qt.Horizontal, "썸네일")
        self.modelAttr.setHeaderData(2, QtCore.Qt.Horizontal, "검출정보")
        self.modelAttr.setHeaderData(3, QtCore.Qt.Horizontal, "검출프레임번호")
        self.modelAttr.setHeaderData(4, QtCore.Qt.Horizontal, "검출좌표정보_히든")
        self.modelAttr.setHeaderData(5, QtCore.Qt.Horizontal, "검출라벨명_히든")
        self.modelAttr.setHeaderData(6, QtCore.Qt.Horizontal, "검출정확도_히든")
        self.ext_tableView_extResultList.setModel(self.modelAttr)

        # ※모델을 정의(setModel)한 뒤부터 컬럼에 대한 설정 가능(아래)

        # 체크박스 컬럼 넓이 조정
        self.ext_tableView_extResultList.setColumnWidth(0, 50)
        self.ext_tableView_extResultList.setColumnWidth(1, 50)
        self.ext_tableView_extResultList.setColumnWidth(2, 430)
        self.ext_tableView_extResultList.setColumnWidth(3, 110)
        self.ext_tableView_extResultList.setColumnHidden(4, True)
        self.ext_tableView_extResultList.setColumnHidden(5, True)
        self.ext_tableView_extResultList.setColumnHidden(6, True)

        # 테이블 row 단위 selection
        self.ext_tableView_extResultList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # 헤더 사이즈 고정처리
        self.ext_tableView_extResultList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ext_tableView_extResultList.verticalHeader().hide()
        self.ext_tableView_extResultList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        modelObj = self.ext_tableView_extResultList.model()


    ###########
    # 공통 클릭 이벤트
    ###########
    def eventFilter(self, object, event):
        # TODO : 영상 추출, 오토포커싱 초기화

        if object is self.mainTabWidget.tabBar() and event.type() == QtCore.QEvent.MouseButtonPress :
            # print(event.type())
            movedIndex = object.tabAt(event.pos()) # 이동할 인덱스
            currentIndex = object.currentIndex()  # 현재 인덱스
            # print(object.preIndex, currentIndex, movedIndex)
            cntIndes = self.mainTabWidget.count() - 1

            if currentIndex == cntIndes and movedIndex == object.preIndex:
                return False

            if movedIndex < cntIndes:
                if self.cm.create_massage_box("yesno", text='기 추출된 내역이 모두 삭제됩니다.\n탭을 이동하시겠습니까?'):
                    self.afc.quit_afcProcess()
                    self.extClass.clearRowData()
                    self.cm.quit_videoPlayer()
                    self.initVideoLabel()

                    # 검출 전체 데이터 초기화
                    self.cm.video_player.totalExtData = list()
                    self.cm.video_player.totalExtImgs = list()

                    # 검출대상리스트 헤더 및 기본 설정 (검출 / 오토포커싱 공통)
                    self.comm_tableWidget_classList_tHeader_setting()

                    object.preIndex = movedIndex
                    event.accept()
                    # print(object.preIndex,currentIndex,movedIndex)

                    # 탭 검출대상 리스트 초기화
                    # self.ext_btnGrp = self.cm.createTargetClassList("ext")
                    self.afc_btnGrp = self.cm.createTargetClassList("afc")
                    self.alr_btnGrp = self.cm.createTargetClassList("alr")

                    # self.ext_btnGrp.buttonClicked.connect(self.click_ext_btnGrp)
                    self.afc_btnGrp.buttonClicked.connect(self.click_afc_btnGrp)
                else:
                    event.ignore()
                    return True

            # 검출 및 오토포커싱 일 경우 검출 모델 지정
            # if int(movedIndex) < 2:
            #     self.cm.video_player.usedFaceStateNm = "vggface"
            #     self.cm.video_player.initModel()
            # elif int(movedIndex) == 2:
            #     self.cm.video_player.usedFaceStateNm = "vggalr"
            #     self.cm.video_player.initModel()


        elif object is self.mainTabWidget.tabBar() and event.type() == QtCore.QEvent.KeyPress:
            # print("key pressed!!")
            event.ignore()
            return True

        return False

    def click_ext_tableView_extResultList(self):
        """
        검출 테이블 데이터 더블클릭 이벤트
        :return:
        """
        # 영상이 플레이 상태이면 비디오플레이어를 일시정지 시킨 후 프레임 이동
        if self.cm.video_player.isPlaying():
            self.cm.video_player.pauseVideo()

        selRowNum = ""
        for idx in self.ext_tableView_extResultList.selectionModel().selectedIndexes():
            selRowNum = idx.row()
            selColNum = idx.column()

        # 검출 데이터 가져오기
        selectModel = self.ext_tableView_extResultList.model()
        colIdx = selectModel.index(int(selRowNum), 3)
        colData = colIdx.data()

        # 동영상 프레임 이동
        self.cm.video_player.moveFrame(int(colData))

    def click_tab(self):
        """
        MEMO : 탭 클릭 시 클릭 이벤트
        :return:
        """
        indexNum = self.mainTabWidget.currentIndex()
        if indexNum == 0:
            self.click_tab_ext()

        elif indexNum == 1:
            self.click_tab_afc()
        else:
            self.click_tab_opt()

        ###########
        # 공통 설정 경로 LineEdit 클릭 이벤트
        ###########

        ###########
        # 클릭 이벤트 영상검출 탭 start
        ###########

    def click_tab_ext(self):
        """
        MEMO : 영상검출 탭 클릭
        :return:
        """
        # print("click_tab_ext")
        # if self.cm.create_mcged")


    def click_ext_pushButton_localUpload(self):
        """
        MEMO : 영상검출.로컬업로드 버튼 클릭
        :return:
        """
        self.cm.video_player.buffertime = int(self.opt.get_buffertime()[0])

        if self.cm.video_player.isRunning() and self.cm.video_player.ext_state:
            # video player thread 종료 후 재시작
            if self.cm.create_massage_box("yesno",text='기 추출된 내역이 모두 삭제됩니다.\n계속하시겠습니까?'):
                self.extClass.clearRowData()
                self.cm.quit_videoPlayer()
            else:
                return

        if not self.cm.local_upload() == "":
            self.cm.video_player.openVideo(self.cm.uploadPath)

    def click_ext_pushButton_mdDown(self):
        """
        MEMO : 영상검출.영상 내려받기 버튼 클릭
        :return:
        """
        resultList = self.extClass.extGetDownloadData()
        saveCoord = True
        self.stackedLayout.setCurrentIndex(0)

        realTime = self.cm.getMicrotimes()
        self.cm.openVideoWriter(file_path="./faceExtractVideo_{}.{}".format(realTime, self.opt.get_downFileFmt()),format=self.opt.get_downFileFmt())
        self.cm.saveVideo(resultList)
        self.cm.closeVideoWriter()

        # 좌표정보 입력
        if saveCoord:
            self.cm.saveCoordFile(resultList,"./faceExtractCoord{}.{}".format(realTime,self.opt.get_coordFileFmt()),self.opt.get_coordFileFmt())

        self.cm.create_massage_box("Confirm","영상 내려받기가 완료되었습니다.")
        self.stackedLayout.setCurrentIndex(1)

    def click_ext_pushButton_urlUpload(self):
        """
        MEMO : 영상검출.URL 업로드 버튼 클릭
        :return:
        """
        self.cm.video_player.buffertime = int(self.opt.get_buffertime()[0])
        self.stackedLayout.setCurrentIndex(0)

        if self.cm.url_upload() is not "":
            self.cm.uploadPath = self.cm.downloadYouTubeUrl(self.cm.uploadUrl)
            if self.cm.uploadPath  is not "":
                if self.cm.video_player.isRunning() and self.cm.video_player.ext_state:
                    # video player thread 종료 후 재시작
                    if self.cm.create_massage_box("yesno", text="기 추출된 내역이 모두 삭제됩니다\n계속하시겠습니까?"):
                        self.extClass.clearRowData()
                        self.cm.quit_videoPlayer()

                self.cm.video_player.openVideo(self.cm.uploadPath)

        self.stackedLayout.setCurrentIndex(1)


    def click_ext_pushButton_play(self):
        """
        MEMO : 영상검출.play 버튼 클릭
        :return:
        """
        # print("click_ext_pushButton_play")
        # if self.cm.video_player.isRunning():
        #     if self.cm.create_massage_box("yesno","기 추출된 내역이 모두 삭제됩니다\n계속하시겠습니까?"):
        #         self.extClass.clearRowData()

        self.cm.video_player.playVideo()

    def click_ext_pushButton_pause(self):
        """
        MEMO : 영상검출.일시정지 버튼 클릭
        :return:
        """
        # print("click_ext_pushButton_pause")
        self.cm.video_player.pauseVideo()

    def click_ext_pushButton_stop(self):
        """
        MEMO : 영상검출.정지 버튼 클릭
        :return:
        """
        # print("click_ext_pushButton_stop")
        self.extClass.clearRowData()
        self.cm.quit_videoPlayer()
        self.initVideoLabel()

        # 검출 전체 데이터 초기화
        self.cm.video_player.totalExtData = list()
        self.cm.video_player.totalExtImgs = list()

    def click_ext_pushButton_allClear(self):
        """
        MEMO : 영상검출.검출내역테이블 초기화 버튼 클릭
        :return:
        """
        # print("click_ext_pushButton_allClear")
        self.clearYN = self.cm.create_massage_box("YesNo", text="모든 검출 내역이 초기화 됩니다 계속하시겠습니까?")

        if self.clearYN:
            self.extClass.clearRowData()

    def click_ext_pushButton_selectDelete(self):
        """
        MEMO : 영상검출.검출내역테이블 선택삭제 버튼 클릭
        :return:
        """
        # print("click_ext_pushButton_selectDelete")

        ## 체크한 인덱스 혹은 modelrow 추출

        self.clearYN = self.cm.create_massage_box("YesNo","선택 내역을 삭제하시겠습니까?")

        if self.clearYN:
            self.extClass.deleteRowData()

    # def click_ext_pushButton_allSave(self):
    #     """
    #     MEMO : 영상검출.검출내역테이블 전체 내려받기 버튼 클릭
    #     :return:
    #     """
    #     self.clearYN = self.cm.create_massage_box("YesNo", "전체 검출 내역을 내려받기 하시겠습니까?")
    #
    #     if self.clearYN:
    #         resultData = self.extClass.extGetDownloadData('all')
    #         ## TODO :: 191005_영상다운로드 & 좌표다운로드 메서드 쪽으로 넘기기

    # def click_ext_pushButton_selectSave(self):
    #     """
    #     MEMO : 영상검출.검출내역테이블 선택내역 영상 내려받기
    #     :return:
    #     """
    #     print("click_ext_pushButton_selectSave")
    #
    #     self.cm.getSelectedClassList("ext")
    #
    #     # self.clearYN = self.cm.create_massage_box("YesNo", "선택 내역을 내려받기 하시겠습니까?")
    #     #
    #     # if self.clearYN:
    #     #     resultData = self.extClass.extGetDownloadData('sel')
    #     #     print("download Data info :: (sel)")
    #     #     print(resultData)
    #     #     ## TODO :: 191005_영상다운로드 & 좌표다운로드 메서드 쪽으로 넘기기

    def click_ext_pushButton_startExt(self):
        """
        MEMO : 영상검출.검출시작 버튼 클릭
        :return:
        """
        # print("click_ext_pushButton_startExt")
        # TODO : Upload Ext Click

        if self.cm.classCheckBoxOnOffHandler("ext", "clear"):
            self.cm.classCheckBoxOnOffHandler("ext", "hide")
            # SORTING 을 위한 전역 변수 초기화
            self.cm.video_player.totalExtImgs = list()
            self.cm.video_player.totalExtData = list()

        self.cm.video_player.pauseVideo()

        # TODO : 191029 JK
        self.cm.video_player.usedFaceStateNm = "vggface"
        # self.cm.video_player.usedFaceStateNm = "facenet2"

        # 가장 최신의 피클파일로 설정
        if self.cm.video_player.usedFaceStateNm == "vggface":
            self.cm.video_player.vggRecogModel.precompute_features_map = self.cm.selectLastUptPickleFeatureList("map")

        if self.cm.video_player.ext_state == 0 or self.cm.video_player.ext_state == 2:
            self.cm.video_player.ext_state = 1

        # 클래스 리스트 체크박스 초기화
        self.cm.getSelectedClassList("clear")

        self.cm.video_player.moveFrame(self.cm.video_player.current_workingFrame)
        self.cm.video_player.playVideo()


    def click_tab_afc(self):
        """
        MEMO : 오토포커싱 탭 클릭
        :return:
        """
        # print("click_tab_afc123132")


    def click_afc_pushButton_localUpload(self):
        """
        MEMO : 오토포커싱 로컬 업로드 버튼 클릭
        :return:
        """
        self.cm.video_player.buffertime = int(self.opt.get_buffertime()[0])

        if self.cm.video_player.isRunning() and self.cm.video_player.afc_state:
            # video player thread 종료 후 재시작
            if self.cm.create_massage_box("yesno",text='기 추출된 내역이 모두 삭제됩니다.\n계속하시겠습니까?'):
                self.cm.quit_videoPlayer()
                self.afc.quit_afcProcess()
            else:
                return

        if not self.cm.local_upload() == "":
            self.initVideoLabel()
            self.cm.video_player.openVideo(self.cm.uploadPath)
            self.cm.video_player.afc.setUp(self.cm.form)


    def click_afc_pushButton_startExt(self):
        """
        MEMO : 오토포커싱, 검출 시작 버튼
        :return:
        """
        # print("afc_pushButton_startExt")
        class_name = self.cm.getSelectedClassList("afc")
        if not class_name == []:
            self.afc.setClassName(class_name[0])

            self.cm.video_player.pauseVideo()

            if self.cm.video_player.cap.isOpened():
                if self.cm.video_player.afc_state == 0 or self.cm.video_player.afc_state == 2:
                    self.cm.video_player.afc_state = 1
                    self.afc_horizontalSlider.setEnabled(False)

                self.cm.video_player.moveFrame(self.cm.video_player.current_workingFrame)

            self.cm.video_player.playVideo()
        else:
            self.cm.create_massage_box("Confirm",text='오토포커싱 대상이 선택하지 않았습니다.')

            


    def click_afc_pushButton_mdDown(self):
        """
        MEMO : 오토포커싱 영상 내려받기 버튼 클릭
        :return:
        """
        # print("afc_pushButton_mdDown")
        ###########################
        # loading 창 띄우기
        ############################

        self.cm.video_player.pauseVideo()
        result = self.afc.get_coordResult()

        if result == {}:
            self.cm.create_massage_box("confirm","기 추출된 내역이 없습니다.")
        else:
            self.stackedLayout.setCurrentIndex(0)
            realTime = self.cm.getMicrotimes()
            self.cm.openVideoWriter(file_path="./faceExtractVideo_{}{}".format(realTime,self.opt.get_downFileFmt()),
                                    format=self.opt.get_downFileFmt())
            self.cm.saveVideo([],"afc")
            self.cm.closeVideoWriter()

            # saveCoord = True
            # if saveCoord:
            #     self.cm.saveCoordFile([]],
            #                           "./faceExtractCoord{}.{}".format(realTime, self.opt.get_coordFileFmt()),
            #                           self.opt.get_coordFileFmt())

            self.cm.create_massage_box("Confirm","영상 내려받기가 완료되었습니다.")
            self.stackedLayout.setCurrentIndex(1)



    def click_afc_pushButton_urlUpload(self):
        """
        MEMO : 오토포커싱 URL 업로드 버튼 클릭
        :return:
        """
        self.cm.video_player.buffertime = int(self.opt.get_buffertime()[0])
        self.stackedLayout.setCurrentIndex(0)

        if self.cm.url_upload() is not "":
            self.cm.uploadPath = self.cm.downloadYouTubeUrl(self.cm.uploadUrl)

            if self.cm.video_player.isRunning() and self.cm.video_player.afc_state:
                # video player thread 종료 후 재시작
                if self.cm.create_massage_box("yesno",text="기 추출된 내역이 모두 삭제됩니다\n계속하시겠습니까?"):
                    self.extClass.clearRowData()
                    self.cm.quit_videoPlayer()
            self.cm.video_player.usedFaceStateNm = "vggface"
            self.cm.video_player.openVideo(self.cm.uploadPath)

        self.stackedLayout.setCurrentIndex(1)

    def click_afc_pushButton_play(self):
        """
        MEMO : 오토포커싱. 원본 영상 플레이 버튼 클릭
        :return:
        """
        # Validation Check 필요함
        # 포커싱 된 영상이 존재할 경우 메시지박스 띄우고
        # 포커싱 영상이 없을 경우 메시지박스 없이 원본 영상만 교체
        # if self.cm.create_massage_box("yesno", "기 추출된 내역이 모두 삭제됩니다\n계속하시겠습니까?"):

        self.cm.video_player.playVideo()

        # if not self.afc.afc_state:
        #     self.cm.video_player.playVideo()
        # else:
        #     if self.afc.isRunning() and self.afc.afc_play == 0:
        #         # self.afc.changePixmap.connect(self.play_afc)
        #         self.afc.afc_play = 1

    def click_afc_pushButton_pause(self):
        """
        MEMO : 오토포커싱. 원본 영상 일시정지 버튼 클릭
        :return:
        """
        # print("afc_pushButton_pause")
        self.cm.video_player.pauseVideo()

        # if self.cm.video_player.isRunning():
        #     self.cm.video_player.pauseVideo()
        # else:
        #     self.afc.afc_play = 0

    def click_afc_pushButton_stop(self):
        """
        MEMO : 오토포커싱. 원본 영상 정지 버튼 클릭
        :return:
        """
        # print("afc_pushButton_stop")

        # TODO : 초기화 붙이기
        self.afc.quit_afcProcess()
        self.cm.quit_videoPlayer()
        self.initVideoLabel()

        # 검출 전체 데이터 초기화
        self.cm.video_player.totalExtData = list()
        self.cm.video_player.totalExtImgs = list()

    def click_afc_label_before_Md(self):
        """
        MEMO : 오토포커싱. 원본 영상 화면라벨영역 클릭
        :return:
        """
        # print("afc_label_before_Md")

    def afc_label_after_Md(self):
        """
        MEMO : 오토포커싱. 포커싱 영상 화면라벨영역 버튼 클릭
        :return:
        """
        # print("afc_label_after_Md")

    def chaened_afc_horizontalSlider(self):
        # print("slider min,max {} {}".format(self.afc_horizontalSlider.minimum(),self.afc_horizontalSlider.maximum()))
        if self.cm.video_player.isPlaying():
            self.cm.video_player.pauseVideo()
            self.cm.video_player.moveFrame(self.afc_horizontalSlider.value())
            self.cm.video_player.playVideo()
        else:
            self.cm.video_player.moveFrame(self.afc_horizontalSlider.value())

        ###########
        # 클릭 이벤트 오토포커싱 탭 end
        ###########

    ###########
    # 클릭 이벤트 수동학습 탭 start
    ###########

    def click_alr_pushButton_localUpload(self):
        """
        MEMO : 학습.로컬업로드 버튼 클릭
        :return:
        """
        # print("click_alr_pushButton_localUpload")
        self.cm.video_player.buffertime = int(self.opt.get_buffertime()[0])

        if self.cm.video_player.isRunning() and self.cm.video_player.ext_state:
            # video player thread 종료 후 재시작
            if self.cm.create_massage_box("yesno",text='기 추출된 내역이 모두 삭제됩니다.\n계속하시겠습니까?'):
                self.cm.quit_videoPlayer()
            else:
                return

        if not self.cm.local_upload() == "":
            self.cm.video_player.openVideo(self.cm.uploadPath)

    def click_alr_pushButton_extImage(self):
        """
        MEMO : 학습 이미지 추출 버튼 클릭
        :return:
        """
        # print("click_alr_pushButton_extImage")
        className = ""
        # 추출 파일명 확인 없으면 메시지 리턴
        if self.cm.inputAlrClassName() == "":
            if self.cm.create_massage_box("Confirm", text='업로드된 영상이 없습니다.\n얼굴 추출 영상을 먼저 업로드해주세요.'):
                return

        className = self.cm.classNmAlr
        if className != "":
            # 해당 클래스명으로 폴더생성
            path = self.opt.get_saveImgDir().replace('\\', '/')
            if os.path.exists(path) == False:
                os.mkdir(path)
            fullPath = os.path.join(path, className)
            if os.path.exists(fullPath) == False:
                os.mkdir(fullPath)

            # 클래스 폴더 관련 변수 데이터 저장
            self.cm.video_player.targetPicklePath = self.cm.selectLastUptPickleFeatureList("path")
            self.cm.video_player.saveClassNamePath = path   # 상위폴더
            self.cm.video_player.saveClassName = className  # 클래스폴더명

            self.cm.video_player.usedFaceStateNm = "vggface"
            # 비디오 일시정지
            self.cm.video_player.pauseVideo()

            if self.cm.video_player.cap.isOpened():
                if self.cm.video_player.alr_state == 0 or self.cm.video_player.alr_state == 2:
                    self.cm.video_player.alr_state = 1

                self.cm.video_player.moveFrame(self.cm.video_player.current_workingFrame)

            self.cm.video_player.playVideo()
        else:
            if self.cm.create_massage_box("rConfirm", text='클래스명을 입력해주세요.'):
                return


    def click_alr_pushButton_openFolder(self):
        """
        MEMO : 학습. 폴더 열기 버튼 클릭
        :return:
        """
        # print("click_alr_pushButton_openFolder")
        import subprocess, platform
        # OS 별 File Seperator 설정
        pSysNm = platform.system()

        if pSysNm is "Windows":
            path = self.opt.get_saveImgDir().replace('\\', '/')
            subprocess.run(['explorer', os.path.realpath(path)])
        elif pSysNm is "Darwin":
            path = self.opt.get_saveImgDir().replace('\\', '/')
            subprocess.run(['nautilus', os.path.realpath(path)])
        elif str(pSysNm) == "Linux":
            path = self.opt.get_saveImgDir().replace('\\', '/')
            subprocess.run(['nautilus', os.path.realpath(path)])

    def click_alr_pushButton_startLearning(self):
        """
        MEMO : 학습. 학습 시작 버튼 클릭
        :param self:
        :return:
        """
        # print("click_alr_pushButton_startLearning")
        if self.cm.create_massage_box("yesno", text="학습을 진행하시겠습니까?"):
            # 로딩바 on
            self.stackedLayout.setCurrentIndex(0)

            retCode, picklePath = self.cm.video_player.learningPickle()
            if retCode == True:
                # 로딩바 off
                self.cm.create_massage_box("confirm", "학습이 완료되었습니다.")
                #TODO: 191018학습 완료 시 클래스 리스트 초기화 하고 피클 정보도 새로 업로드 해야함 (제일 처음에 피클 최신으로 끼우는거 다시)

                # 검출대상 리스트 초기화
                self.cm.classCheckBoxOnOffHandler("ext", "delete")
                self.cm.classCheckBoxOnOffHandler("afc", "delete")
                self.cm.classCheckBoxOnOffHandler("alr", "delete")

                # video_player 의 __init__ 타겟 피클파일 변수정보를 최신화 시켜준다.
                self.cm.video_player.targetPicklePath = self.cm.video_player.selectLastUptPickleFeatureList("path")
                self.cm.video_player.usedFaceStateNm = "vggface"
                # 가장 최신의 피클파일로 설정
                self.cm.video_player.vggRecogModel.precompute_features_map = self.cm.selectLastUptPickleFeatureList("map")

                # 검출 대상 리스트 생성(검출탭, 포커싱탭, 학습탭)
                self.ext_btnGrp = self.cm.createTargetClassList("ext")
                self.afc_btnGrp = self.cm.createTargetClassList("afc")
                self.alr_btnGrp = self.cm.createTargetClassList("alr")

                self.ext_btnGrp.buttonClicked.connect(self.click_ext_btnGrp)
                self.afc_btnGrp.buttonClicked.connect(self.click_afc_btnGrp)
            else:
                self.cm.create_massage_box("confirm", "학습이 실패하였습니다.")

            self.stackedLayout.setCurrentIndex(1)


    def click_alr_pushButton_play(self):
        """
        MEMO : 학습. 영상 재생 버튼 클릭
        :return:
        """
        # print("click_alr_pushButton_play")
        self.cm.video_player.playVideo()

    def click_alr_pushButton_pause(self):
        """
        MEMO : 학습. 영상 일시정지 버튼 클릭
        :return:
        """
        # print("click_alr_pushButton_pause")
        self.cm.video_player.pauseVideo()

    def click_alr_pushButton_stop(self):
        """
        MEMO : 학습. 영상 정지 버튼 클릭
        :return:
        """
        # print("click_alr_pushButton_stop")
        ###########
        # 클릭 이벤트  수동학습 탭 end
        ###########

        ###########
        # 클릭 이벤트 설정 탭 start
        ###########


    def click_tab_opt(self):
        """
        MEMO : 설정탭 클릭
        :return:
        """
        # print("click_tab_opt")

    def click_opt_pushButton_urlDownDir(self):
        """
        MEMO : 설정 URL 저장 파일 경로 폴더찾기 버튼 클릭
        :return:
        """
        # print("opt_pushButton_urlDownDir")
        # self.opt_lineEdit_urlSaveDir.setText(self.cm.optUrlSaveFileDir())
        button = self.sender()
        self.opt.set_directory(button)

    def click_opt_pushButton_saveDir(self):
        """
        MEMO : 설정 내려받기 저장 파일 경로 폴더찾기 버튼 클릭
        :return:
        """
        # print("opt_pushButton_saveDir")
        # self.opt_lineEdit_saveDir.setText(self.cm.optUrlSaveFileDir())
        button = self.sender()
        self.opt.set_directory(button)


    def click_opt_pushButton_saveImgDir(self):
        """
        MEMO : 설정 내려받기 저장 파일 경로 폴더찾기 버튼 클릭
        :return:
        """
        # print("opt_pushButton_saveDir")
        # self.opt_lineEdit_saveDir.setText(self.cm.optUrlSaveFileDir())
        button = self.sender()
        self.opt.set_directory(button)

        ###########
        # 클릭 이벤트 설정 탭 end
        ###########

        ##########
        # img label update
        ##########

    @QtCore.Slot()
    def endAlrExt(self):
        self.cm.create_massage_box("Confirm", "영상내 얼굴 이미지 검출이 완료되었습니다.")
        if self.cm.create_massage_box("YesNo", text="얼굴 이미지 폴더를 오픈하시겠습니까?"):
            import subprocess, platform
            # OS 별 File Seperator 설정
            pSysNm = platform.system()
            imgDir = self.opt_lineEdit_saveImgDir.text()
            if pSysNm is "Windows":
                path = imgDir.replace('\\', '/')
                subprocess.run(['explorer', os.path.realpath(path)])
            elif pSysNm is "Darwin":
                path = imgDir.replace('\\', '/')
                subprocess.run(['nautilus', os.path.realpath(path)])
            elif str(pSysNm) == "Linux":
                path = imgDir.replace('\\', '/')
                subprocess.run(['nautilus', os.path.realpath(path)])

        # 이미지 저장 경로 설정
        self.cm.video_player.vggRecogModel.FACE_IMAGES_FOLDER = self.opt_lineEdit_saveImgDir.text()



    @QtCore.Slot(dict)
    def saveFaceInitAlr(self):
        """
        학습에 필요한 기본 설정 변수를 셋팅한다.
        :return:
        """
        initDict = dict()
        self.opt.get_saveImgDir()

    @QtCore.Slot()
    def endExtProcSetting(self):
        """
        검출 영상 종료 후 클래스 리스트 체크박스 초기화
        :param typeStr:
        :param flag:
        :return:
        """
        if self.cm.classCheckBoxOnOffHandler("ext", "clear"):
            self.cm.classCheckBoxOnOffHandler("ext", "show")
        self.cm.create_massage_box("Confirm", "영상 검출이 완료되었습니다.")
        # self.ext_pushButton_mdDown.setVisible(True)

    @QtCore.Slot(list)
    def insertAtResultListData(self,image,dataList):
        """
        얼굴 검출 결과 내역테이블 추가
        :param dataList:
        :return:
        """
        self.extClass.extAddRowData(image,dataList)

    @QtCore.Slot(QtGui.QImage)
    def setPixMap(self,image):
        image = QtGui.QPixmap.fromImage(image)
        image = image.scaled(self.ext_label_extMd.size(),QtCore.Qt.KeepAspectRatio)
        self.ext_label_extMd.setPixmap(image)


    @QtCore.Slot(QtGui.QImage)
    def set_before_PixMap(self,image):
        image = QtGui.QPixmap.fromImage(image)
        image = image.scaled(self.afc_label_before_Md.size(),QtCore.Qt.KeepAspectRatio)
        self.afc_label_before_Md.setPixmap(image)

    # @QtCore.Slot(QtGui.QImage,QtCore.QRect)
    @QtCore.Slot(QtGui.QImage)
    def set_after_PixMap(self,image):
        afc_image = QtGui.QPixmap.fromImage(image)
        # 좌표 처리
        afc_image = afc_image.copy(QtCore.QRect(405,77,500,430))  # QtCore.QRect(x, y, width, height)
        # print("width : {} height : {}".format(afc_image.width(), afc_image.height()))
        afc_image = afc_image.scaled(self.afc_label_after_Md.size(),QtCore.Qt.KeepAspectRatio)
        # self.afc_label_before_Md.setPixmap(image)
        self.afc_label_after_Md.setPixmap(afc_image)

    @QtCore.Slot(QtGui.QImage)
    def setAlrPixMap(self,image):
        image = QtGui.QPixmap.fromImage(image)
        image = image.scaled(self.alr_label_extMd.size(),QtCore.Qt.KeepAspectRatio)
        self.alr_label_extMd.setPixmap(image)

    @QtCore.Slot(QtGui.QImage, QtCore.QRect)
    def process_afc(self, image, rect):
        image = QtGui.QPixmap.fromImage(image)
        # 좌표 처리
        afc_image = image.copy(rect)  # QtCore.QRect(x, y, width, height)
        afc_image = afc_image.scaled(self.afc_label_after_Md.size(),QtCore.Qt.KeepAspectRatio)
        # image = image.scaled(self.afc_label_before_Md.size(), QtCore.Qt.KeepAspectRatio)
        # self.afc_label_before_Md.setPixmap(image)
        self.afc_label_after_Md.setPixmap(afc_image)

    @QtCore.Slot(QtGui.QImage,QtCore.QRect)
    def play_afc(self,image,rect):
        image = QtGui.QPixmap.fromImage(image)
        # 좌표 처리
        afc_image = image.copy(rect)  # QtCore.QRect(x, y, width, height)
        afc_image = afc_image.scaled(self.afc_label_after_Md.size(),QtCore.Qt.KeepAspectRatio)
        # image = image.scaled(self.afc_label_before_Md.size(),QtCore.Qt.KeepAspectRatio)
        # self.afc_label_before_Md.setPixmap(image)
        self.afc_label_after_Md.setPixmap(afc_image)

    @QtCore.Slot(int,int)
    def set_time(self,cur_time,total_time):
        cur_seconds = int(cur_time % 60)
        cur_minutes = int((cur_time / 60) % 60)
        cur_hours = int(cur_time / 3600)
        total_seconds = int(total_time % 60)
        total_minutes = int((total_time / 60) % 60)
        total_hours = int(total_time / 3600)
        update_time = "{0:02d}:{1:02d}:{2:02d} / {3:02d}:{4:02d}:{5:02d}".format(cur_hours,cur_minutes,cur_seconds,
                                                                                 total_hours,total_minutes,
                                                                                 total_seconds)
        self.ext_video_time.setText(update_time)

    @QtCore.Slot(int,int)
    def set_afc_before_time(self,cur_time,total_time):
        cur_seconds = int(cur_time % 60)
        cur_minutes = int((cur_time / 60) % 60)
        cur_hours = int(cur_time / 3600)
        total_seconds = int(total_time % 60)
        total_minutes = int((total_time / 60) % 60)
        total_hours = int(total_time / 3600)
        update_time = "{0:02d}:{1:02d}:{2:02d} / {3:02d}:{4:02d}:{5:02d}".format(cur_hours,cur_minutes,cur_seconds,
                                                                                 total_hours,total_minutes,
                                                                                 total_seconds)
        self.afc_horizontalSlider.setValue(cur_time * self.cm.video_player.fps)
        self.afc_before_time.setText(update_time)

    @QtCore.Slot(int)
    def set_afc_totalTime(self, total_time):
        # print(total_time)
        self.afc_horizontalSlider.setMaximum(total_time)
        # print(self.afc_horizontalSlider.maximum())

    @QtCore.Slot(int,int)
    def set_alr_time(self,cur_time,total_time):
        cur_seconds = int(cur_time % 60)
        cur_minutes = int((cur_time / 60) % 60)
        cur_hours = int(cur_time / 3600)
        total_seconds = int(total_time % 60)
        total_minutes = int((total_time / 60) % 60)
        total_hours = int(total_time / 3600)
        update_time = "{0:02d}:{1:02d}:{2:02d} / {3:02d}:{4:02d}:{5:02d}".format(cur_hours,cur_minutes,cur_seconds,
                                                                                 total_hours,total_minutes,
                                                                                 total_seconds)
        self.alr_video_time.setText(update_time)

    @QtCore.Slot(int)
    def enabled_afc_horizontalSlider(self, state):
        # self.afc_horizontalSlider.setDisabled(state)
        if self.cm.create_massage_box("yesno", text='영상 오토포커싱이 완료되었습니다.\n결과 영상을 재생하시겠습니까?'):
            self.cm.video_player.moveFrame(0)
            self.cm.video_player.playVideo()

    def initVideoLabel(self):
        black_image = QtGui.QImage(1920,1280,QtGui.QImage.Format_Indexed8)
        black_image.fill(QtGui.qRgb(0,0,0))
        image = QtGui.QPixmap.fromImage(black_image)
        image = image.scaled(self.ext_label_extMd.size(),QtCore.Qt.KeepAspectRatio)
        self.ext_label_extMd.setPixmap(image)
        image = image.scaled(self.afc_label_before_Md.size(),QtCore.Qt.KeepAspectRatio)
        self.afc_label_before_Md.setPixmap(image)
        image = image.scaled(self.afc_label_after_Md.size(),QtCore.Qt.KeepAspectRatio)
        self.afc_label_after_Md.setPixmap(image)
        image = image.scaled(self.alr_label_extMd.size(),QtCore.Qt.KeepAspectRatio)
        self.alr_label_extMd.setPixmap(image)
        # print("alr size : {} ".format(self.alr_label_extMd.size()))

    def closeEvent(self, event):

        self.cm.video_player.stopVideo()
        self.cm.video_player.wait()

        super(Ui_Form, self).closeEvent(event)


if __name__ == "__main__":
    import sys
    from os import path

    # 패키지 경로(절대/상대) Validation Proc
    if __package__ is None:
        # print(path.dirname(path.dirname(path.abspath(__file__))))
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from extract import Extract
        from option import Option
        from autofocus import Autofocus
    else:
        from .extract import Extract
        from .option import Option
        from .autofocus import autofocus

    app = QtWidgets.QApplication(sys.argv)

    s_path = path.abspath("darkstyle/darkstyle.qss")
    with open(s_path, 'r') as f:
        app.setStyleSheet(f.read())

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.initVideoLabel()
    sys.exit(app.exec_())

