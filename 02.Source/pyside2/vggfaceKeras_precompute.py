import cv2
import os, glob, pickle, platform, site
import numpy as np
from keras.engine import Model
from keras import layers, models
from keras.layers import Input
from keras_vggface.vggface import VGGFace
from keras_preprocessing import image
from keras_applications.resnet50 import ResNet50
from keras_applications.resnet50 import preprocess_input
from keras_vggface import utils


def pickleStuff(fileName, stuff):
    saveStuff = open(fileName, "wb")
    pickle.dump(stuff, saveStuff)
    saveStuff.close()

class vggFaceFaceExtractor(object):

    def __new__(cls, weight_file=None, face_size=224):
        if not hasattr(cls, 'instance'):
            cls.instance = super(vggFaceFaceExtractor, cls).__new__(cls)
        return cls.instance

    def __init__(self, face_size=224):
        self.osName = ""
        self.face_cascade = ""
        self.faceSize = face_size

    def caseSetting(self):
        """
        OS Platform 에 따른 분류
        :return:
        """
        if platform.system() == "Windows":
            self.osName = "Windows"
            # self.face_cascade = cv2.CascadeClassifier('C:\\Users\\JK\\Documents\\GitHub\\bitproject\\haarcascade_frontface.xml')
            self.face_cascade = cv2.CascadeClassifier(
                os.path.join(site.getsitepackages()[1], "cv2/data/haarcascade_frontalface_default.xml"))
        elif platform.system() == "Linux":
            self.osName = "Linux"
            # self.face_cascade = cv2.CascadeClassifier('/home/bit/anaconda3/envs/faceRecognition/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
            self.face_cascade = cv2.CascadeClassifier(
                os.path.join(site.getsitepackages()[0], "cv2/data/haarcascade_frontalface_default.xml"))

    def cropFace(self, imgarray, section, margin=20, size=224):
        """
        이미지 리스트를 crop 처리한다.
        :param imgarry: full Image
        :param section: face Detected Area (x, y, w, h)
        :param margin: add some margin to the face detected area
        :param size: result image resolution
        :return: resize image (size * size * 3)
        """

        img_h, img_w, _ = imgarray.shape

        if section is None:
            print("section is None :: ", section)
            section = [0, 0, img_w, img_h]

        print("section :: ", section)
        (x, y, w, h) = section

        margin = int(min(w,h) * margin / 100)
        x_a = x - margin
        y_a = y - margin
        x_b = x + w + margin
        y_b = y + h + margin

        # TODO : 위 값을 이용하여 박스를 그려보고 해당 위치가 무엇을 의미하는지 확인해 볼 것
        #tempBox =
        print("before if :: {}, {}, {}, {}".format(x_a, y_a, x_b, y_b))

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

        print("after if :: {}, {}, {}, {}".format(x_a, y_a, x_b, y_b))

        cropped = imgarray[y_a: y_b, x_a: x_b]
        resized_img = cv2.resize(cropped, (size, size), interpolation=cv2.INTER_AREA)
        resized_img = np.array(resized_img)
        return resized_img, (x_a, y_a, x_b - x_a, y_b - y_a)

    def extractFace(self, videoFile, saveFolder):
        """

        :param videoFile:
        :param saveFolder:
        :return:
        """
        # OS에 따라 처리분기
        self.caseSetting()

        # 0 means the default video capture device in OS
        cap = cv2.VideoCapture(videoFile)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        print("length: {}, w x h: {} x {}, fps: {}".format(length, width, height, fps))
        # infinite loop, break by key ESC
        frame_counter = 0
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                frame_counter = frame_counter + 1
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
                    cv2.imshow('Faces', frame)
                    imgfile = os.path.basename(videoFile).replace(".", "_") + "_" + str(frame_counter) + ".png"
                    imgfile = os.path.join(saveFolder, imgfile)
                    cv2.imwrite(imgfile, face_img)
            if cv2.waitKey(5) == 27:  # ESC key press
                break
            if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                # If the number of captured frames is equal to the total number of frames,
                # we stop
                break
        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()



def main():
    # pooling(opt = avg, None, max)
    resnet50Features = VGGFace(model='resnet50', include_top=False, input_shape=(224,224,3),pooling='avg')

    def image2x(imagePath):
        img = image.load_img(imagePath, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = utils.preprocess_input(x, version=1) # or version = 2
        print("x :: ")
        print(x)
        return x

    def calMeanFeature(imageFolder):
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

        batchSize = 32
        faceImageChunks = chunks(faceImages, batchSize)
        fvecs = None

        for faceImageChunk in faceImageChunks:
            images = np.concatenate([image2x(faceImage) for faceImage in faceImageChunk])
            batchFvecs = resnet50Features.predict(images)

            if fvecs is None:
                fvecs = batchFvecs
            else:
                fvecs = np.append(fvecs, batchFvecs, axis=0)

        print("fvecs :: ")
        print(fvecs)
        print("np.array(fvecs).sum(axis=0) / len(fvecs) :: ")
        print(np.array(fvecs).sum(axis=0) / len(fvecs))

        return np.array(fvecs).sum(axis=0) / len(fvecs)


    FACE_IMAGES_FOLDER = "../Ref/data/faceImages"
    VIDEOS_FOLDER = "../Ref/data/videos"
    extractor = vggFaceFaceExtractor()
    folders = list(glob.iglob(os.path.join(VIDEOS_FOLDER, "*")))
    os.makedirs(FACE_IMAGES_FOLDER, exist_ok=True)
    # names = className
    names = [os.path.basename(folder) for folder in folders]

    # video 를 읽어서 얼굴 검출 및 파일 저장
    for i, folder in enumerate(folders):
        name = names[i]
        videos = list(glob.iglob(os.path.join(folder, '*.*')))
        save_folder = os.path.join(FACE_IMAGES_FOLDER, name)
        print(save_folder)
        os.makedirs(save_folder, exist_ok=True)
        for video in videos:
            extractor.extractFace(video, save_folder)

    # 이미지를 피클 파일(바이너리)로 정리한다.
    # precompute_features = []
    # for i, folder in enumerate(folders):
    #     name = names[i]
    #     save_folder = os.path.join(FACE_IMAGES_FOLDER, name)
    #     mean_features = calMeanFeature(imageFolder=save_folder)
    #     print("mean_features :: ")
    #     print(mean_features)
    #     precompute_features.append({"name": name, "features": mean_features})
    # pickleStuff("../Ref/data/train/precompute_features.pickle", precompute_features) # pickle(binary) data save


if __name__ == "__main__":
    print("model running==============")
    main()
    print("model running End==============")