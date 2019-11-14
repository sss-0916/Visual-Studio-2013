#coding=gbk

# author = '张蒙蒙'
# date = '2019/03/11'

import cv2
import numpy as np

left_camera_matrix = np.array([[797.58967, 0., 631.26410],
                               [0., 800.39419, 186.55679],
                               [0., 0., 1.]])
left_distortion = np.array([[0.01009, -0.03489, -0.00151, -0.00476, 0.00000]])

right_camera_matrix = np.array([[796.76386, 0., 668.37217],
                                [0., 800.07048, 191.98687],
                                [0., 0., 1.]])
right_distortion = np.array([[0.00082, -0.02273, -0.00119, -0.00415, 0.00000]])

# 旋转关系矢量
om = np.array([0.00754, -0.00717, -0.00376]) 
# 使用Rodrigues变换将om变换为R
R = cv2.Rodrigues(om)[0]  
# 平移关系向量
T = np.array([-123.66249, 1.90924, -0.83691]) 

size = (1280, 360) # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)

# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)