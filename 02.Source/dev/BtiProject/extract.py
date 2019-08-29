from PySide2 import QtGui, QtWidgets, QtCore
from common import common

class Extract(object):

    def __init__(self, ui):
        self.table = ui.ext_tableView_extResultList
        self.cm = common(ui)

    def add_tRowData(self):
        """
        # 영상검출 내역 테이블에 데이터를 추가한다.
        :return:
        """
        dModel = self.table.model()
        rowCnt = self.table.model().rowCount()

        # 데이터 생성 #1
        # (CheckBox + colData)
        chkItem = QtGui.QStandardItem()
        chkItem.setCheckable(True)
        chkItem.setEditable(False)
        dModel.setItem(rowCnt, 0, chkItem)

        # 썸네일 이미지 생성
        #thumnailImg = self.cm.createThumnail_filePath("D:/sampleImg/image2.jpg", 50, 50, 50)

        # 썸네일 넣고나면 2,6 으로 변경해야함
        for colCnt in range(1,6):
            item = QtGui.QStandardItem("Input Result Value")
            item.setEditable(False)
            dModel.setItem(rowCnt, colCnt, item)

        # Row Height 설정 (썸네일 이미지 뷰를 위하여 크기조정)
        self.table.setRowHeight(rowCnt, 70)