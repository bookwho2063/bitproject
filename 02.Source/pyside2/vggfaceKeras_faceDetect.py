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

    def identify_face(self, features, threshold=110):
        distances = []
        for person in self.precompute_features_map:
            person_features = person.get("features")
            distance = scipyDistance.euclidean(person_features, features)
            distances.append(distance)
        min_distance_value = min(distances)
        min_distance_index = distances.index(min_distance_value)


        if min_distance_value < threshold:
            # print("min_distance_value :: (", str(min_distance_value) + ") :: " + str(self.precompute_features_map[min_distance_index].get("name")))
            # print("min_distance_index :: ", str(min_distance_index))
            return self.precompute_features_map[min_distance_index].get("name")
        else:
            print("Not Found min_distance_value :: (", str(min_distance_value) + " )")
            print("Not Found min_distance_index :: ", str(self.precompute_features_map[min_distance_index].get("name")))
            return "???"

    def detect_face(self):
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
        video_capture = cv2.VideoCapture("/home/bit/Downloads/test5.mp4")

        width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        fps = video_capture.get(cv2.CAP_PROP_FPS)

        video_writer = cv2.VideoWriter('./write_70.avi', fcc, fps, (int(width), int(height)))

        # infinite loop, break by key ESC
        while True:
            if not video_capture.isOpened():
                sleep(5)

            # Capture frame-by-frame
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10, minSize=(64, 64))

            # print("faces :: ")
            # print(faces)

            # placeholder for cropped faces
            face_imgs = np.empty((len(faces), self.face_size, self.face_size, 3))
            # print("face_imgs :: ")
            # print(face_imgs)

            # 검출된 얼굴 수 만큼 루프를 돌며 사각형을 그리고, imgs 어레이에 인풋
            for i, face in enumerate(faces):
                face_img, cropped = self.crop_face(frame, face, margin=10, size=self.face_size)
                (x, y, w, h) = cropped

                # width > 60 일때만 검출 하도록 변경 조치
                if w > 70:
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

            cv2.imshow('Keras Faces', frame)
            if cv2.waitKey(5) == 27:  # ESC key press
                break

        # When everything is done, release the capture
        video_capture.release()
        video_writer.release()
        cv2.destroyAllWindows()


def main():
    face = FaceIdentify(precompute_features_file="../Ref/data/train/precompute_features.pickle")
    face.detect_face()

if __name__ == "__main__":
    main()




