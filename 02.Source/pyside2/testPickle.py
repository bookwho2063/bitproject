import cv2
import os, glob, pickle, platform, site, datetime


def load_stuff(filename):
    """
    피클 파일 로드
    :param filename:
    :return:
    """
    saved_stuff = open(filename, "rb")
    stuff = pickle.load(saved_stuff)
    saved_stuff.close()
    print("=====loaded stuff success :: ", filename)
    print("stuff :: ", stuff)
    return stuff


if __name__ == "__main__":
    load_stuff("../dev/BtiProject/00.Resource/data/pickle/savePickle_20191029145645.pickle20191029145814.pickle")
    load_stuff("../dev/BtiProject/00.Resource/data/pickle/savePickle_20191029145645.pickle20191029145814.pickle")