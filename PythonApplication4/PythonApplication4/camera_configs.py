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

om = np.array([0.04541, -0.04581, -0.00146]) # ��ת��ϵ����
R = cv2.Rodrigues(om)[0]  # ʹ��Rodrigues�任��om�任ΪR
T = np.array([-204.88896, -1.52871, -9.09793]) # ƽ�ƹ�ϵ����

size = (800, 600) # ͼ��ߴ�

# �����������
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# �������map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)