from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import cv2,time


class Autofocus(QThread):
    changePixmap = Signal(QImage,QRect)

    def __init__(self):
        QThread.__init__(self)
        self.current_frame = 0
        # self.play = True
        self.afc_state = 0  # 0 :검출 시작 전 1: 검출 중 2. 검출 완료
        self.afc_process = 0
        self.afc_play = 0
        self.afc_save = 0
        self.afc_coordList = []

        # 테스트 변수
        self.list_index = 0
        self.list_coord = [(405,77,500,430),(405,77,250,215),(405,77,418,360),(405,77,174,150)]

    def setUp(self,ui):
        self.video_player = ui.cm.video_player
        self.afc_width,self.afc_height = ui.opt.get_coord()
        self.filepath = ui.cm.uploadPath
        self.cap = cv2.VideoCapture(self.filepath)
        # self.class_num = class_num

    def run(self):
        self.afc_process = 1

        while True:

            if self.afc_process:
                if self.afc_state == 0 or self.afc_state == 1:
                    self.extract_afcVideo()

            # if self.afc_save:
            #     pass
            #
            # if self.afc_play:
            #     pass

            time.sleep(1)

    def search_afcSection(self,ui):
        return self.afc_width,self.afc_height

    # def detect_centerCoord(self, calss_num, frame):
    def detect_centerCoord(self):
        '''
        프레임에서 대상이 있는지 확인하고 있을 때 대상의 얼굴 좌표를 리턴한다
        :param calss_num:
        :param frame:
        :return: (x, y, width, height)
        '''
        self.list_index = (self.list_index + 1) % 4
        return self.list_coord[self.list_index]

    # 네트워크를 통해 추출된 좌표가 나왔을 때 그것을 기준으로 구현
    # def make_afcSection(self, centerCoord):
    #     '''
    #     얼굴의 좌표를 기준으로 포커싱할 영역을 결정한다.
    #     :param centerCoord: face 중심점 좌표 및 크기
    #     :return: x,y,widht,height
    #     '''
    #     x, y, width, height = centerCoord
    #

    def extract_afcVideo(self):
        '''
        추출된 이미지를 재생하고 저장한다.
        :return:
        '''
        self.afc_state = 1
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,self.current_frame)

        while self.afc_process:

            if not self.current_frame % 30:
                index = int(self.current_frame / 30)
                self.afc_coordList.append(self.detect_centerCoord())
                x,y,width,height = self.afc_coordList[index]

                print("index : {} value : {}".format(index,self.afc_coordList[index]))

            ret,frame = self.cap.read()
            self.current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))

            if ret:
                rgbImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data,rgbImage.shape[1],rgbImage.shape[0],
                                           rgbImage.shape[1] * rgbImage.shape[2],QImage.Format_RGB888)
                self.changePixmap.emit(convertToQtFormat.copy(),QRect(x,y,width,height))
            else:
                self.afc_state = 2
                self.afc_process = 0
                break
            time.sleep(0.03)

    def play_afcResult(self):
        '''
        추출된 영상을 플레이어에서 재생한다.
        :return:
        '''
        self.afc_play = 1
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    def save_coordFile(self,type):
        '''
        오토포커싱된 좌표를 파일로 저장한다.
        :param type:
        :return:
        '''
        pass

    def save_afcVideoFile(self,extension,resolution,result):
        '''
        오토포커싱된 영상을 파일로 저장한다.
        :param extension:
        :param resolution:
        :param result:
        :return:
        '''
        pass

    # def pause_afc(self):
    #     self.play = False
    #
    # def start_afc(self):
    #     self.play = True

    def search_afcResult(self,file_name):
        return self.afc_state


'''
1. 검출 시작 클릭 -> button(로컬업로드, URL 업로드, 영상 내려받기, 미디어 control, 검출시작, 검출 대상 리스트(추출 도중 변경 가능시에는 제외)) 사용 불가 
    -> 탭 이동시 경고창 팝업(현재 진행중인 검출 결과가 사라집니다. 중지하겠습니까? Y/N)
    -> before 첫 프레임 부터 play -> after는 포커싱 되는 즉시 결과를 play
    -> 포커싱 완료 후 비활성화된 button(처음 시작시 비활성화된 버튼, after player 미디어 ocntrol 버튼)을 다시 활성화, '포커싱이 완료되었습니다' 팝업 

2. 검출시작 -> 이전 결과 확인 -> 결과가 있으면 이전 결과를 불러오겠습니까? Y/N 팝업창 -> N일 때 1번 과정과 동일
            -> Y일 때 이전 결과 불러오기


2. 공통 변수
    - self.afc_width : 설정의 넓이값
    - self.afc_height : 설정의 높이값
    - self.selected_class : 선택된 클래스
    - self.uploadPath : common의 uploadpath외 동일
    - self.predict : coommon class or facenet_model class

3. 기능
    - 오토 포커싱 영역 조회 : 설정탭에서 설정한 박스의 크기를 조회한다.
    search_afcSection()
    """
        TITLE   :  설정탭에서 지전한 오토포커싱 박스의 크기를  리턴한다. 
        MEMO   :   
        return   :   afc_width, afc_height
    """

    - 오토포커싱 영역 중심점 좌표 검출 : 입력받은 프레임에서 클래스의 중심 좌표와 width,height를 검출한다. 
       result : x_center,y_center,width, height 좌표를 리턴한다.
       ㄴ 학습된 모델에서 frame에서 예측된 결과를 받는다.
       ㄴ 예측된 결과와 설정된 width, height를 바탕으로 오토포커싱 결과를 리턴한다.

       detect_centerCoord(class, frame)

    - make_afcCoord(x_center,y_center,width_center,height_center, afc_width,afc_height)


    - 오토포커싱 영상 추출 : 검출된 결과를 이용하여 오토포커싱된 영상을 추출 
        ㄴ 영상 추출 도중 영상 재생을 위해서 siganl을 이용하여 QImage, QRect(추출 결과) emit
        ㄴ 검출 도중 play 방안
           방안 1. 검출 중에는 현재 Thread에서 before, after player를 모두 play(이와 같이하면 정상속도로 play 되지는 않더라도 동시에 play 가능
           방안 2. before 영상은 common의 player thread에서 재생, auto focusing 영상은 현 autofuocus class에서 재생. 
                이 때 영상간의 속도 차이를 줄일 수 있는 방안을 따로 생각해야 함

        extract_afcVideo(class, video_file)

    - 결과 영상 재생 : 오토포커싱 결과를 재생한다. 처음 이전 

    - 미디어 플레이어 간 버튼 액션 공유
       ㄴ 공유하기 전에 영상에 대한 오토 포커싱이 완료되어야 한다.
       ㄴ 공유하기 위해서는 같은 slot에 connect


    - 오토 포커싱 결과 저장 : 추출된 결과를 기반으로 
        afc_result_save(video_name, result)
        result : frame_num, x_pos, y_pos, width, height

    - 오토 포커싱 결과 조회 : 추출 시작 전 이전 추출 결과가 있는지 확인 있을 시 팝업창을 띄워 이전 결과를 불러올지 선택

    - 오토포커싱 추출 클래스 변경 : 재생중 가능할 때 구현( 필요한 기능 구현 완료 후 구현). 추출 대상 클래스 value만 signal을 이용하여 변경, 
        ㄴ추출 과정 중 변경에서 crash 발생시 mutex 등 이용
'''