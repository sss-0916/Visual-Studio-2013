#coding=gbk

import numpy as np
import cv2
import camera_configs

cv2.namedWindow("left")
#cv2.namedWindow("right")
cv2.moveWindow("left", 0, 0)
#cv2.moveWindow("right", 600, 0)
camera1 = cv2.VideoCapture(0)
#camera2 = cv2.VideoCapture(0)

camera1.set(3, 800)
camera1.set(4, 600)
#camera2.set(3, 800)
#camera2.set(4, 600)

while True:
    ret1, frame1 = camera1.read()
    #ret2, frame2 = camera2.read()

    # 根据更正map对图片进行重构
    img1_rectified = cv2.remap(frame1, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
    #img2_rectified = cv2.remap(frame2, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)

    cv2.imshow("left", img1_rectified)
    #cv2.imshow("right", img2_rectified)

    key = cv2.waitKey(1)

camera1.release()
camera2.release()
cv2.destroyAllWindows()