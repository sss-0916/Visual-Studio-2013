# coding=gbk

import cv2
import numpy as np
import camera_configs as cf

# ͼ��ɼ�ģ��
# ��������ͷ
##camera = cv2.VideoCapture(0)
# ���÷ֱ���
##camera.set(3, 800)
##camera.set(4, 600)

while True:
    # ��֡��ȡͼ��
    ##ret, img = camera.read()
    img = cv2.imread("./img.bmp")
    cv2.imshow("img", img)
    #cv2.imwrite("img.bmp", img)

    # תΪ�Ҷ�ͼ
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img_gray", img_gray)
    #cv2.imwrite("img_gray.bmp", img_gray)

    # ����У��
    img_undistortion = cv2.remap(img_gray, cf.map1, cf.map2, 
        interpolation = cv2.INTER_LINEAR, 
        borderMode = cv2.BORDER_CONSTANT)
    cv2.imshow("img_undistortion", img_undistortion)
    #cv2.imwrite("img_undistortion.bmp", img_undistortion)

    # ͼ���˲�
    img_filtered = cv2.medianBlur(img_undistortion, 5)
    cv2.imshow("img_filtered", img_filtered)
    #cv2.imwrite("img_filtered.bmp", img_filtered)

    # ͼ����ǿ��ֱ��ͼ���⻯��
    img_enhance = cv2.equalizeHist(img_filtered)
    cv2.imshow("img_enhance", img_enhance)
    #cv2.imwrite("img_enhance.bmp", img_enhance)

    cv2.waitKey(1)