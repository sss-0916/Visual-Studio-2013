#coding=gbk

# author = '张蒙蒙'
# date = '2019/03/11'

import cv2
import numpy as np

left_camera_matrix = np.array([[247.22062, 0., 417.06144],
                               [0., 248.61726, 263.50008],
                               [0., 0., 1.]])
left_distortion = np.array([[-0.08442, 0.00503, -0.00299, -0.00107, 0.00000]])

right_camera_matrix = np.array([[249.42760, 0., 383.61715],
                                [0., 250.43797, 285.64547],
                                [0., 0., 1.]])
right_distortion = np.array([[-0.08497, 0.00517, 0.00238, 0.00035, 0.00000]])

# 旋转关系矢量
om = np.array([0.11188, 0.01626, 0.01502]) 
# 使用Rodrigues变换将om变换为R
R = cv2.Rodrigues(om)[0]  
# 平移关系向量
T = np.array([-38.49777, 0.44534, -0.11373]) 

size = (800, 600) # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)

# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)