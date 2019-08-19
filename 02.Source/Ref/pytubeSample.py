
#YouTube('https://www.youtube.com/watch?v=ayulNIOHvak&list=PLvImSI_94S8_XNtWN-FUWMl6ZiC2IYYqB').streams.first().download()

#from pytube import YouTube
import os
import subprocess

#yt = YouTube('https://www.youtube.com/watch?v=Iq3_phBQA_Y&has_verified=1')  # 다운로드 받고자 하는 url을 입력합니다.

# print("yt \n")
# print(yt)

#print(yt.title)
#yt.streams.first().download()


def callStream():
    """
    오류사항 존재, 개발자 GIT 을 통해 확인 필요함
    :return:
    """
    from pytube import YouTube
    yt =  YouTube('www.youtube.com/watch?v=mM8qkJVY8ks')
    #print("Title :: ", yt.title)
    #print("Thumnail URL :: ", yt.thumbnail_url)

    yt.streams.first().download()
    #yt.streams.all()

if __name__ == "__main__":
    print("Hello~")
    callStream()