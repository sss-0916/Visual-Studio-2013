#coding=gbk

# author = '张蒙蒙'
# date = '2019/03/11'

import cv2
import numpy as np

left_camera_matrix = np.array([[229.04055, 0., 402.84629],
                               [0., 230.09197, 270.90618],
                               [0., 0., 1.]])
left_distortion = np.array([[-0.07235, 0.00321, -0.00104, -0.00072, 0.00000]])

right_camera_matrix = np.array([[225.19932, 0., 389.37238],
                                [0., 225.84381, 289.43632],
                                [0., 0., 1.]])
right_distortion = np.array([[-0.06627, 0.00255, 0.00028, 0.00154, 0.00000]])

# 旋转关系矢量
om = np.array([0.04541, -0.04581, -0.00146]) 
# 使用Rodrigues变换将om变换为R
R = cv2.Rodrigues(om)[0]  
# 平移关系向量
T = np.array([-204.88896, -1.52871, -9.09793]) 

size = (800, 600) # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)

# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)