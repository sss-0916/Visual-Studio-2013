# coding=gbk

import cv2
import numpy as np
import camera_configs as cf

# 图像采集模块
# 开启摄像头
##camera = cv2.VideoCapture(0)
# 设置分辨率
##camera.set(3, 800)
##camera.set(4, 600)

while True:
    # 按帧读取图像
    ##ret, img = camera.read()
    img = cv2.imread("./img.bmp")
    cv2.imshow("img", img)
    #cv2.imwrite("img.bmp", img)

    # 转为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img_gray", img_gray)
    #cv2.imwrite("img_gray.bmp", img_gray)

    # 畸变校正
    img_undistortion = cv2.remap(img_gray, cf.map1, cf.map2, 
        interpolation = cv2.INTER_LINEAR, 
        borderMode = cv2.BORDER_CONSTANT)
    cv2.imshow("img_undistortion", img_undistortion)
    #cv2.imwrite("img_undistortion.bmp", img_undistortion)

    # 图像滤波
    img_filtered = cv2.medianBlur(img_undistortion, 5)
    cv2.imshow("img_filtered", img_filtered)
    #cv2.imwrite("img_filtered.bmp", img_filtered)

    # 图像增强（直方图均衡化）
    img_enhance = cv2.equalizeHist(img_filtered)
    cv2.imshow("img_enhance", img_enhance)
    #cv2.imwrite("img_enhance.bmp", img_enhance)

    cv2.waitKey(1)