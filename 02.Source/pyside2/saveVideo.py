import cv2



"""
frame 번호 순서대로 write 처리한다.
:param frameList:
:return:
"""

cap = cv2.VideoCapture("/home/bit/Downloads/bp3.mp4")
fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
out = cv2.VideoWriter("./extVideo.avi", fcc, fps, (int(width), int(height)))

while True:
    cur_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
    cnt_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    if cur_frame == cnt_frame:
        cap.open("/home/bit/Downloads/bp3.mp4")

    print("cur_frame :: ", int(cur_frame))
    print("cnt_frame :: ", int(cnt_frame))

    ret, frame = cap.read()
    print("before :: ", int(cur_frame))
    if int(cur_frame) > 500 and int(cur_frame) < 2000:
        print("write fps :: ", int(cur_frame))
        out.write(frame)

    if cur_frame == 2000 or cur_frame > 2000:
        out.release()
        cap.release()
        break

out.release()
cap.release()
