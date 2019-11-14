#coding=gbk

# author = '������'
# date = '2019/03/11'

import cv2
import numpy as np

left_camera_matrix = np.array([[408.27126, 0., 325.69904],
                               [0., 409.60095, 184.20470],
                               [0., 0., 1.]])
left_distortion = np.array([[0.02221, -0.05677, -0.00016, -0.00029, 0.00000]])

right_camera_matrix = np.array([[407.73455, 0., 341.68274],
                                [0., 409.06746, 196.48607],
                                [0., 0., 1.]])
right_distortion = np.array([[0.01217, -0.03439, 0.00059, -0.00080, 0.00000]])

# ��ת��ϵʸ��
om = np.array([0.00700, -0.00422, -0.00376]) 
# ʹ��Rodrigues�任��om�任ΪR
R = cv2.Rodrigues(om)[0]  
# ƽ�ƹ�ϵ����
T = np.array([-122.25168, 1.17720, -1.33952]) 

size = (640, 360) # ͼ��ߴ�

# �����������
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)

# �������map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)