#coding=gbk

import cv2
import numpy as np

# 相机内参数矩阵
camera_matrix = np.array(
    [[414.22607, 0., 381.76500],
    [0., 424.64700, 276.82032],
    [0., 0., 1.]]
    )

# 畸变校正矩阵
distortion = np.array(
    [[0.23918, -0.23275, -0.01125, 0.01405]]
    )

# 像素
size = (800, 600)

# 计算更正map
map1, map2 = cv2.fisheye.initUndistortRectifyMap(
    camera_matrix, distortion, np.eye(3), 
    camera_matrix, size, cv2.CV_16SC2
)