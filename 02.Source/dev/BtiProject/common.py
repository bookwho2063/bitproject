from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from time import sleep
import cv2,time
import os, re, datetime
from autofocus import Autofocus

# img face recognition test
import dlib
import matplotlib.pyplot as plt
import sys
from skimage import io      #pip install scikit-image
import cv2
from keras.models import load_model
import FacenetInKeras
import facenetRealTime
import openfaceRealTime

class cv_video_player(QThread):
    changePixmap = Signal(QImage)
    changeTime = Signal(int,int)
    changeExtFrame = Signal(QImage,list)
    setTotalTime = Signal(int)

    # changeAfcFrame = Signal(QImage,QRect)

    def __init__(self, afc =None, parent=None):
        QThread.__init__(self)
        # self.openVideo()
        self.play = True
        self.cap = cv2.VideoCapture()
        self.running = True
        self.fps = 0

        # 추출 작업 0 : 시작 전  1 : 작업 중  2 : 완료
        self.ext_state = 0
        self.afc_state = 0
        self.buffertime = 3
        self.current_workingFrame = 0

        # afc 클래스
        self.afc = Autofocus()

        # 얼굴 검출 관련 클래스 설정
        self.usedFaceStateNm = "openface"        # facenet / facenet2 / openface
        self.model = None
        self.initModel()

    def initModel(self):
        if self.usedFaceStateNm == 'facenet':
            self.model = FacenetInKeras.facenetInKeras()
            print("========== facenet model build")

        elif self.usedFaceStateNm == 'facenet2':
            self.model = facenetRealTime.facenetRealtime()
            self.model.defaultSetFacenet2()
            print("========== facenet2 model build")

        elif self.usedFaceStateNm == 'openface':
            self.model = openfaceRealTime.openfaceRealTime()
            self.model.defaultSetOpenface()
            print("========== openface model build")

    def run(self):

        # 비디오 업로드 시 모델 업로드 처리
        if self.usedFaceStateNm == "facenet":
            self.model.faceModel = load_model('./00.Resource/model/facenet_keras.h5')

        while self.running:
            start_time =time.time()
            convertToQtFormat = ""
            rgbImage = ""
            if self.play and self.cap.isOpened():
                # print("시작 시간 : ", start_time)
                self.cur_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
                ret,frame = self.cap.read()

                if ret:
                    # 재생 시간 정보 업데이트 emit
                    if not self.cur_frame % self.fps:
                        self.changeTime.emit(int(self.cur_frame / self.fps), int(self.duration))

                    # 프레임이미지 컨버팅 (영상내 얼굴 검출을 위함)
                    rgbImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], rgbImage.shape[1] * rgbImage.shape[2], QImage.Format_RGB888)

                    # 영상검출탭 검출 수행
                    if self.ext_state and self.cur_frame % (self.fps * self.buffertime) == 0 and self.cur_frame > self.current_workingFrame:
                        self.current_workingFrame = self.cur_frame

                        # 검출수행
                        rgbImage, resultData = self.extractFaceOrder(rgbImage)

                        # 결과 데이터가 존재할 경우에만 결과목록에 출력
                        if len(resultData) > 0:
                            # 결과 데이터 형태
                            # list[{dict}, ....{dict}, cur_frame]
                            resultData.append(str(self.cur_frame))
                            self.changeExtFrame.emit(convertToQtFormat.copy(), resultData)

                    # 오토포커싱탭 검출 수행
                    if self.afc_state == 1:
                        # if self.afc_state and self.cur_frame > self.current_workingFrame:
                        self.current_workingFrame = self.cur_frame
                        if self.cur_frame == 1:
                            self.current_workingFrame = 0

                        ## TODO :: COPY HERE EXTRACT
                        # 검출수행
                        rgbImage, resultData = self.extractFaceOrder(rgbImage)

                        # self.afc.extract_afcVideo(img = frame, current_workingFrame=self.current_workingFrame )
                        x, y, width, height = self.afc.extract_afcVideo(current_workingFrame=self.current_workingFrame, resultList=resultData)

                        self.afc.changePixmap.emit(convertToQtFormat.copy(), QRect(x, y, width, height))
                    elif self.afc_state == 2:
                        x, y, width, height = self.afc.play_afcResult(playFrame=self.cur_frame)

                    self.changePixmap.emit(convertToQtFormat.copy())
                    # print("self.cur_frame % self.fps :: ", self.cur_frame % self.fps)
                else:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)
                    self.play = False
                # print("종료 시간 : ",time.time())
            time.sleep(self.getWaitTime(start_time,self.fps)*0.9)

    def extractFaceOrder(self, rgbImage):
        """
        입력받은 이미지를 이용하여 각기다른 검증 모델을 수행한다
        :param rgbImage:
        :return:
        """
        if str(self.usedFaceStateNm) == "facenet":
            # keras_facenet #1
            rgbImage, resultData = self.faceRecog_keras_facenet(rgbImage)
        elif str(self.usedFaceStateNm) == "facenet2":
            # keras_facenet #2
            rgbImage, resultData = self.faceRecog_keras_facenet2(rgbImage)
        elif str(self.usedFaceStateNm) == "openface":
            # openface run
            rgbImage, resultData = self.faceRecog_keras_openface(rgbImage)

        return rgbImage, resultData

    def faceRecog_keras_facenet(self, rgbImage):
        """
        # keras를 이용한 facenet 얼굴 검출 처리 #1
        :param rgbImage:
        :return: rgbImage
        """
        # print("======================검출을 수행합니다.(faceRecog_keras_facenet)")
        faceDetResults, faceImgArr = self.model.extract_face(rgbImage)

        resultData = []

        # 이미지 내 검출된 얼굴 갯수만큼 루프
        for idx in range(len(faceDetResults)):
            dataDict = dict()
            # 검출된 얼굴박스 하나에 대하여 임베딩 처리
            imgToEmd = self.model.getEmbedding(faceImgArr[idx])
            # 임베딩 된 얼굴데이터의 검증 수행
            predictNm, predictPer = self.model.predictImg(imgToEmd)

            # predict 결과치가 특정 퍼센트 이상일 때만 박스 생성
            if 65 < int(predictPer):
                x, y, w, h = faceDetResults[idx]['box']
                # print("left : {} _ top : {} _ right : {} _ bottom : {}".format(x, y, w, h))

                # bug fix
                x, y = abs(x), abs(y)
                x2, y2 = x + w, y + h

                # extract the face
                # faceImg = rgbImage[y:y2, x:x2]
                # rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.rectangle(rgbImage, (x, y), (x2, y2), (0, 255, 0), 2)
                cv2.putText(rgbImage, str(predictNm), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                dataDict['x'] = x
                dataDict['y'] = y
                dataDict['w'] = x2
                dataDict['h'] = y2
                dataDict['labelname'] = str(predictNm)
                dataDict['percent'] = str(predictPer)
                resultData.append(dataDict)
            else:
                continue

        # 박스 처리된 이미지 저장
        # cv2.imwrite("./twice_{}frame.jpg".format(self.cur_frame), rgbImage)

        return rgbImage

    def faceRecog_keras_facenet2(self, rgbImage):
        """
        facenet 2 run
        :param rgbImage:
        :return:rgbImage
        """
        # print("======================검출을 수행합니다.(faceRecog_keras_facenet)")
        rgbImage, resultData = self.model.runFacenet(rgbImage)
        # rgbImage = self.model.run(rgbImage)
        return rgbImage, resultData

    def faceRecog_keras_openface(self, rgbImage):
        """
        openface run
        :param rgbImage:
        :return:
        """
        # print("======================검출을 수행합니다.(faceRecog_keras_openface)")
        rgbImage, resultData = self.model.runPredictOpenface(rgbImage)
        return rgbImage, resultData

    def pauseVideo(self):
        self.play = False

    def playVideo(self):
        if not self.cap.isOpened():
            return

        if not self.isRunning():
            self.running = True
            self.start()

        self.play = True

    def stopVideo(self):
        self.running = False
        self.cap.release()
        self.ext_state = 0
        self.afc_state = 0
        self.current_workingFrame = 0
        self.changeTime.emit(0,0)

    def openVideo(self,file_path):
        self.cap = cv2.VideoCapture(file_path)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        if self.cap.isOpened():
            self.total_frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
            self.cur_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            self.fps = round(self.cap.get(cv2.CAP_PROP_FPS))
            self.duration = self.total_frame / self.fps
            self.minutes = int(self.duration/60)
            self.seconds = int(self.duration%60)
            self.changeTime.emit(int(self.cur_frame / self.fps),int(self.duration))
            self.setTotalTime.emit(int(self.total_frame))
            self.moveFrame(0)

    def moveFrame(self, frame_num):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        ret, frame = self.cap.read()
        self.cur_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))

        if ret:
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                       rgbImage.shape[1] * rgbImage.shape[2], QImage.Format_RGB888)
            self.changePixmap.emit(convertToQtFormat.copy())
            self.changeTime.emit(int(self.cur_frame / self.fps), int(self.duration))
            self.cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)

    def initScreen(self):
        black_image = QImage(1920,1280, QImage.Format_Indexed8)
        black_image.fill(QtGui.qRgb(0,0,0))
        self.changePixmap.emit(black_image.copy())

    def getWaitTime(self, start_time, fps):
        wait_time = 1 / fps - time.time() + start_time
        return wait_time if wait_time > 0 else 0
    def isPlaying(self):
        return self.play

    # def play_Demo(self):
    #     print("thread start")
    #     while True:
    #
    #         if self.play and self.cap.isOpened():
    #             ret,frame = self.cap.read()
    #             self.cur_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
    #
    #             if ret:
    #                 rgbImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #                 convertToQtFormat = QImage(rgbImage.data,rgbImage.shape[1],rgbImage.shape[0],
    #                                            rgbImage.shape[1] * rgbImage.shape[2],QImage.Format_RGB888)
    #                 self.changePixmap.emit(convertToQtFormat.copy())
    #             else:
    #                 self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    #                 self.play = False
    #
    #         if not self.cur_frame % round(self.fps):
    #             # print("cur frame : {} total frame : {} ".format(self.cur_frame, self.total_frame))
    #             # print("fps : {} {}".format(round(self.fps), self.cur_frame / round(self.fps)))
    #             self.changeTime.emit(int(self.cur_frame / self.fps),int(self.duration))
    #
    #         time.sleep(0.025)


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

    def __init__(self, ui):
        self.form = ui
        self.video_player = cv_video_player(ui.afc)
        self.youtubeUrlValidCheck = re.compile(
            "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$")


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
        path =  QFileDialog.getOpenFileName(QFileDialog(),"비디오 선택","","Video Files (*.avi *.mp4)")[0]
        print(path)
        if path == "":
            return path
        else:
            self.uploadPath = path
            return self.uploadPath


    def url_upload(self):
        self.uploadUrl = self.create_input_dialog("text","URL 입력창","URL 주소")
        return self.uploadUrl

    def quit_videoPlayer(self):
        self.video_player.stopVideo()
        self.video_player.initScreen()

    def create_massage_box(self, type, text=""):
        '''
        메시지 박스를 생성
        :param type: 메시지 박스 종류 선택( Confirm, YesNo)
        :param text: 메시지 박스 내용
        :return: type이 YesNo일 때 bool
        '''
        msgbox = QMessageBox()
        msgbox.setText(text)

        if type == "Confirm" or type == "confirm" or type == "CONFIRM":
            msgbox.setStandardButtons(QMessageBox.Yes)
            msgbox.setWindowTitle("알림")
            buttonY = msgbox.button(QMessageBox.Yes)
            msgbox.exec_()

            # YES pressed
            if msgbox.clickedButton() == buttonY:
                return True

        elif type == "YesNo" or type == "yesno" or type == "YESNO":
            msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgbox.setWindowTitle("선택")
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
        # 조회부
        # classListDir = os.listdir(self.opt_lineEdit_urlSaveDir.text())
        classListDir = os.listdir("./LabelList")
        jpgFileList = [file for file in classListDir if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")
                       or file.endswith(".JPG") or file.endswith(".JPEG") or file.endswith(".PNG")]

        # 딕셔너리 생성부
        resultDict = {}
        for classData in jpgFileList:
            splitData = classData.split(".")
            # DICT 에 KEY(라벨명) : VALUE(경로/파일명.확장자) 형식으로 라벨 데이터 설정
            resultDict[splitData[0]] = "./LabelList/" + classData

        return resultDict


    def createThumnail_QImage(self, resultType, qImage, width, height, radius, antialiasing=True):
        """
        qImage 형식의 img 데이터를 이용하여 width/height 크기로
        원형 썸네일 QPixmap 생성 후 Label에 입력하여 리턴
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

        imgData = QtGui.QPixmap(QImage(qImage)).scaled(width, height)
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

    def createThumnail_filePath(self, returnType, fullPath, width, height, radius, antialiasing=True):
        """
        filePath 형식의 img 데이터를 이용하여 width/height 크기로
        원형 썸네일 QPixmap 생성 후 Label에 입력하여 리턴
        :param returnType: label, pixmap
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

        imgData = QtGui.QPixmap(fullPath).scaled(QSize(width, height), QtCore.Qt.KeepAspectRatio)
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
        painter.end()
        resultLabel.setPixmap(target)

        if returnType is "label" or returnType is "LABEL":
            return resultLabel
        elif returnType is "pixmap" or returnType is "PIXMAP":
            return target


    def createTargetClassList(self):
        """
        # 검출 대상 클래스 썸네일 이미지 및 목록을 생성하여 출력한다
        :return: bool (Class Create Success boolean)

        Step.
        this->selectClassImgList(self)->
        loop->createThumnail_filePath()->CreateClassList in
        """
        # 학습 대상 클래스 리스트 불러오기
        self.classImgCount = 0
        self.classListDict = self.selectClassImgList()

        for classListDictKey, classListDictValue in self.classListDict.items():
            # 썸네일 생성
            thumbnailImgInExt = self.createThumnail_filePath("pixmap", os.path.abspath(classListDictValue), 50, 50, 80)
            thumbnailImgInAfc = self.createThumnail_filePath("pixmap", os.path.abspath(classListDictValue), 50, 50, 80)

            # VLayout을 생성하여 이미지 라벨 및 이름라벨 입력
            extImgItem = QLabel()
            extImgItem.setPixmap(thumbnailImgInExt)

            vBoxExt = QVBoxLayout()
            vBoxExt.setAlignment(Qt.AlignCenter)
            vBoxExt.addWidget(extImgItem)
            vBoxExt.addWidget(QLabel(str(classListDictKey), alignment=Qt.AlignHCenter))

            afcImgItem = QLabel()
            afcImgItem.setPixmap(thumbnailImgInAfc)
            vBoxAfc = QVBoxLayout()
            vBoxAfc.setAlignment(Qt.AlignCenter)
            vBoxAfc.addWidget(afcImgItem)
            vBoxAfc.addWidget(QLabel(str(classListDictKey), alignment=Qt.AlignHCenter))

            # Layout Widget 생성
            qWExt = QWidget()
            qWAfc = QWidget()
            qWExt.setLayout(vBoxExt)
            qWAfc.setLayout(vBoxAfc)

            # 레이아웃(썸네일+이름라벨) 테이블 적용
            self.form.ext_tableWidget_classList.setCellWidget(0, int(self.classImgCount), qWExt)
            self.form.afc_tableWidget_classList.setCellWidget(0, int(self.classImgCount), qWAfc)
            self.classImgCount = self.classImgCount + 1




    def downloadYouTubeUrl(self, url):
        """
        youtube-dl 을 사용하여 URL 영상 다운로드
        :param url:
        :return:
        """
        if self.youtubeUrlValidCheck.match(url) is None:
            self.create_massage_box("confirm","URL 경로가 잘못됐습니다.\nURL을 확인해주세요.")
            return ""

        import youtube_dl

        # ydl_opts = {
        #     'format': 'bestaudio/best',
        #     'postprocessors': [{
        #         'key': 'FFmpegExtractAudio',
        #         'preferredcodec': 'mp3',
        #         'preferredquality': '192',
        #     }]
        # }

        # ffmpeg 설치법
        # git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
        # https://ffmpeg.zeranoe.com/builds/


        ydl_opts = {
            'outtmpl': './videoList/%(title)s.%(ext)s'
        }


        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            infoList = ydl.extract_info("{}".format(url))
            temp = infoList.get("title",None)
            title = temp.replace("/","_")
            # format = infoList.get("format", None)
            ext = infoList.get("ext",None)

            print("format :{} ".format(format))
            print("ext :{} ".format(ext))

            if title is not None or title is not "":
                if ydl.download([str(url)]) == 1:
                    self.create_massage_box("confirm","URL 영상 다운로드에 실패하였습니다.\nURL을 확인해주세요.")
                else:
                    # self.create_massage_box("confirm", "URL 영상을 다운로드 하였습니다.")
                    targetPath = os.path.abspath("./videoList")
                    # ext = self.fileFormatTracker(targetPath, title)
                    oPath = targetPath + "/" + title + "." + ext
                    return oPath

                # 경로 및 타이틀 정보를 리턴해서 영상재생 객체에 던져야함
                # 경로 + / + 파일명 + ".mp4"


                ## 경로 조정 해봐라 고정 경로주니까 잘되네
                ## 경로 조합하는게 잘못되서 위에꺼 안맞는듯

                # oPath = "D:/박준욱/## 00.BIT_PROJECT/9999.github/bitproject/02.Source/dev/BtiProject/videoList/"+title+".mp4"

    def openVideoWriter(self,file_path,format,size=""):
        '''
        VideoWriter를 생성
        :param file_path: 저장할 파일의 경로 및 파일이름
        :param size: 저장할 비디오의 사이즈(width, height)
        :param format: 저장할 비디오의 포맷 종류(avi, mp4 지원)
        '''
        file_name = os.path.splitext(file_path)[0] + format

        if format == ".avi":
            fourcc = cv2.VideoWriter_fourcc("D","I","V","X")
        elif format == ".mp4":
            fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

        if size == "":
            size = (int(self.video_player.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(self.video_player.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        print("file name : {}".format(file_name))
        print("fps : {}".format(self.video_player.fps))
        print(fourcc)
        print("size : {}".format(size))
        self.out = cv2.VideoWriter(file_name,fourcc,self.video_player.fps,size)

    def saveVideo(self, resultList):
        for result in resultList:
            self.video_player.cap.set(cv2.CAP_PROP_POS_FRAMES, int(result[-1]))
            for i in range(self.video_player.buffertime * self.video_player.fps):
                ref, frame = self.video_player.cap.read()
                if ref:
                    self.out.write(frame)
                else:
                    break

    def saveCoordFile(self,resultList,file_name,type='CSV',):

        if type == 'CSV':
            import csv
            resultList[0][0]['frame_num'] = None
            keys = resultList[0][0].keys()
            print(keys)
            with open(file_name,'wt',newline='') as output_file:
                dict_writer = csv.DictWriter(output_file,keys)
                dict_writer.writeheader()
                for result in resultList:
                    result = [dict(item,**{'frame_num': result[-1]}) for item in result[:-1]]
                    dict_writer.writerows(result)
        elif type == 'JSON':
            import json
            with open(file_name,'w') as output_file:
                for result in resultList:
                    result = [dict(item,**{'frame_num': result[-1]}) for item in result[:-1]]
                    json.dump(result,output_file,ensure_ascii=False,indent="\t")

    def closeVideoWriter(self):
        print("다운로드 완료")
        self.out.release()

    def downloadVideo(self, frameList):
        """
        frame 번호 순서대로 write 처리한다.
        :param frameList:
        :return:
        """
        cap = cv2.VideoCapture("")
        fcc = cv2.VideoWriter_fourcc('D','I','V','X')
        fps = 60
        width = 640
        height = 480
        out = cv2.VideoWriter("경로", fcc, fps, (width, height))

        while True:
            ret, frame = cap.read()
            cur_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

            if cur_frame in frameList:
                out.write(frame)

            if (cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT)):
                break

        out.release()
        cap.release()

    def downloadCoordList(self, saveFileNm, coordList, type="csv"):
        """
        검출 좌표 결과 파일 다운로드
            :param saveFileNm: 확장자를 제외한 저장 파일명 (Default 는 영상파일명)
            :param coordList: 좌표 리스트(X,Y 조합이므로 홀수가 될 수 없음)
            :param type: 저장 확장자 명 (CSV, JSON 지원)
            :return: bool
        """
        import platform
        # OS 별 File Seperator 설정
        pSysNm = platform.system()
        seperator = ""
        if pSysNm is "Windows":
            seperator = "/"
        elif pSysNm is "Darwin" or pSysNm is "Linux":
            seperator = "\\"

        # 설정 > 내려받기 저장 경로 추출
        saveFileDir = self.form.opt_lineEdit_saveDir.text()

        # DIR Validation Check
        if saveFileDir == "" or saveFileDir == None or saveFileDir == "업로드 경로":
            self.create_massage_box("Confirm", "'내려받기 저장 경로' 가 지정되지 않았습니다.\n 설정 > 공통 옵션 설정 > 내려받기 저장 경로 를 지정해주세요.")
            return False
        else:
            saveFullPath = saveFileDir + seperator + saveFileNm + "." + type

            # File Open
            with open(saveFullPath, mode='wt', encoding='utf-8') as saveFile:
                # Type = CSV
                if type is "csv" or type is "CSV":
                    for coordData in coordList:
                        if coordData is coordList[-1]:
                            saveFile.write(coordData)
                        else:
                            saveFile.write(coordData+",")
                # Type = JSON
                elif type is "json" or type is "JSON":
                    import json
                    from collections import OrderedDict
                    # JSON 데이터 입력 변수
                    jsonData = OrderedDict()

                    # if coordList = 10 -> 5 , rowCnt 0~5
                    for rowCnt in range(int(len(coordList) / 2)):
                        targetCnt = int(rowCnt+rowCnt)
                        jsonData[str(rowCnt)] = {'X':str(coordList[int(targetCnt)]), 'Y':str(coordList[int(targetCnt+1)])}

                    # JSON 덤프 저장
                    json.dump(jsonData, saveFile, ensure_ascii=False, indent="\t")
                else:
                    self.create_massage_box("confirm", "해당 확장자 형식은 지원하지 않습니다. ({})".format(type))

                self.create_massage_box("confirm", "{} 에 저장을 완료 하였습니다.".format(saveFullPath))
                saveFile.close()

    def getMicrotimes(self):
        """
        UTC 시간을 리턴한다
        다운로드 영상 및 좌표 파일의 파일명으로 활용
        :return:
        """
        return round(datetime.datetime.utcnow().timestamp() * 1000)
