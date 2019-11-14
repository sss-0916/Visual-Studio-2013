#coding=gbk

#from multiprocessing import Process, Queue
import numpy as np
import cv2
#import camera_configs_1 as camera_configs
import camera_configs_2 as camera_configs
import math

cv2.namedWindow("left", 0)
cv2.namedWindow("right", 0)
cv2.namedWindow("depth")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 404, 0)
cv2.resizeWindow("left", 400, 300)
cv2.resizeWindow("right", 400, 300)
cv2.createTrackbar("num", "depth", 0, 10, lambda x: None)
cv2.createTrackbar("blockSize", "depth", 15, 255, lambda x: None)

#camera1 = cv2.VideoCapture(0)
#camera2 = cv2.VideoCapture(1)

# 设置分辨率800×600
#camera1.set(3, 800)
#camera1.set(4, 600)
#camera2.set(3, 800)
#camera2.set(4, 600)

# 添加点击事件，打印当前点的距离
def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:        
        print(threeD[y][x])
        print(x)
        print(y)

cv2.setMouseCallback("depth", callbackFunc, None)

# 地面滤除
#ground_filter = [
#    36863, 34807, 32867, 31037, 29313, 
#    27689, 26160, 24721, 23368, 22096, 
#    20900, 19777, 18723, 17734, 16806, 
#    15936, 15121, 14357, 13641, 12971, 
#    12344, 11757, 11207, 10693, 10212, 
#    9762, 9341, 8947, 8579, 8234, 
#    7910, 7608, 7324, 7058, 6808, 
#    6573, 6352, 6145, 5949, 5765, 
#    5590, 5426, 5270, 5122, 4981, 
#    4848, 4720, 4599, 4483, 4372, 
#    4265, 4163, 4065, 3970, 3879, 
#    3791, 3706, 3624, 3544, 3467, 
#    3393, 3321, 3250, 3182, 3116, 
#    3052, 2990, 2930, 2872, 2815, 
#    2760, 2707, 2656, 2606, 2558, 
#    2511, 2466, 2422, 2381, 2340, 
#    2301, 2263, 2227, 2192, 2159, 
#    2126, 2095, 2065, 2036, 2008, 
#    1981, 1954, 1929, 1904, 1881, 
#    1857, 1835, 1812, 1791, 1769, 
#    1748, 1728, 1707, 1687, 1668, 
#    1648, 1629, 1610, 1591, 1573, 
#    1556, 1539, 1522, 1507, 1492, 
#    1479, 1467, 1458, 1450, 1444
#]
ground_filter = [
    36663, 34607, 32667, 30837, 29113, 27489, 25960, 24521, 23168, 21896, 
    20700, 19577, 18523, 17534, 16606, 15736, 14921, 14157, 13441, 12771, 
    12144, 11557, 11007, 10493, 10012, 9562, 9141, 8747, 8379, 8034, 
    7710, 7408, 7124, 6858, 6608, 6373, 6152, 5945, 5749, 5565, 
    5390, 5226, 5070, 4922, 4781, 4648, 4520, 4399, 4283, 4172, 
    4065, 3963, 3865, 3770, 3679, 3591, 3506, 3424, 3344, 3267, 
    3193, 3121, 3050, 2982, 2916, 2852, 2790, 2730, 2672, 2615, 
    2560, 2507, 2456, 2406, 2358, 2311, 2266, 2222, 2181, 2140, 
    2101, 2063, 2027, 1992, 1959, 1926, 1895, 1865, 1836, 1808, 
    1781, 1754, 1729, 1704, 1681, 1657, 1635, 1612, 1591, 1569, 
    1548, 1528, 1507, 1487, 1468, 1448, 1429, 1410, 1391, 1373, 
    1356, 1339, 1322, 1307, 1292, 1279, 1267, 1258, 1250, 1244
]

#for y in range(120):
#    ground_filter[y] -= 200

for y in range(28):
    ground_filter[y + 36] -= 180

#print(ground_filter)

# 数字降噪
digital_noise_reduction = np.zeros((160 * 120, 3), 
    dtype = np.int16)

#camera_swap_flag = False

while True:
    # 按下's'交换摄像头
    #key = cv2.waitKey(1)
    #if key == ord('s'):
    #    camera_swap_flag = not camera_swap_flag

    # 摄像头交换
    #if camera_swap_flag:
    #    ret1, frame1 = camera2.read()
    #    ret2, frame2 = camera1.read()
    #else:
    #    ret1, frame1 = camera1.read()
    #    ret2, frame2 = camera2.read()

    #if not ret1 or not ret2:
    #    break

    #frame1 = cv2.imread('D:/img/img_ground/left_12.bmp')
    #frame2 = cv2.imread('D:/img/img_ground/right_12.bmp')

    #frame1 = cv2.imread('D:/img/img_ground/left_3.bmp')
    #frame2 = cv2.imread('D:/img/img_ground/right_3.bmp')

    frame1 = cv2.imread('D:/img/img_people/left_8.bmp')
    frame2 = cv2.imread('D:/img/img_people/right_8.bmp')

    # 根据更正map对图片进行重构
    img1_rectified = cv2.remap(frame1, camera_configs.left_map1, 
        camera_configs.left_map2, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(frame2, camera_configs.right_map1, 
        camera_configs.right_map2, cv2.INTER_LINEAR)

    # 将图片置为灰度图，为StereoBM作准备
    imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)

    # 两个trackbar用来调节不同的参数查看效果
    num = cv2.getTrackbarPos("num", "depth")
    blockSize = cv2.getTrackbarPos("blockSize", "depth")
    if blockSize % 2 == 0:
        blockSize += 1
    if blockSize < 5:
        blockSize = 5

    # 根据Block Maching方法生成差异图
    stereo = cv2.StereoBM_create(numDisparities=16 * num, blockSize=blockSize)

    disparity = stereo.compute(imgL, imgR)

    disp = cv2.normalize(disparity, disparity, 
        alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # 将图片扩展至3d空间中，其z方向的值则为当前的距离
    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32) / 16.,
        camera_configs.Q)

    threeD = threeD.astype(np.int16)

    # 对threeD进行间隔5采样
    sampling_threeD = threeD[0 : 600 : 5, 0 : 800 : 5, 2]
    #print(sampling_threeD)

    # 地面滤除
    for y in range(120):
        temp = sampling_threeD[y, :]
        #print(temp)
        #print(ground_filter[y])
        temp[temp > ground_filter[y]] = 15000
        #print(temp)
        #temp[temp > ground_filter[y]] = 26000

    #print(sampling_threeD)

    # 将单位转换为厘米
    sampling_threeD = sampling_threeD / 10
    #print(sampling_threeD)
    sampling_threeD[sampling_threeD > 1400] = 1400
    sampling_threeD[sampling_threeD < 0] = 1500
    # 转成无符号整型
    sampling_threeD = sampling_threeD.astype(np.uint16)
    #print(sampling_threeD)

    # 采样
    sampling_result = sampling_threeD.copy()
    #sampling_result[sampling_result > 25000] = 0

    # 采样后效果显示
    sampling_result = sampling_result / 5.88
    cv2.namedWindow("interval sampling", 0)
    #cv2.resizeWindow("interval sampling", 400, 300)
    #cv2.moveWindow("interval sampling", 0, 335)
    sampling_result = sampling_result.astype(np.uint8)
    cv2.imshow("interval sampling", sampling_result)

    # 数字降噪
    dnr_temp = sampling_threeD.reshape(160 * 120, 1) 
    # 剔除过期数据
    digital_noise_reduction = digital_noise_reduction[:, 0 : 2]
    # 引入最新一帧
    digital_noise_reduction = np.concatenate((dnr_temp, digital_noise_reduction), 
        axis = 1)
    dnr_multiframe = digital_noise_reduction.copy()
    # 对三帧图像的相同像素点处的距离进行排序
    dnr_multiframe.sort(axis = 1)
    # 取最小的距离进行判断
    dnr_mask = dnr_multiframe[:, 2]
    # 取中值
    dnr_result = dnr_multiframe[:, 1]
    dnr_result[dnr_mask > 1400] = 1500
    dnr_result = dnr_result.reshape(120, 160)
    #dnr_result[dnr_result > 25000] = 0
    dnr_result_show = dnr_result.copy()

    # 数字降噪后效果显示
    dnr_result_show = dnr_result_show / 5.88
    cv2.namedWindow("digital noise reduction", 0)
    #cv2.resizeWindow("digital noise reduction", 400, 300)
    #cv2.moveWindow("digital noise reduction", 404, 335)
    dnr_result_show = dnr_result_show.astype(np.uint8)
    cv2.imshow("digital noise reduction", dnr_result_show)

    # 列排序
    dnr_result.sort(axis = 0)
    distance_result = dnr_result[20, :]
    distance_result = distance_result.reshape(160)

    #print(distance_result)

    cv2.namedWindow("sort by distance", 0)
    #cv2.resizeWindow("sort by distance", 400, 300)
    #cv2.moveWindow("sort by distance", 404, 335)
    distance_sort_show = dnr_result.copy()
    distance_sort_show = distance_sort_show / 5.88
    distance_sort_show = distance_sort_show.astype(np.uint8)
    cv2.imshow("sort by distance", distance_sort_show)

    cv2.imshow("left", img1_rectified)
    cv2.imshow("right", img2_rectified)
    cv2.imshow("depth", disp)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("./snapshot/BM_left.jpg", imgL)
        cv2.imwrite("./snapshot/BM_right.jpg", imgR)
        cv2.imwrite("./snapshot/BM_depth.jpg", disp)