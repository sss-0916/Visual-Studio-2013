#coding=gbk

# author = '张蒙蒙'
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

# 旋转关系矢量
om = np.array([0.00700, -0.00422, -0.00376]) 
# 使用Rodrigues变换将om变换为R
R = cv2.Rodrigues(om)[0]  
# 平移关系向量
T = np.array([-122.25168, 1.17720, -1.33952]) 

size = (640, 360) # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)

# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)