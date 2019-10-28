import cv2
import os, glob, pickle, platform, site, datetime
import numpy as np
import tensorflow as tf
from keras import backend as K
from time import sleep
from keras.engine import Model
from keras import layers, models
from keras.layers import Input
from keras_vggface.vggface import VGGFace
from keras_preprocessing import image
from keras_applications.resnet50 import ResNet50
from keras_applications.resnet50 import preprocess_input
from keras_vggface import utils
from scipy.spatial import distance as scipyDistance


def load_stuff(filename):
    """
    피클 파일 로드
    :param filename:
    :return:
    """
    saved_stuff = open(filename, "rb")
    stuff = pickle.load(saved_stuff)
    saved_stuff.close()
    # print("=====loaded stuff success :: ", filename)
    # print("stuff :: ", stuff)
    return stuff

def pickleStuff(fileName, stuff):
    """
        피클 파일 생성
    :param fileName:
    :param stuff:
    :return: pickle data List
    """
    saveStuff = open(fileName, "wb")
    pickle.dump(stuff, saveStuff)
    saveStuff.close()
    print("=====create stuff success")

def getDayTime(flag):
    """
    날자 형식을 리턴한다.
    :param flag: yyyymmdd / yyyymmddhhmmssmm / yyyymmddhhmmss
    :return:
    """
    now = datetime.datetime.now()
    if flag == "yyyymmdd":
        dt = datetime.datetime.today().strftime("%Y%m%d")
        return dt
    elif flag == "yyyymmddhhmmssmm":
        dt = datetime.datetime.today().strftime("%Y%m%d%H%M%s")
        return dt
    else:
        dt = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        return dt


def appendPickleStuff(stuff, name, feature):
    """
    pickle 데이터를 추가한다 (검출 얼굴 임베딩 데이터 값 추가)
    :param stuff: 피클 데이터
    :param appendData:
    :return:
    """
    stuff.append({"name": name, "features": feature})

class recognitionFace(object):
    """
    INFO : VGGFACE2를 이용하여 영상 내 프레임에서 얼굴을 검출하는 클래스
    """
    def __new__(cls, weight_file=None, face_size=224):
        if not hasattr(cls, 'instance'):
            cls.instance = super(recognitionFace, cls).__new__(cls)
        return cls.instance

    def __init__(self, face_size=224):
        self.face_size = face_size
        self.precompute_features_map = None
        self.face_cascade = None
        self.model = None

        self.FACE_IMAGES_FOLDER = "./00.Resource/tmp"
        self.osName = ""  # OS명
        self.face_cascade = ""  # cascade 타겟변수
        self.faceSize = face_size  # 얼굴 검출 사진 사이즈
        self.batchSize = 16  # 배치사이즈
        self.className = None  # 사용자가 입력한 클래스명
        self.saveFolder = None  # vggfaceInit() 을 통해 생성되는 클래스폴더경로
        self.savePkPath = "./00.Resource/data/pickle/"  # 피클파일 저장경로
        self.savePkNm = "savePickle_"  # 피클파일 저장파일명
        self.targetStuff = None

    def selectLastUptPickleFeatureList(self, flag):
        """
        pickle 폴더 내 마지막으로 생성된 .pickle 파일 조회 후 피처 리스트 리턴
        :param: flag(path:pickle Path(str) / feature:pickle Feature(list)
        :return:
        """
        pFolderPath = "./00.Resource/data/pickle"
        pFileList = list()
        featureList = list()
        for file in os.listdir(pFolderPath):
            if file.split(".")[1] != "pickle":
                continue
            pFileList.append(os.path.join(pFolderPath, file))

        pFileList.sort(key=os.path.getmtime)
        if flag == "path":
            return pFileList[-1]
        elif flag == "feature":
            precompute_features_map = load_stuff(pFileList[-1])
            # 피클 데이터 공용변수 설정
            self.targetStuff = precompute_features_map
            for person in precompute_features_map:
                featureList.append(person.get("name"))

            return featureList

    def changePicklefile(self):
        self.precompute_features_map = load_stuff(self.selectLastUptPickleFeatureList("path"))

    def vggRecogInit(self):
        """
        클래스를 초기화한다 (최초 프로그램 시작시 수행하므로 기타변수들 여기서 추가하지말 것)
        :return:
        """
        if self.model == None:
            # print("model :: ", self.model)
            # print("model type :: ", type(self.model))
            self.model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')  # pooling: None, avg or max
            self.model.predict(np.zeros((1, 224, 224, 3)))
            self.session = K.get_session()
            self.graph = tf.get_default_graph()
            self.graph.finalize()

    def changePickle(self, targetPath):
        load_stuff(targetPath)

    def createPickle(self, targetStuffList=None):
        """
        pickle 파일을 생성한다.
        :return: 저장 성공여부
        """
        folders = list(glob.iglob(os.path.join(self.FACE_IMAGES_FOLDER, "*")))
        names = [os.path.basename(folder) for folder in folders]

        dt = getDayTime("yyyymmddhhmmss")
        self.savePkNm = self.savePkNm + str(dt) + ".pickle"
        # precompute_features = []
        pickleFilePath = os.path.join(self.savePkPath, self.savePkNm)

        if targetStuffList is None:
            targetStuffList = []

        # pickle data read
        for i, folder in enumerate(folders):
            name = names[i]
            save_folder = os.path.join(self.FACE_IMAGES_FOLDER, name)
            mean_features = self.calMeanFeature(imageFolder=save_folder)
            targetStuffList.append({"name": name, "features": mean_features})
            # precompute_features.append({"name": name, "features": mean_features})

            # 대표 이미지 저장을 위하여 피클 생성 폴더 이미지 리스트 조회
            imgs = os.listdir(save_folder)
            imgs.sort()
            for img in imgs:
                if img.split(".")[-1] == "png" or img.split(".")[-1] == "PNG":
                    # 대표이미지 생성 및 LabelList 폴더 저장
                    name = name + ".png"
                    labelImgPath = os.path.join("./LabelList", name)
                    img = os.path.join(save_folder, img)
                    thumnailImg = cv2.imread(img, cv2.IMREAD_COLOR)
                    cv2.imwrite(labelImgPath, thumnailImg)
                    break

        # 피클 파일 생성
        pickleStuff(pickleFilePath, targetStuffList)


        if os.path.isfile(pickleFilePath):
            return True, pickleFilePath
        else:
            return False, pickleFilePath

    def loadPickle(self, loadPath):
        """
        pickle 파일을 로드 한다
        :param loadPath: 로드할 대상 파일 경로
        :return: 로드 클래스명 (썸네일 생성을 위함)
        """
        pass
        return "loadClassList"

    def osSetting(self):
        """
        OS Platform 에 따른 분류
        :return:
        """
        if platform.system() == "Windows":
            self.osName = "Windows"
            self.face_cascade = cv2.CascadeClassifier(
                os.path.join(site.getsitepackages()[1], "cv2/data/haarcascade_frontalface_default.xml"))
        elif platform.system() == "Linux":
            self.osName = "Linux"
            self.face_cascade = cv2.CascadeClassifier(
                os.path.join(site.getsitepackages()[0], "cv2/data/haarcascade_frontalface_default.xml"))


    def cropFace(self, imgarray, section, margin=20, size=224):
        """
        프레임을 crop 하여 결과를 리턴한다.
        :param imgarry: full Image
        :param section: face Detected Area (x, y, w, h)
        :param margin: add some margin to the face detected area
        :param size: result image resolution
        :return: resize image (size * size * 3)
        """

        img_h, img_w, _ = imgarray.shape

        if section is None:
            section = [0, 0, img_w, img_h]

        (x, y, w, h) = section

        margin = int(min(w,h) * margin / 100)
        x_a = x - margin
        y_a = y - margin
        x_b = x + w + margin
        y_b = y + h + margin

        if x_a < 0:
            x_b = min(x_b - x_a, img_w-1)
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

        # print("after if :: {}, {}, {}, {}".format(x_a, y_a, x_b, y_b))

        cropped = imgarray[y_a: y_b, x_a: x_b]
        resized_img = cv2.resize(cropped, (size, size), interpolation=cv2.INTER_AREA)
        resized_img = np.array(resized_img)
        return resized_img, (x_a, y_a, x_b - x_a, y_b - y_a)

    def extractFace(self, frame, frameNum):
        """
        프레임에서 얼굴을 검출하고 저장한다.
        :param frame: 프레임 정보를 인자로 준다
        :return:
        """
        # OS에 따라 처리분기
        self.osSetting()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=10,
            minSize=(64, 64)
        )

        # only keep the biggest face as the main subject
        face = None
        if len(faces) > 1:  # Get the largest face as main face
            face = max(faces, key=lambda rectangle: (rectangle[2] * rectangle[3]))  # area = w * h
        elif len(faces) == 1:
            face = faces[0]

        if face is not None:
            face_img, cropped = self.cropFace(frame, face, margin=40, size=self.faceSize)

            (x, y, w, h) = cropped
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 200, 0), 2)
            # cv2.imshow('Faces', frame)

            # 이미지 데이터 특정경로 저장
            imgfile = os.path.basename(self.className) + str(frameNum) + ".png"
            imgfile = os.path.join(str(self.saveFolder), str(imgfile))

            # 이미지 데이터파일명이 폴더 내 존재하는 경우
            if os.path.exists(imgfile):
                dayOfMillieSecond = getDayTime("yyyymmddhhmmssmm")
                imgfile = os.path.basename(self.className) + str(dayOfMillieSecond) + ".png"
                imgfile = os.path.join(str(self.saveFolder), str(imgfile))

            # rgb to bgr
            b,g,r = cv2.split(face_img)
            face_img = cv2.merge([r,g,b])

            # img write
            cv2.imwrite(imgfile, face_img)


    def image2x(self, imagePath):
        """
        이미지의 평균치를 구한다.
        :param imagePath:
        :return:
        """
        img = image.load_img(imagePath, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = utils.preprocess_input(x, version=1) # or version = 2
        return x

    def calMeanFeature(self, imageFolder):
        faceImages = list(glob.iglob(os.path.join(imageFolder, "*")))

        def chunks(l, n):
            """
            batchSize 만큼의 제너레이터를 생성하여 리턴한다.
            :param l:
            :param n:
            :return:
            """
            for i in range(0, len(l), n):
                yield l[i:i+n]

        faceImageChunks = chunks(faceImages, self.batchSize)
        fvecs = None

        for faceImageChunk in faceImageChunks:
            images = np.concatenate([self.image2x(faceImage) for faceImage in faceImageChunk])
            batchFvecs = self.model.predict(images)
            if fvecs is None:
                fvecs = batchFvecs
            else:
                fvecs = np.append(fvecs, batchFvecs, axis=0)

            # print("========== 생성중 ... [ " + str(len(fvecs)) + " ]")
        return np.array(fvecs).sum(axis=0) / len(fvecs)


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
        distances = []
        for person in self.precompute_features_map:
            person_features = person.get("features")
            distance = scipyDistance.euclidean(person_features, features)
            distances.append(distance)
        min_distance_value = min(distances)
        min_distance_index = distances.index(min_distance_value)

        # print("=== 검출 대상명 :: ", self.precompute_features_map[min_distance_index].get("name"))
        # print("=== 스코어 :: ", min_distance_value)

        if min_distance_value < threshold:
            return str(self.precompute_features_map[min_distance_index].get("name")), str(min_distance_value)
        else:
            return "???", "???"

    def osSetting(self):
        if platform.system() == "Windows":
            self.face_cascade = cv2.CascadeClassifier(os.path.join(site.getsitepackages()[1], "cv2/data/haarcascade_frontalface_default.xml"))
        elif platform.system() == "Linux":
            self.face_cascade = cv2.CascadeClassifier(os.path.join(site.getsitepackages()[0], "cv2/data/haarcascade_frontalface_default.xml"))

    def detect_face(self, frame):
        """
        프레임데이터 입력 시 검출 결과 정보를 리턴한다.
        :param frame:
        :return:
        """
        self.osSetting()
        predicted_names = list()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10, minSize=(64, 64))

        # placeholder for cropped faces
        face_imgs = np.empty((len(faces), self.face_size, self.face_size, 3))

        tempCoordList = list()
        for i, face in enumerate(faces):
            face_img, cropped = self.crop_face(frame, face, margin=10, size=self.face_size)
            (x, y, w, h) = cropped
            # 검출 결과 좌표 데이터 설정
            tempCoordDict = dict()
            tempCoordDict['x'] = x
            tempCoordDict['y'] = y
            tempCoordDict['w'] = w
            tempCoordDict['h'] = h
            tempCoordList.append(tempCoordDict)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 200, 0), 2)
            face_imgs[i, :, :, :] = face_img

        # 페이스 데이터 검증
        if len(face_imgs) > 0:
            with self.session.as_default():
                features_faces = self.model.predict(face_imgs)
            predicted_names = [self.identify_face(features_face) for features_face in features_faces]

            # 데이터 메타데이터셋 정립
            for idx in range(len(predicted_names)):
                (cName, cPer) = predicted_names[idx]
                if cName != "???":
                    tempCoordList[idx]['labelname'] = str(cName)
                    tempCoordList[idx]['percent'] = str(round(float(cPer),2))
                    predicted_names[idx] = (cName, str(round(float(cPer),2)))
                else:
                    tempCoordList[idx]['labelname'] = "???"
                    tempCoordList[idx]['percent'] = "0"
                    predicted_names[idx] = ("???", "0")

        # draw results
        for i, face in enumerate(faces):
            label = "{}".format(predicted_names[i])
            self.draw_label(frame, (face[0], face[1]), label)

        return frame, tempCoordList