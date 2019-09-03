from PySide2 import QtGui, QtWidgets, QtCore
from common import common
from time import sleep

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
        # 첫번째 컬럼 - 체크박스
        chkItem = QtGui.QStandardItem()
        chkItem.setCheckable(True)
        chkItem.setEditable(False)
        chkItem.setTextAlignment(QtCore.Qt.AlignCenter)
        dModel.setItem(rowCnt, 0, chkItem)

        # 데이터 생성 #2
        # 두번째 컬럼 - 컴출클래스를 이용한 썸네일 이미지 입력 ()

        # 데이터 생성 #2
        # 두번째 컬럼 - 컴출클래스를 이용한 썸네일 이미지 입력 (ICON/브러시)
        thumnailImg = self.cm.createThumnail_filePath("D:/sampleImg/image2.jpg", 50, 50, 50)

        # icon 데이터로 썸네일 입력
        # ic = QtGui.QIcon()
        # ic.addPixmap(thumnailImg)
        # imgItem = QtGui.QStandardItem()
        # imgItem.setIcon(ic)
        # imgItem.setText("썸네일명")

        # 브러시를 이용하여 썸네일 입력
        # 추후 학습 결과를 QImage
        imgBrush = QtGui.QBrush()
        imgBrush.setTexture(thumnailImg)
        imgBrush.setStyle(QtCore.Qt.BrushStyle.RadialGradientPattern)
        imgItem = QtGui.QStandardItem()
        imgItem.setBackground(imgBrush)
        imgItem.setTextAlignment(QtCore.Qt.AlignCenter)
        imgItem.setEditable(False)

        dModel.setItem(rowCnt, 1, imgItem)

        # 데이터 생성 #3
        # 세번째~나머지 컬럼 - 텍스트 데이터 입력 처리 루프
        for colCnt in range(2,6):
            inputTextSample = "Input Result Value : {}".format(rowCnt)
            item = QtGui.QStandardItem(inputTextSample)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setEditable(False)
            dModel.setItem(rowCnt, colCnt, item)

        # Row Height 설정 (썸네일 이미지 뷰를 위하여 크기조정)
        # 데이터 ROW를 입력한 뒤에 해당 라인의 높이 설정이 가능함 건당 처리 필요
        self.table.setRowHeight(rowCnt, 50)


        print(rowCnt, " 번째 row 입력!! ")

        # 5번째만 출력해주고 나머지는 숨기기
        if rowCnt is 3:
            print("selectData :: ")
            # selectData = self.table.model().itemData(QtCore.QModelIndex())
            selectData = self.table.model().index(0,0).__eq__(QtGui.QAccessible.State.checked)
            # self.ext_tableView_extResultList.model().index(0, 0).__eq__(QtGui.QAccessible.State.checked)
            print(selectData)

        # 전체 모델 이동 후 모델 초기화 후 다시 집어넣고 확인
        if rowCnt is 6:
            print("전체 모델 이동 후 모델 초기화 후 다시 집어넣고 확인")
            data = self.table.selectionModel().selectedIndexes()
            print(data)

        # 개별삭제 테스트
        if rowCnt is 10:
            print("3번째 row 를 삭제합니다.")
            self.table.model().removeRow(3)
            print("3번째 삭제 후 row cnt :: ", self.table.model().rowCount())

        # 전체삭제 테스트
        if rowCnt is 15:
            print("전체 row 를 삭제합니다.")
            for rowNum in range(1, self.table.rowCount()):
                self.table.model().removeRow(rowNum)
            print("전체 삭제 후 row cnt :: ", self.table.model().rowCount())


