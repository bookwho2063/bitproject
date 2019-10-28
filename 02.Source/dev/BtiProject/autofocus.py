from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import cv2,time,os
import numpy as np


class Autofocus(QObject):
    changePixmap = Signal(QImage,QRect)

    def __init__(self):
        super(Autofocus,self).__init__()
        self.afc_coordDict = {}  # 검출 좌표 dict
        self.class_name = ""


    def quit_afcProcess(self):
        self.afc_coordDict = {}  # 검출 좌표 dict

    def setUp(self,ui):
        # 추출할 박스 크기
        self.width = ui.cm.video_player.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = ui.cm.video_player.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.afc_width,self.afc_height = ui.opt.get_coord()
        self.afc_extFrameRate = int(ui.cm.video_player.fps )

    def setClassName(self, name):
        print("name :: ", name)
        self.class_name = name

    def getClassName(self):
        return self.class_name

    # TODO : 포커싱할 좌표를 리턴 / afc_width, afc_heigh 비율 조절 필요
    def make_afcSection(self, resultList):
        '''
        얼굴의 좌표를 기준으로 포커싱할 추출 영역을 결정한다.
        :param resultList: 현재 프레임의 얼굴 검출 결과
        :return: x,y,widht,height
        '''
        current_result = ""
        current_accuracy = 0
        if not resultList == []:
            for result in resultList:
                if result['labelname'] == self.class_name and current_accuracy < float(result['percent']):
                    current_result = result
                    current_accuracy = float(result['percent'])

        if current_result == "":
            return [0,0,self.width,self.height]
        else:
            x = current_result['x'] + current_result['w'] / 2 - self.afc_width / 2
            y = current_result['y'] + current_result['h'] / 2 - self.afc_height / 2

            x,y = [x if x > 0 else 0 for x in [x,y]]

            # print("result",current_result)
            # print("make_afcSection ",[x,y,self.afc_width,self.afc_height])
            return [x,y,self.afc_width,self.afc_height]


    def extract_afcVideo(self, current_workingFrame, resultList=[]):
        '''
        추출된 이미지를 재생하고 영역 좌표를 리스트로 저장한다.
        :param current_workingFrame : 현재 프레임이 작업되고 있는 프레임 number
        :param resultList : 현재 프레임의 얼굴 검출 결과
        :return: crop할 좌표
        '''
        index = int(current_workingFrame / self.afc_extFrameRate)
        result = self.make_afcSection(resultList)
        if current_workingFrame == 0:
            self.cur_coord = result
            self.dst_coord = self.cur_coord

        if current_workingFrame % self.afc_extFrameRate < int(self.afc_extFrameRate / 2):
            if not (index in self.afc_coordDict.keys() or result == [0,0,self.width,self.height]):
                self.afc_coordDict[index] = result
                self.dst_coord = self.afc_coordDict[index]
        elif int(current_workingFrame % self.afc_extFrameRate) == int(self.afc_extFrameRate / 2):
            if not index in self.afc_coordDict.keys():
                self.afc_coordDict[index] = result
                self.dst_coord = self.afc_coordDict[index]

        # print("frame : {} cur_coord : {} dst_coord dst_coord : {}".format(current_workingFrame,index,self.cur_coord,
        #                                                                   self.dst_coord))

        self.cur_coord = self.smooth_movedSection(self.cur_coord,self.dst_coord,
                                                  current_workingFrame % self.afc_extFrameRate,
                                                  self.afc_extFrameRate)

        return self.cur_coord


    def get_coordResult(self):
        '''
        오토포커싱된 좌표를 리턴한다
        :param type:
        :return:
        '''
        return self.afc_coordDict

    def save_afcVideoFile(self,cap, out):
        '''
        오토포커싱된 영상을 파일로 저장한다.
        :param extension:
        :param resolution:
        :param result:
        :return:
        '''
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        out_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        out_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        while True:
            current_savingFrame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            ret,frame = cap.read()
            if ret:

                # 영상 저장의 배경 화면 생성
                back_img = np.zeros([out_height,out_width,3],dtype=np.uint8)
                x,y,width,height = self.play_afcResult(current_savingFrame)

                if not (width == self.width or height == self.height):
                    resized_x,resized_y,size = self.set_saveCoord(width,height,out_width,out_height)
                    crop_frame = frame[int(y): int(y + height),int(x): int(x + width),:]
                    crop_frame = cv2.resize(crop_frame,dsize=size)
                    back_img[resized_y:resized_y + crop_frame.shape[0],
                    resized_x:resized_x + crop_frame.shape[1]] = crop_frame
                    save_frame = back_img
                else:
                    save_frame = frame

                out.write(save_frame)
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

    def play_afcResult(self,playFrame):
        index = int(playFrame / self.afc_extFrameRate)
        if playFrame == 0:
            self.cur_coord = self.afc_coordDict[0]
            self.dst_coord = self.cur_coord

        if not playFrame % self.afc_extFrameRate and index in self.afc_coordDict.keys():
            self.dst_coord = self.afc_coordDict[index]

            # print("frame : {} index : {} dst_coord : {}".format(current_workingFrame,index,self.dst_coord))

        self.cur_coord = self.smooth_movedSection(self.cur_coord,self.dst_coord,
                                                  playFrame % self.afc_extFrameRate,
                                                  self.afc_extFrameRate)

        return self.cur_coord

    def set_saveCoord(self,width,height,target_width,tartget_height):
        if target_width / tartget_height > width / height:
            ratio = tartget_height / height
            x = abs(int((target_width - ratio * width) / 2))
            y = 0

            resize_width = int(ratio * width)
            resize_height = int(ratio * height)

            if resize_height > tartget_height:
                resize_heightc = tartget_height
            return x,y,(resize_width,resize_height)
        else:
            ratio = target_width / width
            x = 0
            y = abs(int((tartget_height - ratio * height) / 2))

            resize_width = int(ratio * width)
            resize_height = int(ratio * height)

            if resize_width > target_width:
                resize_width = target_width

            return x,y,(resize_width,resize_height)

