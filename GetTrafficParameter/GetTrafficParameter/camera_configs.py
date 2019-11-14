#coding=gbk

import cv2
import numpy as np

# ����ڲ�������
camera_matrix = np.array(
    [[414.22607, 0., 381.76500],
    [0., 424.64700, 276.82032],
    [0., 0., 1.]]
    )

# ����У������
distortion = np.array(
    [[0.23918, -0.23275, -0.01125, 0.01405]]
    )

# ����
size = (800, 600)

# �������map
map1, map2 = cv2.fisheye.initUndistortRectifyMap(
    camera_matrix, distortion, np.eye(3), 
    camera_matrix, size, cv2.CV_16SC2
)