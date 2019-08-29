from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import cv2,time
import os

"""
# Default Flow Task 
# 1. 로컬업로드 선택 -> 파일업로드 다이얼로그(영상 확장자 선택) -> 해당 업로드 탭 영상 실행(영상 핸들링) ->
# 2. url 업로드 선택 -> url 입력 팝업에 url 입력 후 확인 -> 영상 다운로드(다운 불가시 메시지 팝업) -> 다운 영상 업로드 -> 해당 업로드 탭 영상 실행(영상 핸들링)
# 3. 내려받기 -> 내려받기 파일명 미리보기 팝업('설정탭 저장경로/YYYYMMDD_HHMMSS.확장자(설정탭)' 로 저장하시겠습니까? Y/N)
      -> 로딩바(프로그레스바) 출력 -> 해당 경로로 내려받기 저장(우선은 업로드한 영상을 저장하는 걸로 저장프로세스만 처리)
      -> '내려받기가 완료되었습니다.' 팝업

# common class 공통 변수 설정
    (common)self.uploadPath         : 업로드 경로
    (common)self.uploadUrl          : 업로드 URL 주소
    (common)self.callTabObjNm       : 요청 탭 오브젝트 네임
    (common)self.savePath           : 저장 경로
    (common)self.saveFileNm         : 저장 파일명
    (common)self.saveFmt            : 저장 확장자명
    (common)self.saveResol          : 저장 화질명
    (common)self.saveProgressPer    : 저장 프로그레스 퍼센트
    ...
    ...
"""


class cv_video_player(QThread):
    changePixmap = Signal(QImage)
    changeTime = Signal(int,int)

    def __init__(self,parent=None):
        QThread.__init__(self)
        # self.openVideo()
        self.play = True

    def run(self):
        print("thread start")
        while True:

            if self.play and self.cap.isOpened():
                ret,frame = self.cap.read()
                self.cur_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))

                if ret:
                    rgbImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    convertToQtFormat = QImage(rgbImage.data,rgbImage.shape[1],rgbImage.shape[0],
                                               rgbImage.shape[1] * rgbImage.shape[2],QImage.Format_RGB888)
                    self.changePixmap.emit(convertToQtFormat.copy())
                else:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)
                    self.play = False

            if not self.cur_frame % round(self.fps):
                # print("cur frame : {} total frame : {} ".format(self.cur_frame, self.total_frame))
                # print("fps : {} {}".format(round(self.fps), self.cur_frame / round(self.fps)))
                self.changeTime.emit(int(self.cur_frame / self.fps),int(self.duration))

            time.sleep(0.025)

    def pauseVideo(self):
        self.play = False

    def playVideo(self):
        if not self.isRunning():
            self.start()
        else:
            self.play = True

    def stopVideo(self):
        pass

    def openVideo(self,file_path):
        print(file_path)
        self.cap = cv2.VideoCapture(file_path)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        if file_path:
            self.total_frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
            self.cur_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
            self.duration = self.total_frame / self.fps
            self.minutes = int(self.duration/60)
            self.seconds = int(self.duration%60)
            self.changeTime.emit(int(self.cur_frame / self.fps),int(self.duration))

        # 창을 다시 열었을 때를 위해 upload시에 라벨을 특정 색으로 초기화
        # convertToQtFormat = QImage(rgbImage.data,w,h,bytesPerLine,QImage.Format_RGB888)
        # p = convertToQtFormat.scaled(1280,1040,Qt.KeepAspectRatio)
        # self.changePixmap(p)




    def moveFrame(self, frame):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,frame)


class common(object):
    ## 공통 클래스 변수 설정
    uploadPath = ""
    uploadUrl = ""
    callTabObjNm = ""
    savePath = ""
    saveOptFilePath = ""
    saveUrlPath = ""
    saveFileNm = ""
    saveFmt = ""
    saveResol = ""
    saveProgressPer = ""
    video_player = cv_video_player()

    def __init__(self, ui):
        self.form = ui

    def optUrlSaveFileDir(self):
        """
        TITLE : 설정.URL저장파일경로 정보 설정
        :return: URL PATH String
        """
        self.saveUrlPath = QFileDialog.getExistingDirectory(None, "폴더선택", "/", QFileDialog.ShowDirsOnly)
        print("select folder :: ", self.saveUrlPath)
        return self.saveUrlPath



    def local_upload(self):
        '''
        Title : 로컬 경로의 파일의 경로를 읽어온다
        '''
        self.uploadPath = QFileDialog.getOpenFileName(QFileDialog(),"비디오 선택","","Video Files (*.avi, *.mp4)")[0]
        return self.uploadPath

    def url_upload(self):
        self.uploadUrl = self.create_input_dialog("text","URL 입력창","URL 주소")

    def create_videoPlayer(self):
        self.video_player = cv_video_player()

    def quit_videoPlayer(self):
        self.video_player.cap.release()
        self.video_player.terminate()

    def create_massage_box(self,type,text=""):
        '''
        메시지 박스를 생성
        :param type: 메시지 박스 종류 선택( Confirm, YesNo)
        :param text: 메시지 박스 내용
        :return: type이 YesNo일 때 bool
        '''
        msgbox = QMessageBox()
        msgbox.setText(text)

        if type == "Confirm":
            msgbox.exec_()

        elif type == "YesNo":
            msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            buttonY = msgbox.button(QMessageBox.Yes)
            buttonN = msgbox.button(QMessageBox.No)
            msgbox.exec_()

            # YES pressed
            if msgbox.clickedButton() == buttonY:
                return True
            # NO pressed
            elif msgbox.clickedButton() == buttonN:
                return False

    def create_input_dialog(self,type,title,text):
        """
        input 박스를 생성
        :return:
        """
        if type == "text":
            text,ok = QInputDialog().getText(QInputDialog(),title,text,QLineEdit.Normal)
            return text

    def selectClassImgList(self):
        """
        학습된 검출 대상 리스트 내역을 조회한다
        조회내역은 1.라벨명 2.썸네일이미지경로 및 파일명
        :return: 딕셔너리로 리턴한다
        """
        # 조회부 (조회할 경로는 설정.URL저장파일경로 로 우선 설정한다)
        classListDir = os.listdir(self.opt_lineEdit_urlSaveDir.text())
        jpgFileList = [file for file in classListDir if file.endswith(".jpg")]

        # 딕셔너리 생성부
        resultDict = {}
        for classData in jpgFileList:
            splitData = classData.split(".")
            # DICT 에 KEY(라벨명) : VALUE(경로/파일명.확장자) 형식으로 입력
            resultDict[splitData[0]] = self.opt_lineEdit_urlSaveDir.text()+"/"+classData

        print("resultDict :: ".format(resultDict))

        return resultDict


    def createThumnail_QImage(self, qImage, width, height, radius, antialiasing=True):
        """
        qImage 형식의 img 데이터를 이용하여 width/height 크기로
        원형 썸네일 QPixmap 생성 후 Label에 입력하여 리턴
        :param qImage:
        :param width:
        :param height:
        :return: img in Label(QPixmap)
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

        return resultLabel

    def createThumnail_filePath(self, fullPath, width, height, radius, antialiasing=True):
        """
        filePath 형식의 img 데이터를 이용하여 width/height 크기로
        원형 썸네일 QPixmap 생성 후 Label에 입력하여 리턴
        :param fullPath: 경로/파일명.확장자
        :param width: 넓이(썸네일이미지)
        :param height: 높이(썸네일이미지)
        :return: img in Label(QPixmap)
        """

        resultLabel = QtWidgets.QLabel()
        resultLabel.setMaximumSize(width, height)
        resultLabel.setMinimumSize(width, height)
        target = QtGui.QPixmap(resultLabel.size())
        target.fill(QtCore.Qt.transparent)

        # imgData = QtGui.QPixmap(QtGui.QImage(qImage))\
        #     .scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

        imgData = QtGui.QPixmap(fullPath).scaled(width, height)
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

        return resultLabel

    '''
    - 로컬 업로드 : local 경로에 있는 영상을 읽어온다.(opencv 등을 이용해 읽어옴)
    - url 업로드 : url 경로(youtube 등)의 영상의 읽어온다. ( pytube 등을 이용해 읽어옴)
      ## mediaUpload(type, addr):   
         type : local/url
         addr : address


    - url 다운로드 저장 : url 업로드를 통해 받아온 영상을 저장, 경로는 설정파일에서 설정 가능 
      ## saveStream(frame, ...):


   QT : QMediaPlayer player / realtime
   opencv : 
    - 업로드 영상처리 (media plyaer) : 업로드를 통해 받은 영상 데이터 핸들링(재생, 일시정지, 정지 등)
        - play()
        - stop()
        - pause()
        - 현재 플레이 시간    ( opencv 는 프레임 시간 계산 필요 )

   - (1)검출 대상 리스트 조회 : 총 라벨 및 학습 썸네일 정보 조회
      List getClassList():
         """
            TITLE   :   학습된 클래스 리스트를 반환한다
            MEMO   :   
            return   :   list
         """
         pass

    - (2)검출 대상 리스트 생성 : 특정 경로에 있는 대상 정보와 대상의 이미지를 읽어와 widget을 추가한다
      addClass(getClassList, objName):
         """
            TITLE   :   학습된 클래스 리스트를 인자로 받아 objName에 해당하는 layer에 입력한다
         """
         pass

    - 영상 검출
      (1) mediaExtProc(objName):
            """
               #   TITLE   :   검출한 결과만 리턴
               #   NOTE   :
            """
            player
            while{
               if(20FP)
               frame = data

               if flag == ext
                  {

                  }
               else
                  afc.aksd()


            }
            pass


    - 검출 결과 내역 생성 : 영상 검출 결과와 추가 정보들을 리스트로 생성


    - 설정 데이터 로드 : 설정값을 읽어 온다.
    - 설정 데이터 확인 : 추출, 오토포커싱 이전에 설정값이 세팅되어 있는지 확인
    - 학습된 모델 


    '''


"""
   <AddMethodList>

   getAttr(objName):
      """
# TITLE   :   오브젝트명에 해당하는 값 조회
# NOTE   :
"""
pass

setAttr(objName, value):
"""
# TITLE   :   오브젝트명에 대상 값 삽입
# NOTE   :
"""
pass



"""




