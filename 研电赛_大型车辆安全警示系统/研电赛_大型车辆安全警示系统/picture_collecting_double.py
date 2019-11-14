#coding=gbk

# scholiast = '张蒙蒙'
# date = '2019/03/11'
import cv2
import time

# 自动拍照, 或手动按s拍照
AUTO = False
# 自动拍照间隔
INTERVAL = 2

cv2.namedWindow("left", 0)
cv2.namedWindow("right", 0)
cv2.moveWindow("left", 0, 0)
#cv2.moveWindow("right", 960, 0)
cv2.moveWindow("right", 0, 365)
cv2.resizeWindow("left", 540 * 4, 120 * 4)
cv2.resizeWindow("right", 540 * 4, 120 * 4)
left_camera = cv2.VideoCapture(0)
right_camera = cv2.VideoCapture(1)

# 设置左右摄像头的分辨率
#left_camera.set(3, 1280)
#left_camera.set(4, 960)
#right_camera.set(3, 1280)
#right_camera.set(4, 960)
left_camera.set(3, 640)
left_camera.set(4, 360)
right_camera.set(3, 640)
right_camera.set(4, 360)

counter = 0
utc = time.time()
pattern = (12, 8) # 棋盘格尺寸
# 自动
#folder = 'D:/img/img_auto/' # 拍照文件目录
# 手动
folder = 'D:/img/img_binocular/' # 拍照文件目录
# 单标标定左摄像头
#folder = 'D:/img/img_left/' # 拍照文件目录
# 单目标定有摄像头
#folder = 'D:/img/img_right/' # 拍照文件目录

def shot(pos, frame):
    global counter
    path = folder + pos + "_" + str(counter) + ".bmp"

    cv2.imwrite(path, frame)
    print("snapshot saved into: " + path)

while True:
    ret, left_frame = left_camera.read()
    ret, right_frame = right_camera.read()

    #CutImg1 = Left[60:180, 50:590]  # y x
    #CutImg2 = Right[71:191, 50:590]  # y x
    cut_left = left_frame[60 : 180, 50 : 590]
    cut_right = right_frame[60 : 180, 50 : 590]

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        shot("left", cut_left)
        shot("right", cut_right)
        counter += 1

    # 画线
    #green = (0, 255, 0)
    #cv2.line(left_frame, (400, 0), (400, 600), green)
    #cv2.line(left_frame, (0, 300), (800, 300), green)
    #cv2.line(right_frame, (400, 0), (400, 600), green)
    #cv2.line(right_frame, (0, 300), (800, 300), green)

    #cv2.line(right_frame, (360, 0), (360, 960), green)
    #cv2.line(right_frame, (0, 480), (720, 480), green)
    #cv2.line(left_frame, (0, 360), (960, 360), green)
    #cv2.line(left_frame, (480, 0), (480, 720), green)
    #cv2.line(right_frame, (0, 360), (960, 360), green)
    #cv2.line(right_frame, (480, 0), (480, 720), green)

    cv2.imshow("left", cut_left)
    cv2.imshow("right", cut_right)

    # 画线
    #green = (0, 255, 0)
    #cv2.line(left_frame, (0, 0), (300, 300), green)

    now = time.time()
    if AUTO and now - utc >= INTERVAL:
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1
        utc = now

    #key = cv2.waitKey(1)
    #if key == ord('q'):
    #    break
    #elif key == ord('s'):
    #    shot("left", left_frame)
    #    shot("right", right_frame)
    #    counter += 1

left_camera.release()
right_camera.release()
cv2.destroyWindow("left")
cv2.destroyWindow("right")