import cv2

class saveVideo(object):

    def __init__(self):
        self.cap = cv2.VideoCapture("C:/Users/bit/Downloads/videoplayback.mp4")
        self.fps = round(self.cap.get(cv2.CAP_PROP_FPS))
        self.bufferTime = 3
        self.out = None

    def openVideoWriter(self, file_name):
        '''
        file format
        fps
        width
        height
        saveFileName
        :return:
        '''
        # cap = cv2.VideoCapture("C:/Users/bit/Downloads/videoplayback.mp4")
        fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.out = cv2.VideoWriter("./extVideo.avi", fcc, self.fps, (int(width), int(height)))

    def closeVideoWriter(self):
        self.out.release()

    def saveVideo(self, resultList, saveCoord=True):
        for result in resultList:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, int(result[-1]))
            for i in range(self.bufferTime * self.fps):
                ref, frame = self.cap.read()
                if ref:
                    self.out.write(frame)
                else:
                    break

    def saveCoordFile(self, resultList, file_name, type = 'csv',):

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




'''
resultLIst
buffertime

'''
resultList = [[{'x': 360, 'y': 129, 'w': 132, 'h': 132, 'percent': '98.48', 'labelname': 'roje'},{'x': 313, 'y': 43, 'w': 102, 'h': 102, 'percent': '97.64', 'labelname': 'roje'},{'x': 313, 'y': 43, 'w': 102, 'h': 102, 'percent': '97.64', 'labelname': 'roje'}, '0'], [{'x': 313, 'y': 43, 'w': 102, 'h': 102, 'percent': '97.64', 'labelname': 'roje'}, '1000'], [{'x': 260, 'y': 42, 'w': 144, 'h': 144, 'percent': '95.4', 'labelname': 'roje'}, '2000']]
resultList_2 = [[{'x': 360, 'y': 129, 'w': 132, 'h': 132, 'percent': '98.48', 'labelname': 'roje'}, '0'], [{'x': 313, 'y': 43, 'w': 102, 'h': 102, 'percent': '97.64', 'labelname': 'roje'}, '1000'], [{'x': 260, 'y': 42, 'w': 144, 'h': 144, 'percent': '95.4', 'labelname': 'roje'}, '2000']]
sv = saveVideo()


## 클래스를 통해 비디오 파일 저장
# sv.openVideoWriter()
# sv.saveVideo(resultList)
# sv.closeVideoWriter()

######################
# csv 파일 저장 (검출 결과
######################
# with open('test.csv','wt',newline='') as output_file:
#     dict_writer = csv.DictWriter(output_file,keys)
#     dict_writer.writeheader()
#     for result in resultList:
#         result = [dict(item,**{'frame_num': result[-1]}) for item in result[:-1]]
#         dict_writer.writerows(result)

######################
# json 파일 저장
######################
import json

with open('./test.json', 'w') as output_file:
    for result in resultList:
        result = [dict(item,**{'frame_num': result[-1]}) for item in result[:-1]]
        json.dump(result, output_file, ensure_ascii=False, indent="\t")





######################
# 비디오 프레임 저장
######################
# while True:
#     cur_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
#     cnt_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
#
#     if cur_frame == cnt_frame:
#         cap.open("C:/Users/bit/Downloads/videoplayback.mp4")
#
#     print("cur_frame :: ", int(cur_frame))
#     print("cnt_frame :: ", int(cnt_frame))
#
#     ret, frame = cap.read()
#     print("before :: ", int(cur_frame))
#     if int(cur_frame) > 500 and int(cur_frame) < 2000:
#         print("write fps :: ", int(cur_frame))
#         out.write(frame)
#
#     if cur_frame == 2000 or cur_frame > 2000:
#         closeVideoWriter(out)
#         cap.release()
#         break
#
# closeVideoWriter(out)
# # out.release()
# cap.release()
