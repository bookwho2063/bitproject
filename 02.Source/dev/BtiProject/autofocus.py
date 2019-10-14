from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import cv2,time,os


# class Autofocus(QThread):
#     changePixmap = Signal(QImage,QRect)
#
#     def __init__(self):
#         QThread.__init__(self)
#         self.current_workingFrame = 0
#         self.current_playingFrame = 0
#         self.current_savingFrame = 0
#         # self.play = True
#         self.afc_state = 0  # 0 :검출 시작 전 1: 검출 중 2. 검출 완료
#         self.afc_process = 0
#         self.afc_play = 0
#         self.afc_save = 0
#         self.afc_coordList = []  # 검출 좌표 리스트
#
#         self.running = True
#         # self.cap = cv2.VideoCapture()
#
#         # 테스트 변수
#         self.list_index = 0
#         self.list_coord = [(650,330,360,720),(720,405,300,600),(650,330,360,720),(800,500,240,480),(1000,525,150,300)]
#
#     def quit_afcProcess(self):
#         self.current_workingFrame = 0
#         self.current_playingFrame = 0
#         self.current_savingFrame = 0
#
#         self.afc_state = 0
#         self.afc_process = 0
#         self.afc_play = 0
#         self.afc_coordList = []  # 검출 좌표 리스트
#
#         self.running = False
#
#         # if self.cap.isOpened():
#         #     self.cap.release()
#
#     def setUp(self,ui):
#         self.video_player = ui.cm.video_player
#
#         # 추출할 크기
#         self.afc_width,self.afc_height = ui.opt.get_coord()
#
#         # self.filepath = ui.cm.uploadPath
#         # self.cap.open(self.filepath)
#         self.afc_extFrameRate = ui.cm.video_player.fps
#
#         # self.class_num = class_num
#
#
#     def run(self):
#         '''
#         오토포커싱 쓰레드의 실행 함수(검출, 영상 재생, 저장
#         :return:
#         '''
#         self.afc_process = 1
#
#         while self.running:
#
#             if self.afc_process:
#                 if not self.afc_state == 2 :
#                     self.extract_afcVideo()
#                 else:
#                     print("검출 작업이 완료되었습니다.")
#                     self.afc_process = 0
#
#             if self.afc_play and self.afc_state == 2:
#                 self.play_afcResult()
#
#             # if self.afc_save:
#             #     pass
#
#             time.sleep(1)
#
#     def search_afcSection(self,index):
#         '''
#         프레임에 해당하는 영역 좌표를 리턴한다.
#         :param ui:
#         :return:
#         '''
#         if index < len(self.afc_coordList):
#             return self.afc_coordList[index]
#         else:
#             return -1
#
#     # def detect_centerCoord(self, calss_num, frame):
#     def detect_centerCoord(self):
#         '''
#         딥러닝 모델을 이용하여 프레임에서 대상이 있는지 확인하고 있을 때 대상의 얼굴 좌표를 반환한다.
#         :param calss_num:
#         :param frame:
#         :return: (x, y, width, height)
#         '''
#         pass
#
#     # 네트워크를 통해 추출된 좌표가 나왔을 때 그것을 기준으로 구현
#     def make_afcSection(self,centerCoord=0):
#         '''
#         얼굴의 좌표를 기준으로 포커싱할 추출 영역을 결정한다.
#         :param centerCoord: face 중심점 좌표 및 크기
#         :return: x,y,widht,height
#         '''
#         self.list_index = (self.list_index + 1) % 4
#         return self.list_coord[self.list_index]
#
#     def extract_afcVideo(self, img, current_workingFrame):
#         '''
#         추출된 이미지를 재생하고 영역 좌표를 리스트로 저장한다.
#         :param img : 오토포커싱할 img
#         :param current_workingFrame : 현재 프레임이 작업되고 있는 프레임 number
#         :return: crop할 좌표
#         '''
#         # self.afc_state = 1
#         # self.cap.set(cv2.CAP_PROP_POS_FRAMES,self.current_workingFrame)
#         # # x = 0
#         # # y = 0
#         # # width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#         # # height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#         #
#         # while self.afc_process:
#         #
#         #     if not self.current_workingFrame % self.afc_extFrameRate:
#         #         index = int(self.current_workingFrame / self.afc_extFrameRate)
#         #         self.afc_coordList.append(self.make_afcSection())
#         #
#         #         if index == 0:
#         #             cur_coord = self.afc_coordList[index]
#         #             dst_coord = self.afc_coordList[index]
#         #         else:
#         #             dst_coord = self.afc_coordList[index]
#         #
#         #         print("frame : {} index : {} value : {}".format(self.current_workingFrame,index,
#         #                                                         self.afc_coordList[index]))
#         #
#         #     cur_coord = self.smooth_movedSection(cur_coord,dst_coord,self.current_workingFrame % self.afc_extFrameRate,
#         #                                          self.afc_extFrameRate)
#         #     x,y,width,height = cur_coord
#         #
#         #     # print("current coordinate", cur_coord)
#         #
#         #     ret,frame = self.cap.read()
#         #     self.current_workingFrame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
#         #     print("current_workingFrame", self.current_workingFrame)
#         #
#         #     if ret:
#         #         rgbImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         #         convertToQtFormat = QImage(rgbImage.data,rgbImage.shape[1],rgbImage.shape[0],
#         #                                    rgbImage.shape[1] * rgbImage.shape[2],QImage.Format_RGB888)
#         #         # self.changePixmap.emit(convertToQtFormat.copy(), QRect(x,y,600,300))
#         #
#         #         self.changePixmap.emit(convertToQtFormat.copy(),QRect(x,y,width,height))  # 최종적으로 결정된 추출 영역을 QRect로 emit
#         #     else:
#         #         print("오토포커싱 검출 완료")
#         #         print(self.afc_coordList)
#         #         self.afc_state = 2
#         #         self.afc_process = 0
#         #         break
#         #
#         #     if self.current_workingFrame > 600:
#         #         print("오토포커싱 검출 완료")
#         #         self.afc_state = 2
#         #         self.afc_process = 0
#         #         break
#         #
#         #     time.sleep(0.03)
#         # print("Autofucusing start")
#         # print(current_workingFrame, self.afc_extFrameRate)
#         # print(current_workingFrame % self.afc_extFrameRate)
#         if not current_workingFrame % self.afc_extFrameRate:
#             index = int(current_workingFrame / self.afc_extFrameRate)
#             if index > len(self.afc_coordList) - 1:
#                 self.afc_coordList.append(self.make_afcSection())
#
#             if index == 0:
#                 self.cur_coord = self.afc_coordList[index]
#                 self.dst_coord = self.afc_coordList[index]
#             else:
#                 self.dst_coord = self.afc_coordList[index]
#
#             print("frame : {} index : {} value : {}".format(self.current_workingFrame,index,
#                                                                 self.afc_coordList[index]))
#
#         self.cur_coord = self.smooth_movedSection(self.cur_coord,self.dst_coord,self.current_workingFrame % self.afc_extFrameRate,
#                                              self.afc_extFrameRate)
#
#         return self.cur_coord
#
#     def play_afcResult(self, playFrame):
#         '''
#         추출된 좌표를 기반으로 오토포커싱된 영상을 플레이어에서 재생한다.
#         :return:
#         '''
#         # self.current_playingFrame = 0
#         # self.cap.set(cv2.CAP_PROP_POS_FRAMES,self.current_playingFrame)
#         # print("afc play 시작")
#         # print("{}".format(self.afc_coordList))
#         # print("afc_state : " , self.afc_state)
#         # while self.afc_play and not self.afc_state == 0:
#         #
#         #     if not self.current_playingFrame % self.afc_extFrameRate:
#         #         index = int(self.current_playingFrame / self.afc_extFrameRate)
#         #
#         #         if index == 0:
#         #             cur_coord = self.afc_coordList[index]
#         #             dst_coord = self.afc_coordList[index]
#         #             print("frame : {} index : {} value : {}".format(self.current_playingFrame,index,
#         #                                                             self.afc_coordList[index]))
#         #         elif index < len(self.afc_coordList):
#         #             dst_coord = self.afc_coordList[index]
#         #             print("frame : {} index : {} value : {}".format(self.current_playingFrame,index,
#         #                                                             self.afc_coordList[index]))
#         #
#         #     cur_coord = self.smooth_movedSection(cur_coord,dst_coord,self.current_playingFrame % self.afc_extFrameRate,
#         #                                          self.afc_extFrameRate)
#         #     x,y,width,height = cur_coord
#         #
#         #     ret,frame = self.cap.read()
#         #
#         #     self.current_playingFrame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
#         #
#         #     if ret:
#         #         rgbImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         #         convertToQtFormat = QImage(rgbImage.data,rgbImage.shape[1],rgbImage.shape[0],
#         #                                    rgbImage.shape[1] * rgbImage.shape[2],QImage.Format_RGB888)
#         #         # self.changePixmap.emit(convertToQtFormat.copy(), QRect(x,y,600,300))
#         #         self.changePixmap.emit(convertToQtFormat.copy(),QRect(x,y,width,height))  # 최종적으로 결정된 추출 영역을 QRect로 emit
#         #     else:
#         #         print(self.afc_coordList)
#         #         self.afc_play = 0
#         #         break
#         #
#         #     if self.current_playingFrame > 600:
#         #         self.afc_play = 0
#         #         break
#         #
#         #     time.sleep(0.03)
#         # print("play afc 종료")
#
#     def save_coordFile(self,type):
#         '''
#         오토포커싱된 좌표를 파일로 저장한다.
#         :param type:
#         :return:
#         '''
#         pass
#
#     def save_afcVideoFile(self,file_path,extension,size):
#         '''
#         오토포커싱된 영상을 파일로 저장한다.
#         :param extension:
#         :param resolution:
#         :param result:
#         :return:
#         '''
#         file_name = os.path.splitext(file_path)[0]
#
#         if extension == ".avi":
#             fourcc = cv2.VideoWriter_fourcc("D","I","V","X")
#             out = cv2.VideoWriter("afc_" + file_name + ".avi",fourcc,30.0,size)
#         elif extension == ".mp4":
#             fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
#             out = cv2.VideoWriter("afc_" + file_name + ".mp4",fourcc,30.0,size)
#
#         self.afc_play = 1
#         self.current_savingFrame = 0
#         self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)
#         print("afc play 시작")
#         print("{}".format(self.afc_coordList))
#
#         while self.afc_save:
#
#             if not self.current_savingFrame % self.afc_extFrameRate:
#                 index = int(self.current_savingFrame / self.afc_extFrameRate)
#
#                 if index == 0:
#                     cur_coord = self.afc_coordList[index]
#                     dst_coord = self.afc_coordList[index]
#                     print("frame : {} index : {} value : {}".format(self.current_savingFrame,index,
#                                                                     self.afc_coordList[index]))
#                 elif index < len(self.afc_coordList):
#                     dst_coord = self.afc_coordList[index]
#                     print("frame : {} index : {} value : {}".format(self.current_savingFrame,index,
#                                                                     self.afc_coordList[index]))
#
#             cur_coord = self.smooth_movedSection(cur_coord,dst_coord,self.current_savingFrame % self.afc_extFrameRate,
#                                                  self.afc_extFrameRate)
#             x,y,width,height = cur_coord
#
#             ret,frame = self.cap.read()
#
#             self.current_savingFrame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
#
#             if ret:
#
#                 out.write(frame)
#             else:
#                 self.afc_save = 0
#                 break
#
#             if self.current_savingFrame > 600:
#                 self.afc_save = 0
#                 break
#
#             time.sleep(0.03)
#
#     # def pause_afc(self):
#     #     self.play = False
#     #
#     # def start_afc(self):
#     #     self.play = True
#
#     def get_afcState(self):
#         '''
#         오토포커싱 작업이 완료 되었는지 확인
#         0 : 검출 작업 이전
#         1 : 검출 작업 중
#         2 : 검출 완료
#         :return: self.afc_state
#         '''
#         return self.afc_state
#
#     def smooth_movedSection(self,cur_coord,dst_coord,currentFrame,frameRate):
#         '''
#         현재 좌표와 이동할 좌표, 추출된 프레임의 간격을 계산하여 박스의 이동을 자연스럽게 한다.
#         :param cur_coord: 현재 좌표
#         :param dst_coord: 이동할 좌표
#         :param frameRate: 추출된 좌표의 프레임수
#         :return: 다음 이동할 좌표
#         '''
#         num_remainedFrame = frameRate - currentFrame
#         move_coord = []
#         if num_remainedFrame == 0 or cur_coord == dst_coord:
#             return dst_coord
#
#         for i in range(4):
#             if dst_coord[i] == cur_coord[i]:
#                 move_coord.append(cur_coord[i])
#             else:
#                 move_pos = dst_coord[i] - cur_coord[i]
#                 move_pos /= num_remainedFrame
#                 move_coord.append(cur_coord[i] + move_pos)
#
#         return move_coord
#


class Autofocus(QObject):
    changePixmap = Signal(QImage,QRect)

    def __init__(self):
        super(Autofocus,self).__init__()
        self.afc_coordList = []  # 검출 좌표 리스트

        # TODO coordLIst 이후 dict로 변경 예정
        # self.afc_coordDict = {}  # 검출 좌표 dict

        # TODO : 샘플 클래스 변수
        self.class_name = "roje"
        # self.class_name = ""

        # # 테스트 변수
        # self.list_index = 0
        # self.list_coord = [(650,330,360,720),(720,405,300,600),(650,330,360,720),(800,500,240,480),(1000,525,150,300)]

    def quit_afcProcess(self):

        self.afc_coordList = []  # 검출 좌표 리스트
        # self.afc_coordDict = {}  # 검출 좌표 dict

    def setUp(self,ui):
        # 추출할 박스 크기
        self.width = ui.cm.video_player.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = ui.cm.video_player.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.afc_width,self.afc_height = ui.opt.get_coord()
        self.afc_extFrameRate = ui.cm.video_player.fps
        # self.class_num = class_num


    # TODO : 포커싱할 좌표를 리턴 / afc_width, afc_heigh 비율 조절 필요
    def make_afcSection(self, resultList):
        '''
        얼굴의 좌표를 기준으로 포커싱할 추출 영역을 결정한다.
        :param resultList: 현재 프레임의 얼굴 검출 결과
        :return: x,y,widht,height
        '''
        current_result = ""
        current_accuracy = 0
        print(resultList)
        for result in resultList:
            if result['labelname'] == self.class_name and current_accuracy < float(result['percent']):
                current_result = result
                current_accuracy = float(result['percent'])

        if current_result == "":
            return  [0,0,self.width,self.height]
        else:
            x = result['x'] + result['w'] / 2 - self.afc_width/2
            y = result['y'] + result['h'] / 2 - self.afc_height / 2
            print("result", result)
            print("make_afcSection " , [x, y, self.afc_width, self.afc_height])
            return [x, y, self.afc_width, self.afc_height]


    def extract_afcVideo(self, current_workingFrame, resultList):
        '''
        추출된 이미지를 재생하고 영역 좌표를 리스트로 저장한다.
        :param current_workingFrame : 현재 프레임이 작업되고 있는 프레임 number
        :param resultList : 현재 프레임의 얼굴 검출 결과
        :return: crop할 좌표
        '''
        self.afc_extFrameRate = 5
        if not current_workingFrame % self.afc_extFrameRate:
            index = int(current_workingFrame / self.afc_extFrameRate)
            if index > len(self.afc_coordList) - 1:
                self.afc_coordList.append(self.make_afcSection(resultList))

            if index == 0:
                self.cur_coord = self.afc_coordList[index]
                self.dst_coord = self.afc_coordList[index]
            else:
                self.dst_coord = self.afc_coordList[index]

            print("frame : {} index : {} value : {}".format(current_workingFrame,index,
                                                                self.afc_coordList[index]))

        self.cur_coord = self.smooth_movedSection(self.cur_coord,self.dst_coord,current_workingFrame % self.afc_extFrameRate,
                                             self.afc_extFrameRate)

        return self.cur_coord


    # TODO : 함수를 사용하여 포커싱 좌표를 저장. fps와 추출 시간도 추가 저장해야 한다.
    def get_coordResult(self):
        '''
        오토포커싱된 좌표를 리턴한다
        :param type:
        :return:
        '''
        return self.afc_coordList

    def save_afcVideoFile(self,cap, file_path, extension,size):
        '''
        오토포커싱된 영상을 파일로 저장한다.
        :param extension:
        :param resolution:
        :param result:
        :return:
        '''
        file_name = os.path.splitext(file_path)[0]
        current_savingFrame = 0

        if extension == ".avi":
            fourcc = cv2.VideoWriter_fourcc("D","I","V","X")
            out = cv2.VideoWriter("afc_" + file_name + ".avi",fourcc,30.0,size)
        elif extension == ".mp4":
            fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
            out = cv2.VideoWriter("afc_" + file_name + ".mp4",fourcc,30.0,size)

        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        print("afc play 시작")
        print("{}".format(self.afc_coordList))

        while True:

            if not current_savingFrame % self.afc_extFrameRate:
                index = int(current_savingFrame / self.afc_extFrameRate)

                if index == 0:
                    cur_coord = self.afc_coordList[index]
                    dst_coord = self.afc_coordList[index]
                    print("frame : {} index : {} value : {}".format(current_savingFrame,index,
                                                                    self.afc_coordList[index]))
                elif index < len(self.afc_coordList):
                    dst_coord = self.afc_coordList[index]
                    print("frame : {} index : {} value : {}".format(current_savingFrame,index,
                                                                    self.afc_coordList[index]))

            cur_coord = self.smooth_movedSection(cur_coord,dst_coord, current_savingFrame % self.afc_extFrameRate,
                                                 self.afc_extFrameRate)
            x,y,width,height = cur_coord

            ret,frame = cap.read()

            current_savingFrame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

            if ret:
                out.write(frame)
            else:
                break

    def smooth_movedSection(self,cur_coord,dst_coord,currentFrame,frameRate):
        '''
        현재 좌표와 이동할 좌표, 추출된 프레임의 간격을 계산하여 박스의 이동을 자연스럽게 한다.
        :param cur_coord: 현재 좌표
        :param dst_coord: 이동할 좌표
        :param frameRate: 추출된 좌표의 프레임수
        :return: 다음 이동할 좌표
        '''
        num_remainedFrame = frameRate - currentFrame
        move_coord = []
        if num_remainedFrame == 0 or cur_coord == dst_coord:
            return dst_coord

        for i in range(4):
            if dst_coord[i] == cur_coord[i]:
                move_coord.append(cur_coord[i])
            else:
                move_pos = dst_coord[i] - cur_coord[i]
                move_pos /= num_remainedFrame
                move_coord.append(cur_coord[i] + move_pos)

        return move_coord