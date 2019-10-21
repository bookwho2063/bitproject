from PySide2 import QtGui, QtWidgets, QtCore
from time import sleep

class Extract(object):

    def __init__(self, ui):
        self.table = ui.ext_tableView_extResultList

    def clearRowData(self):
        """
        MEMO : 영상검출 테이블 내역을 초기화 한다. (전체삭제도 동일사용)
        :return:
        """
        retCode = True
        try:
            while self.table.model().rowCount() > 0:
                self.table.model().removeRow(self.table.model().rowCount()-1)
        except:
            retCode = False

        return retCode

    def deleteRowData(self):
        """
        MEMO : 선택 Row 삭제
        :param rowNum: num index list
        :return:
        """
        tableModel = self.table.model()
        rowCnt = self.table.model().rowCount()
        if rowCnt > 0:
            delList = []
            for rowNum in range(rowCnt):
                modelItem = tableModel.item(int(rowNum), 0)
                chkState = modelItem.checkState()
                if chkState is QtCore.Qt.CheckState.Unchecked:
                    continue
                else:
                    delList.append(rowNum)
            while len(delList) > 0:
                tableModel.removeRow(delList.pop())

    def getCheckBoxList(self):
        """
        MEMO : 검출 내역 테이블 체크된 내역을 리턴한다
        :return:
        """
        tableModel = self.table.model()
        rowCnt = self.table.model().rowCount()
        chkList = []
        if rowCnt > 0:
            for rowNum in range(rowCnt):
                modelItem = tableModel.item(int(rowNum), 0)
                chkState = modelItem.checkState()
                if chkState is QtCore.Qt.CheckState.Unchecked:
                    continue
                else:
                    chkList.append(rowNum)
        return chkList


    def extGetDownloadData(self):
        """
        MEMO : 선택/전체 영상 다운로드를 위하여 테이블 데이터 정리
        :param : downFlag(sel/all)
        :return: resultList
        """

        chkList = list()
        rowNum = self.table.model().rowCount()
        chkList = self.getCheckBoxList()  # 선택 내역 rownum List return

        if len(chkList) == 0:   # 체크된 것이 없으므로 전체 다운로드
            for idx in range(rowNum):
                chkList.append(idx)

        resultLists = list()
        for rowNum in chkList:
            # rowNum :: 체크 된 row 번호
            dataDict = dict()
            resultList = list()
            col2 = self.table.model().index(int(rowNum), 2).data()      # 검출정보
            frameNum = self.table.model().index(int(rowNum), 3).data()  # 프레임번호
            col4 = str(self.table.model().index(int(rowNum), 4).data()) #
            col5 = str(self.table.model().index(int(rowNum), 5).data()) #
            col6 = str(self.table.model().index(int(rowNum), 6).data()) #

            # 좌표 서브스트링, 붙여서 정리
            coordList = col4.split('/')
            labels = col5.split(',')
            percents = col6.split(',')
            for idx in range(len(coordList)):
                coord = coordList[idx].split(',')
                if len(coord) == 4:
                    dataDict['x'] = coord[0]
                    dataDict['y'] = coord[1]
                    dataDict['w'] = coord[2]
                    dataDict['h'] = coord[3]
                    dataDict['labelname'] = labels[idx]
                    dataDict['percent'] = percents[idx]
                    resultList.append(dataDict)
            # 프레임 정보 데이터를 정보의 제일 마지막에 추가
            resultList.append(frameNum)
            resultLists.append(resultList)

        return resultLists


    def extAddRowData(self, image, dataList):
        """
        MEMO : 영상검출 내역 테이블에 데이터를 추가한다. (영상 재생구간에 사용)
        :return:
        """
        dModel = self.table.model()
        rowCnt = self.table.model().rowCount()

        # 첫번째 컬럼 생성 (체크박스)
        chkItem = QtGui.QStandardItem()
        chkItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        chkItem.setCheckState(QtCore.Qt.Unchecked)
        dModel.setItem(rowCnt, 0, chkItem)

        # 검출 프레임 썸네일 추출
        thumnailImg = self.createThumnail_QImage("pixmap", image, 50, 50, 50)

        # 썸네일 이미지를 icon 으로 변환하여 입력
        imgIcon = QtGui.QIcon()
        imgIcon.addPixmap(thumnailImg)
        # 썸네일을 입력할 item 객체 생성 및 설정
        imgItems = QtGui.QStandardItem()
        imgItems.setIcon(imgIcon)
        imgItems.setTextAlignment(QtCore.Qt.AlignCenter)
        imgItems.setEditable(False)
        dModel.setItem(rowCnt, 1, imgItems)

        # 검출 정보 추출 (프레임 번호 제외)
        extInfoStr = ""     # 검출 명,정확도 정보
        extCoordStr = ""    # 검출 좌표 정보
        names = ""          # 검출 명
        pers = ""           # 검출 퍼센트
        for idx in range(len(dataList)-1):
            data = dataList[idx]

            nameStr = str(data['labelname'])
            perStr = str(data['percent'])
            coordXStr = str(data['x'])
            coordYStr = str(data['y'])
            coordWStr = str(data['w'])
            coordHStr = str(data['h'])

            if len(dataList)-2 == idx:
                extInfoStr = str(extInfoStr) + str(nameStr) + "[" + perStr + " %]"
                extCoordStr = extCoordStr + coordXStr + "," + coordYStr + "," + coordWStr + "," + coordHStr
                names = names + nameStr
                pers = pers + perStr
                continue

            extInfoStr = str(extInfoStr) + str(nameStr) + "[" + perStr + " %], "
            names = names + nameStr + ","
            pers = pers + perStr + ","

            if extCoordStr == "":
                extCoordStr = coordXStr + "," + coordYStr + "," + coordWStr + "," + coordHStr + "/"
            elif extCoordStr != "":
                extCoordStr = extCoordStr + coordXStr + "," + coordYStr + "," + coordWStr + "," + coordHStr + "/"

        for colIdx in range(2,7):
            if colIdx == 2:     # 검출 정보
                item = QtGui.QStandardItem(extInfoStr)
            elif colIdx == 3:   # 프레임번호
                item = QtGui.QStandardItem(dataList[-1])
            elif colIdx == 4:   # 좌표정보
                item = QtGui.QStandardItem(extCoordStr)
            elif colIdx == 5:   # 라벨명
                item = QtGui.QStandardItem(names)
            elif colIdx == 6:   # 정확도
                item = QtGui.QStandardItem(pers)

            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setEditable(False)
            dModel.setItem(rowCnt, colIdx, item)

        # 건당 데이터의 row 높이 설정
        self.table.setRowHeight(rowCnt, 50)

    def createThumnail_QImage(self, resultType, qImage, width, height, radius, antialiasing=True):
        """
        qImage 형식의 img 데이터를 이용하여 width/height 크기로
        원형 썸네일 QPixmap 생성 후 Label에 입력하여 리턴
        Realese : 썸네일 생성 관련 메서드 이동 common->extract
        :param qImage: 이미지데이터
        :param width: 넓이
        :param height: 높이
        :return: 썸네일 QImage / pixmap
        """

        resultLabel = QtWidgets.QLabel()
        resultLabel.setMaximumSize(width, height)
        resultLabel.setMinimumSize(width, height)
        target = QtGui.QPixmap(resultLabel.size())
        target.fill(QtCore.Qt.transparent)

        opt_radius = 25
        opt_antialiasing = True

        # imgData = QtGui.QPixmap(QtGui.QImage(qImage))\
        #     .scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

        imgData = QtGui.QPixmap(QtGui.QImage(qImage)).scaled(width, height)
        painter = QtGui.QPainter(target)
        if antialiasing:
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
            painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)

        path = QtGui.QPainterPath()
        path.addRoundedRect(
            0, 0, resultLabel.width(), resultLabel.height(), radius, radius
        )

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, imgData)
        resultLabel.setPixmap(target)

        if resultType is "image":
            return resultLabel
        elif resultType is "pixmap":
            return target



