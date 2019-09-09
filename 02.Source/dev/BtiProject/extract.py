from PySide2 import QtGui, QtWidgets, QtCore
from common import common
from time import sleep

class Extract(object):

    def __init__(self, ui):
        self.table = ui.ext_tableView_extResultList
        self.cm = common(ui)

    def clearRowData(self):
        """
        MEMO : 영상검출 테이블 내역을 초기화 한다. (전체삭제도 동일사용)
        :return:
        """
        while self.table.model().rowCount() > 0:
            self.table.model().removeRow(self.table.model().rowCount()-1)

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


    def add_tRowData(self):
        """
        # 영상검출 내역 테이블에 데이터를 추가한다.
        :return:
        """
        dModel = self.table.model()
        rowCnt = self.table.model().rowCount()

        # 데이터 생성 #1.1
        # 첫번째 컬럼 - 체크박스 (QStandardItem)
        # chkItem = QtGui.QStandardItem()
        # chkItem.setCheckable(True)
        # chkItem.setEditable(False)
        # chkItem.setTextAlignment(QtCore.Qt.AlignCenter)
        # dModel.setItem(rowCnt, 0, chkItem)

        # 데이터 생성 #1.2
        # 첫번째 컬럼 - 체크박스 (QTableWidgetItem)
        chkItem = QtGui.QStandardItem()
        chkItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        chkItem.setCheckState(QtCore.Qt.Unchecked)
        dModel.setItem(rowCnt, 0, chkItem)

        # 썸네일 이미지 추출
        thumnailImg = self.cm.createThumnail_filePath("pixmap", "D:/sampleImg/image2.jpg", 50, 50, 50)

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

        self.table.setRowHeight(rowCnt, 50)


    def extAddRowData(self, image, dataList):
        """
        # 영상검출 내역 테이블에 데이터를 추가한다. (영상 재생구간에 사용)
        :return:
        """
        dModel = self.table.model()
        rowCnt = self.table.model().rowCount()

        # 데이터 생성 #1.2
        # 첫번째 컬럼 - 체크박스 (QTableWidgetItem)
        chkItem = QtGui.QStandardItem()
        chkItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        chkItem.setCheckState(QtCore.Qt.Unchecked)
        dModel.setItem(rowCnt, 0, chkItem)

        # 썸네일 이미지 추출
        thumnailImg = self.cm.createThumnail_QImage("pixmap", image, 50, 50, 50)

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
            item = QtGui.QStandardItem(dataList[int(colCnt-2)])
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setEditable(False)
            dModel.setItem(rowCnt, colCnt, item)

        # Row Height 설정 (썸네일 이미지 뷰를 위하여 크기조정)
        # 데이터 ROW를 입력한 뒤에 해당 라인의 높이 설정이 가능함 건당 처리 필요
        self.table.setRowHeight(rowCnt, 50)

    @QtCore.Slot(QtWidgets.QTableWidgetItem)
    def on_tableWidget_itemChanged(self, item):
        """ Handles the row's state
        :type item: QTableWidgetItem
        :parameter item: The changed item
        """
        checked = item.checkState() == QtCore.Qt.Checked
        if checked:  # the item gets checked
            print("checked")
        else:  # the item gets unchecked
            print("unChecked")

class ModelCreater(QtCore.QAbstractTableModel):
    """
    MEMO : QAbstractTableModel 오버라이딩 메서드
    """
    def __init__(self, cycles = [[]], headers = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.cycles = cycles
        self.headers = headers
        self.values_checked = []

    def rowCount(self, parent):
        return len(self.cycles)

    def columnCount(self, parent):
        return len(self.cycles[0])

    def flags(self, index):
        fl = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        print("before fl :: {}".format(fl))
        if index.column() == 0:
            print("HIHI")
            fl |= QtCore.Qt.ItemIsUserCheckable
        else:
            print("BYEBYE")
            fl |= QtCore.Qt.ItemIsEditable

        print("after fl :: {}".format(fl))
        return fl

    def data(self, index, role):
        if not index.isValid():
            return
        row = index.row()
        column = index.column()

        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter;

        elif role == QtCore.Qt.CheckStateRole and column==0:
            return QtCore.Qt.Checked if "1" else QtCore.Qt.Unchecked


    def setData(self, index, value, role = QtCore.Qt.EditRole):
        change = False
        row = index.row()
        column = index.column()

        if role == QtCore.Qt.CheckStateRole:
            value =  value != QtCore.Qt.Unchecked
            print("value :: ", value)
            change = True
        if role == QtCore.Qt.EditRole:
            if (column == 1) or (column == 4):
                try:
                    str(value)
                    change = True
                except:
                    print("Not a valid name")
                    change = False
            elif (column == 2):
                try:
                    int(value)
                    change = True
                except:
                    print("Not a valid frame")
                    change = False
            elif (column == 3):
                try:
                    int(value)
                    change = True
                except:
                    print("Not a valid frame")
                    change = False

            elif (column == 5):
                try:
                    int(value)
                    change = True
                except:
                    print("Not a valid version number")
                    change = False
        if change:
            self.dataChanged.emit(row, column)
            return True
        return False

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

    def insertRows(self, position, rows, values = [] , parent = QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position+rows-1)
        self.endInsertRows()
        self.getData()

    def roleNames(self):
        roles = QtCore.QAbstractTableModel.roleNames(self)
        roles["Checked"] = QtCore.Qt.CheckStateRole
        return roles


    def getData(self):
            rows = self.rowCount(1)
            data = []
            for row in range(rows):
                array = []
                for column in range (6):
                    index = self.index(row, column)
                    info = index.data()
                    array.append(info)
                data.append(array)

            dic = {}
            for item in data:
                dic[item[1]]=item

            print("")
            print("data:")
            print('')
            for key in dic:
                print(key, dic[key])



