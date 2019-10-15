from keras.engine import Model
from keras import models
from keras import layers
from keras.layers import Input
from keras.preprocessing import image
from keras_vggface.vggface import VGGFace
import numpy as np
from keras_vggface import utils
from time import sleep
from scipy.spatial import distance as scipyDistance
import cv2
import os, platform, site
import glob
import pickle
from PIL import ImageFont, ImageDraw, Image

def load_stuff(filename):
    saved_stuff = open(filename, "rb")
    stuff = pickle.load(saved_stuff)
    saved_stuff.close()
    return stuff


class FaceIdentify(object):
    """
    Singleton class for real time face identification
    """

    # CASE_PATH = "cv2/data/haarcascade_frontalface_default.xml"

    def __new__(cls, precompute_features_file=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FaceIdentify, cls).__new__(cls)
        return cls.instance

    def __init__(self, precompute_features_file=None):
        self.face_size = 224
        self.precompute_features_map = load_stuff(precompute_features_file)
        print("Loading VGG Face model...")
        self.model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')  # pooling: None, avg or max
        print("Loading VGG Face model done")

    @classmethod
    def draw_label(cls, image, point, label, font=cv2.FONT_HERSHEY_SIMPLEX,
                   font_scale=1, thickness=2):
        # cv2
        size = cv2.getTextSize(label, font, font_scale, thickness)[0]
        x, y = point
        cv2.rectangle(image, (x, y - size[1]), (x + size[0], y), (255, 0, 0), cv2.FILLED)
        cv2.putText(image, label, point, font, font_scale, (255, 255, 255), thickness)

    def crop_face(self, imgarray, section, margin=20, size=224):
        """
        :param imgarray: full image
        :param section: face detected area (x, y, w, h)
        :param margin: add some margin to the face detected area to include a full head
        :param size: the result image resolution with be (size x size)
        :return: resized image in numpy array with shape (size x size x 3)
        """
        img_h, img_w, _ = imgarray.shape
        if section is None:
            section = [0, 0, img_w, img_h]
        (x, y, w, h) = section
        margin = int(min(w, h) * margin / 100)
        x_a = x - margin
        y_a = y - margin
        x_b = x + w + margin
        y_b = y + h + margin
        if x_a < 0:
            x_b = min(x_b - x_a, img_w - 1)
            x_a = 0
        if y_a < 0:
            y_b = min(y_b - y_a, img_h - 1)
            y_a = 0
        if x_b > img_w:
            x_a = max(x_a - (x_b - img_w), 0)
            x_b = img_w
        if y_b > img_h:
            y_a = max(y_a - (y_b - img_h), 0)
            y_b = img_h
        cropped = imgarray[y_a: y_b, x_a: x_b]
        resized_img = cv2.resize(cropped, (size, size), interpolation=cv2.INTER_AREA)
        resized_img = np.array(resized_img)
        return resized_img, (x_a, y_a, x_b - x_a, y_b - y_a)

    def identify_face(self, features, threshold=100):

        # name 변경용 dict
        nameChDict = dict()
        nameChDict['로제'] = 'Rose'
        nameChDict['제니'] = 'Jennie'
        nameChDict['리사'] = 'Lisa'
        nameChDict['지수'] = 'Jisu'

        distances = []
        for person in self.precompute_features_map:
            person_features = person.get("features")
            distance = scipyDistance.euclidean(person_features, features)
            distances.append(distance)
        min_distance_value = min(distances)
        min_distance_index = distances.index(min_distance_value)
        print("min_distance_value :: ", min_distance_value)
        print("self.precompute_features_map[min_distance_index].get(name) :: ",self.precompute_features_map[min_distance_index].get("name"))
        if min_distance_value < threshold:
            return nameChDict[str(self.precompute_features_map[min_distance_index].get("name"))]
        else:

            return "???"

    def detect_face(self, videoPath, savePath):
        if platform.system() == "Windows":
            # self.face_cascade = cv2.CascadeClassifier('C:\\Users\\JK\\Documents\\GitHub\\bitproject\\haarcascade_frontface.xml')
            face_cascade = cv2.CascadeClassifier(
                os.path.join(site.getsitepackages()[1], "cv2/data/haarcascade_frontalface_default.xml"))
        elif platform.system() == "Linux":
            # self.face_cascade = cv2.CascadeClassifier('/home/bit/anaconda3/envs/faceRecognition/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
            face_cascade = cv2.CascadeClassifier(
                os.path.join(site.getsitepackages()[0], "cv2/data/haarcascade_frontalface_default.xml"))

        # face_cascade = cv2.CascadeClassifier(self.CASE_PATH)

        # 0 means the default video capture device in OS
        # video_capture = cv2.VideoCapture("/home/bit/jk/twice/valid/valid1.mp4")
        fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        fps = cv2.CAP_PROP_FPS
        print("videoPath :: ", videoPath)
        video_capture = cv2.VideoCapture(videoPath)
        video_writer = cv2.VideoWriter(savePath, fcc, int(fps), (1280,720))

        # infinite loop, break by key ESC
        while True:
            if not video_capture.isOpened():
                sleep(5)

            # Capture frame-by-frame
            ret, frame = video_capture.read()

            if video_capture.get(cv2.CAP_PROP_POS_FRAMES) == video_capture.get(cv2.CAP_PROP_FRAME_COUNT):
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10, minSize=(64, 64))

            # placeholder for cropped faces
            face_imgs = np.empty((len(faces), self.face_size, self.face_size, 3))

            # 검출된 얼굴 수 만큼 루프를 돌며 사각형을 그리고, imgs 어레이에 인풋
            for i, face in enumerate(faces):

                face_img, cropped = self.crop_face(frame, face, margin=10, size=self.face_size)
                (x, y, w, h) = cropped

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 200, 0), 2)
                face_imgs[i, :, :, :] = face_img

            # imgs 어레이(한 프레임 내 인물 갯수 및 해당 데이터)
            # model.predict 처리할 때 어레이로 묶은걸 한번만 처리한다 사각 박스별로 처리하는게 아니라.
            if len(face_imgs) > 0:
                # generate features for each face
                features_faces = self.model.predict(face_imgs)
                predicted_names = [self.identify_face(features_face) for features_face in features_faces]

            # draw results
            for i, face in enumerate(faces):
                label = "{}".format(predicted_names[i])
                self.draw_label(frame, (face[0], face[1]), label)
                video_writer.write(frame)

            frame = cv2.resize(frame, (1280,720))

            cv2.imshow('Keras Faces', frame)
            if cv2.waitKey(5) == 27:  # ESC key press
                break

        # When everything is done, release the capture
        video_capture.release()
        video_writer.release()
        cv2.destroyAllWindows()


def main():
    # face = FaceIdentify(precompute_features_file="../dev/BtiProject/00.Resource/data/pickle/precompute_features_40000_bat32.pickle")
    # face = FaceIdentify(precompute_features_file="../dev/BtiProject/00.Resource/data/pickle/precompute_features_20000.pickle")

    # 피클 경로
    faceList = list()
    # faceList.append("../dev/BtiProject/00.Resource/data/pickle/precompute_features_20000.pickle")
    faceList.append("../dev/BtiProject/00.Resource/data/pickle/precompute_features_40000_bat2.pickle")
    faceList.append("../dev/BtiProject/00.Resource/data/pickle/precompute_features_40000_bat4.pickle")
    faceList.append("../dev/BtiProject/00.Resource/data/pickle/precompute_features_40000_bat8.pickle")
    faceList.append("../dev/BtiProject/00.Resource/data/pickle/precompute_features_40000_bat16.pickle")
    faceList.append("../dev/BtiProject/00.Resource/data/pickle/precompute_features_40000_bat32.pickle")

    # 실 비디오 경로
    videoList = list()
    videoList.append("F:/sampleData/bp1.mp4")
    videoList.append("F:/sampleData/bp3.mp4")

    # 비디오 파일명
    vNameList = list()
    vNameList.append("bp1")
    vNameList.append("bp3")

    # 피클파일명
    numList = list()
    # numList.append("20000")
    numList.append("40000_bat2")
    numList.append("40000_bat4")
    numList.append("40000_bat8")
    numList.append("40000_bat16")
    numList.append("40000_bat32")

    for picIdx in range(len(faceList)):
        face = None
        for idx in range(len(videoList)):
            face = FaceIdentify(precompute_features_file=str(faceList[picIdx]))
            face.detect_face(videoList[idx], str("F:/sampleData/result/compareVideo_{}_{}.avi".format(vNameList[idx], numList[picIdx])))
            del face


if __name__ == "__main__":
    main()




