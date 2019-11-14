#coding=gbk

import cv2
import numpy as np

# up����ڲ�������
up_camera_matrix = np.array([[414.22607, 0., 381.76500],
                            [0., 424.64700, 276.82032],
                            [0., 0., 1.]])
# ����У������
up_distortion = np.array([[0.23918, -0.23275, -0.01125, 0.01405]])

# left����ڲ�������
left_camera_matrix = np.array([[414.37962, 0., 286.74291],
                               [0., 417.22665, 121.16955],
                               [0., 0., 1.]])
# ����У������
left_distortion = np.array([[-0.00149, -0.00919, -0.00317, -0.00459, 0.00000]])

# right����ڲ�������
right_camera_matrix = np.array([[413.68210, 0., 286.74291],
                                [0., 414.51679, 121.16955],
                                [0., 0., 1.]])
# ����У������
right_distortion = np.array([[0.01589, -0.03604, -0.00123, 0.00890, 0.00000]])

# ��ת��ϵʸ��
om = np.array([0.00275, -0.03283, -0.00128]) 
# ʹ��Rodrigues�任��om�任ΪR
R = cv2.Rodrigues(om)[0]  
# ƽ�ƹ�ϵ����
T = np.array([-121.09338, -2.22954, 0.06574]) 

# left,right���ͼ��ߴ�
left_right_size = (540, 120) 

# up���ͼ��ߴ�
up_size = (800, 600)

# �����������
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(
    left_camera_matrix, left_distortion, right_camera_matrix, 
    right_distortion, left_right_size, R, T
)

# ˫ĿУ׼�������map
left_map1, left_map2 = cv2.initUndistortRectifyMap(
    left_camera_matrix, left_distortion, R1, P1, left_right_size, cv2.CV_16SC2
)
right_map1, right_map2 = cv2.initUndistortRectifyMap(
    right_camera_matrix, right_distortion, R2, P2, left_right_size, cv2.CV_16SC2
)

# ��ĿУ׼�������map
up_map1, up_map2 = cv2.fisheye.initUndistortRectifyMap(
    up_camera_matrix, up_distortion, np.eye(3), up_camera_matrix, up_size,cv2.CV_16SC2
)