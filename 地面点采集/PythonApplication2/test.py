#coding=gbk

import numpy as np
import cv2
#import camera_configs
import camera_configs_1 as camera_configs
#import camera_configs_2 as camera_configs
import time
import math

# 3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style

# threeD降噪后
#threeD_list = []

# 三张图形降噪
#global_threeD_list = [[0, 0, 0]] * 9216 * 4
#global_threeD_list = [[0, 0, 0]] * 160 * 120 * 3
#threeD_array_sequence = np.zeros((9216, 3, 3), dtype = np.int16)
#print(threeD_array_sequence)

# 坐标系转换
# author = "张蒙蒙"
# date = "2019/04/01"
def axesTransfer(threeD_array, angle, height):
    #list_after_axes_transfer = []
    cos_angle = math.cos(angle * math.pi / 180)
    sin_angle = math.sin(angle * math.pi / 180)

    # 旋转矩阵
    spin_matrix = np.array(
            [[1, 0, 0], 
            [0, cos_angle, sin_angle],
            [0, -sin_angle, cos_angle]]
        )

    # 平移矩阵
    translation_matrix = np.array(
            [0, height, 0]
        )

    array_after_axes_transfer = np.matmul(threeD_array, spin_matrix)
    #threeD_temp = threeD_array.reshape(128 * 72, 3)
    #threeD_temp = threeD_array.reshape(5 * 4, 3)
    #print(threeD_temp)
    #threeD_result_list = threeD_temp.tolist()
    #print(threeD_result_list)
    #for i in range(5 * 4):
        #print(threeD_result_list[i])
        #ele_result = matrixMul(threeD_result_list[i], spin_matrix, translation_matrix)
        #print(ele_result)
        #list_after_axes_transfer.append(ele_result)
        #print(list_after_axes_transfer)
    #print(list_after_axes_transfer)
    #result_temp = np.array(list_after_axes_transfer)
    #array_after_axes_transfer = result_temp.reshape(5, 4, 3)
    array_after_axes_transfer = array_after_axes_transfer + translation_matrix
    return array_after_axes_transfer

# 获取第三个元素
def takeThird(ele):
    return ele[2]

#threeD_list = []

# 块分析 -- 5 x 5区域排序降噪
# author = "张蒙蒙"
# date = "2019/03/21"
def oldBlockAnalysis(block, threeD_list):
    #print(block)
    #block.astype(np.uint8)
    #cv2.namedWindow("block", 0)
    #cv2.resizeWindow("block", 5, 5)
    #cv2.imshow("block", block)
    #print(block)
    temp = np.reshape(block, (-1, 3))
    block_list = temp.tolist()
    #print(block_list)
    block_list.sort(key = takeThird)
    threeD_list.append(block_list[13])

# 切块
def oldCutBlockAnalysis(threeD):
    x = 0
    y = 0
    # 降噪后
    threeD_list = []
    while y >= 0 and y < 600:
        while x >= 0 and x < 800:
            cut_threeD = threeD[y : y + 5, x : x + 5]
            #print(cut_threeD)
            blockAnalysis(cut_threeD, threeD_list)
            x = x + 5
        y = y + 5
        x = 0
    #while y >= 0 and y < 360:
    #    while x >= 0 and x < 640:
    #        cut_threeD = threeD[y : y + 5, x : x + 5]
    #        blockAnalysis(cut_threeD, threeD_list)
    #        x = x + 5
    #    y = y + 5
    #    x = 0
    return threeD_list

# 块分析 -- 九宫格区域降噪
# author = "张蒙蒙" 
# date = "2019/04/04"
def blockAnalysis(block, threeD_list):
    #print(block)
    #block.astype(np.uint8)
    #cv2.namedWindow("block", 0)
    #cv2.resizeWindow("block", 5, 5)
    #cv2.imshow("block", block)
    #print(block)
    #print(block)
    col_list = []
    row_1 = block[0]
    #print(row_1)
    list_1 = row_1.tolist()
    list_1.sort(key = takeThird)
    col_list.append(list_1[1])
    #print(list_1)
    #print(list_1)
    row_2 = block[1]
    list_2 = row_2.tolist()
    list_2.sort(key = takeThird)
    col_list.append(list_2[1])
    #print(row_2)
    row_3 = block[2]
    list_3 = row_3.tolist()
    list_3.sort(key = takeThird)
    col_list.append(list_3[1])
    #print(col_list)
    #print(row_3)
    #col_1 = block[:, 0, :]
    #print(col_1)
    #temp = np.reshape(block, (-1, 3))
    #print(temp)
    #block_list = temp.tolist()
    #print(block_list)
    #block_list.sort(key = takeThird)
    #print(block_list)
    col_list.sort(key = takeThird)
    threeD_list.append(col_list[1])

# 切块
def cutBlockAnalysis(threeD):
    x = 2
    y = 0
    # 降噪后
    threeD_list = []
    while y >= 0 and y < 600:
        while x >= 2 and x < 800:
            cut_threeD = threeD[y : y + 3, x : x + 3]
            #print(cut_threeD)
            blockAnalysis(cut_threeD, threeD_list)
            x = x + 3
        y = y + 3
        x = 2
    #while y >= 0 and y < 360:
    #    while x >= 0 and x < 640:
    #        cut_threeD = threeD[y : y + 5, x : x + 5]
    #        blockAnalysis(cut_threeD, threeD_list)
    #        x = x + 5
    #    y = y + 5
    #    x = 0
    return threeD_list
            
# 3D建模
# author = "白静静"
# date = "2019/03/19"
def plot3D():
    style.use('ggplot')
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')  #1行一列第一个

    #data = np.load("threeD.npy")    #读取npy数据
    #x=data[:, :, 0]
    #y=data[:, :, 1]
    #z=data[:, :, 2]

    x, y, z = axes3d.get_test_data()
    #x = cutx_threeD;
    #y = cuty_threeD;
    #z = cutz_threeD;

    print(axes3d.__file__)
    ax1.plot_wireframe(x,y,z, rstride = 3, cstride = 3)   #列数上限，行数上限

    ax1.set_xlabel('x axis')
    ax1.set_ylabel('y axis')
    ax1.set_zlabel('z axis')

    plt.show()

# list转三维矩阵
# author = "王泽"
# date = "2019/03/23"
def list2ThreeDimension(list):
    ret = np.array(list).reshape(19200, 3, 3)
    return ret;

# 三张图片降噪
# author = "白静静"
# date = "2019/03/27"
def threePictureAnalysis(threeD_array):
    temp_list = []
    for i in range(len(threeD_array)):
        index = np.lexsort([threeD_array[i][:, 2]])
        sorted_threeD_array = threeD_array[i][index, :]
        temp_list.append(sorted_threeD_array[1].tolist())
    #threeD_result = np.array(temp_list).reshape(128, 72, 3)
    threeD_result = np.array(temp_list).reshape(120, 160, 3)
    return threeD_result

# 实时显示Z轴结果
# author = "张蒙蒙"
# date = "2019/03/25"
def beforeNoiseReduction(threeD):
    cv2.namedWindow("Before Noise Reduction", 0)
    cv2.resizeWindow("Before Noise Reduction", 400, 300)
    cut_threeD = threeD[:, :, 2]
    cut_threeD = cut_threeD.astype(np.uint8)
    cv2.imshow("Before Noise Reduction", cut_threeD)

def after5X5NoiseReduction(threeD_after_block_analysis):
    cv2.namedWindow("After 5X5 Noise Reduction", 0)
    cv2.resizeWindow("After 5X5 Noise Reduction", 400, 300)
    threeD_after_block_analysis = threeD_after_block_analysis[:, :, 2]
    threeD_after_block_analysis = threeD_after_block_analysis.astype(np.uint8)
    cv2.imshow("Before Noise Reduction", threeD_after_block_analysis)
    
# 移除无效点
# author = "张蒙蒙"
# date = "2019/03/20"
def removeInvalidPoint(cut_threeD):
    #cut_data = cut_threeD.reshape(640 * 360 * 3)
    cut_data = cut_threeD.reshape(128 * 72 * 3)
    #cut_data.astype(np.int32)
    #cut_data.astype(np.int)
    #cut_data.astype(np.uint16)
    cut_data_list = cut_data.tolist()
    #print("before")
    #print(len(cut_data_list))
    #print(cut_data_list)
    #np.savetxt("before.txt", cut_data_list)
    index = 2;
    sum = 128 * 72 * 3
    #sum = 640 * 360 * 3
    while index < sum:
        if cut_data_list[index] < 0:
            cut_data_list.pop(index)
            cut_data_list.pop(index - 1)
            cut_data_list.pop(index - 2)
            sum = sum - 3
        index = index + 3
    #num = len(cut_data_list) / 3;
    #result = np.array(cut_data_list)
    #result.reshape(num, 1, 3)
    #print(result)
    #print(result)
    #np.array(cut_data_list).reshape(num, 1, 3)
    #cut_data_list.astype(np.uint16)
    print(cut_data_list)
    #cut_data_list.reshape(640, 360, 3)
    #np.save("after_remove_valid_point.npy", cut_data_list)
    #np.save("after_remove_valid_point.npy", result)
    #print("after")
    #print(len(cut_data_list))
    #np.savetxt("after.txt", cut_data_list)

# 云点图绘制
# author = "张蒙蒙"
# date = "2019/03/18"
def cloudPoint():
    #data = np.load("cut_threeD.npy")
    #data = np.load("threeD.npy")
    #data = np.load("threeD_list.npy")
    #data = np.load("threeD_array_result.npy")
    #data = np.load("threeD_after_block_analysis.npy")
    #data = np.load("threeD_array_after_axes_transfer.npy")
    data = np.load("cut_data_out.npy")

    #data = np.load("after_remove_valid_point.npy")

    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]

    #x = data[:, :, 0]
    #y = data[:, :, 1]
    #z = data[:, :, 2]

    #x = np.load("x.npy")
    #y = np.load("y.npy")
    #z = np.load("z.npy")


    #x, y, z = data[0], data[1], data[2]
    ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
    #  将数据点分成三部分画，在颜色上有区分度
    #ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
    #ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
    #ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
    ax.scatter(x, y, z, c='r')

    ax.set_zlabel('Z')  # 坐标轴
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    #ax.set_zlim(0, 10000)
    #ax.set_xlim(-6000, 6000)
    #ax.set_ylim(-6000, 6000)
    ax.set_zlim(0, 6000)
    ax.set_xlim(-4000, 4000)
    ax.set_ylim(-4000, 4000)

    plt.show()

# 自动拍照, 或手动按s拍照
AUTO = False
# 自动拍照间隔
INTERVAL = 2

counter = 0
utc = time.time()
pattern = (12, 8) # 棋盘格尺寸
# 自动
#folder = 'D:/img/img_auto/' # 拍照文件目录
# 手动
folder = 'D:/img/img_q/' # 拍照文件目录
# 单标标定左摄像头
#folder = 'D:/img/img_left/' # 拍照文件目录
# 单目标定有摄像头
#folder = 'D:/img/img_right/' # 拍照文件目录

def shot(pos, frame):
    global counter
    path = folder + pos + "_" + str(counter) + ".jpg"

    cv2.imwrite(path, frame)
    print("snapshot saved into: " + path)

#def shot1(pos, frame):
#    global counter
#    path = folder + pos + str(counter) + ".jpg"

#    cv2.imwrite(path, frame)
#    print("snapshot saved into: " + path)

cv2.namedWindow("left", 0)
cv2.namedWindow("right", 0)
cv2.namedWindow("depth")
cv2.moveWindow("left", 0, 0)
#cv2.moveWindow("right", 600, 0)
#cv2.moveWindow("right", 800, 0)
cv2.moveWindow("right", 404, 0)
#cv2.moveWindow("depth", 808, 0)
#cv2.resizeWindow("left", 640, 360)
#cv2.resizeWindow("right", 640, 360)
#cv2.resizeWindow("left", 800, 600)
#cv2.resizeWindow("right", 800, 600)
cv2.resizeWindow("left", 400, 300)
cv2.resizeWindow("right", 400, 300)
cv2.createTrackbar("num", "depth", 0, 10, lambda x: None)
#cv2.createTrackbar("num", "depth", 0, 8, lambda x: None)
#cv2.createTrackbar("blockSize", "depth", 5, 255, lambda x: None)
#cv2.createTrackbar("blockSize", "depth", 10, 255, lambda x: None)
cv2.createTrackbar("blockSize", "depth", 15, 255, lambda x: None)
camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(1)

# 设置分辨率640x360
camera1.set(3, 800)
camera1.set(4, 600)
camera2.set(3, 800)
camera2.set(4, 600)
#camera1.set(3, 640)
#camera1.set(4, 360)
#camera2.set(3, 640)
#camera2.set(4, 360)

# 添加点击事件，打印当前点的距离
def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:        
        print (threeD[y][x])
        print(x)
        print(y)

#def pritThreeD(e, x, y, f, p):
#    print(threeD[y][x])

cv2.setMouseCallback("depth", callbackFunc, None)

cut_data_array = np.zeros((160 * 120, 3), dtype = np.int16)

while True:
    ret1, frame1 = camera1.read()
    ret2, frame2 = camera2.read()
    #frame1 = cv2.imread("D:\left_0.bmp")
    #frame2 = cv2.imread("D:\right_0.bmp")
    #ret1 = 1;
    #ret2 = 1;

    # 自动拍照
    #now = time.time()
    #if AUTO and now - utc >= INTERVAL:
    #    shot("left", frame1)
    #    shot("right", frame2)
    #    counter += 1
    #    utc = now

    # 手动拍照
    #key = cv2.waitKey(1)
    #if key == ord('q'):
    #    break
    #elif key == ord('s'):
    #    shot("left", frame1)
    #    shot("right", frame2)
    #    counter += 1

    if not ret1 or not ret2:
        break

    #cv2.imshow("left", frame1)
    #cv2.imshow("right", frame2)

    # 根据更正map对图片进行重构
    img1_rectified = cv2.remap(frame1, camera_configs.left_map1, 
                camera_configs.left_map2, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(frame2, camera_configs.right_map1, 
                camera_configs.right_map2, cv2.INTER_LINEAR)

    #cut_left = img1_rectified[10 : 1260, 10 : 710]
    #cut_right = img2_rectified[10 : 1260, 10 : 710]

    #cv2.imshow("left", cut_left)
    #cv2.imshow("right", cut_right)

    #cv2.imshow("left", img1_rectified)
    #cv2.imshow("right", img2_rectified)

    #new_left = cv2.resize(img1_rectified, (640, 360))
    #new_right = cv2.resize(img2_rectified, (640, 360))

    #cv2.imshow("left", new_left)
    #cv2.imshow("right", new_right)

    # 将图片置为灰度图，为StereoBM作准备
    imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("left", imgL)
    #cv2.imshow("right", imgR)

    # 两个trackbar用来调节不同的参数查看效果
    num = cv2.getTrackbarPos("num", "depth")
    blockSize = cv2.getTrackbarPos("blockSize", "depth")
    if blockSize % 2 == 0:
        blockSize += 1
    if blockSize < 5:
        blockSize = 5

    # 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法，有兴趣可以试试）
    stereo = cv2.StereoBM_create(numDisparities=16*num, blockSize=blockSize)
    #stereo = cv2.StereoBM_create(64, 10)
    disparity = stereo.compute(imgL, imgR)

    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # 将图片扩展至3d空间中，其z方向的值则为当前的距离
    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32)/16., camera_configs.Q)

    #y = 0
    #for y in range(600):
    #    z = 650 / (np.cos (58 * math.pi / 180 + np.arctan((300 - y) / 650)))
    #    temp = threeD[y, :]
    #    temp[temp < y] = -1

    #print(threeD)

    #print(threeD.shape)

    #threeD = axesTransfer(threeD, 30, 650)

    #threeD1 = axesTransfer(threeD, 30, 0)

    #threeD = threeD1.copy()

    #np.save("threeD.npy", threeD)

    #print(threeD)
    # threeD转为整数
    #threeD = threeD.astype(np.uint16)

    #print(cut_threeD)

    #cut_threeD = threeD[:, :, 1]
    #print(cut_threeD)

    #print(threeD)
    #cv2.namedWindow("three", 0)
    #cv2.resizeWindow("three", 640, 360)
    #cv2.imshow("three", threeD)
    #print(threeD)

    #zDisplay(threeD)

    # 降噪之前Z实时显示
    #beforeNoiseReduction(threeD)

    # 九宫格降噪
    #threeD_list = cutBlockAnalysis(threeD)

    # 5 x 5区域排序降噪
    # 降噪结果放在threeD_list中
    #threeD_list = cutBlockAnalysis(threeD)
    #threeD_list = cutBlockAnalysis(threeD)
    #print(len(threeD_list))
    #print(threeD_list)
    #print(threeD_list)

    #threeD_after_block_analysis = np.array(threeD_list).reshape(120, 160, 3)
    #threeD_after_block_analysis = np.array(threeD_list).reshape(200, 266, 3)

    # 九宫格降噪后Z实时显示
    #after5X5NoiseReduction(threeD_after_block_analysis)

    #cv2.namedWindow("After Nine Noise Reduction", 0)
    #cv2.resizeWindow("After Nine Noise Reduction", 400, 300)
    #threeD_after_block_analysis = threeD_after_block_analysis[:, :, 2]
    #threeD_after_block_analysis = threeD_after_block_analysis.astype(np.uint8)
    #cv2.imshow("After Nine Noise Reduction", threeD_after_block_analysis)

    # 5 x 5降噪之后Z实时显示
    #after5X5NoiseReduction(threeD_after_block_analysis)
    #cv2.namedWindow("After 5X5 Noise Reduction", 0)
    #cv2.resizeWindow("After 5X5 Noise Reduction", 400, 300)
    #threeD_after_block_analysis = threeD_after_block_analysis[:, :, 2]
    #threeD_after_block_analysis = threeD_after_block_analysis.astype(np.uint8)
    #cv2.imshow("After 5X5 Noise Reduction", threeD_after_block_analysis)

    #np.save("threeD_after_block_analysis.npy", threeD_after_block_analysis)

    #threeD_after_block_analysis = list2ThreeDimension(threeD_list)
    #print(threeD_list)

    #after5X5NoiseReduction(threeD_list)

    # 三张图像降噪
    # 降噪结果放在threeD_array_result中
    #global_threeD_list = global_threeD_list + threeD_list
    #global_threeD_list = global_threeD_list[9216 : 9216 * 4]
    #global_threeD_list = global_threeD_list[19200 : 19200 * 4]
    #print(len(global_threeD_list))

    # threeD_array 为9216 x 3 x 3矩阵
    # threeD_array 为19200 x 3 x 3矩阵
    # 是三张图像拼在一起的
    #threeD_array = list2ThreeDimension(global_threeD_list)

    # 将threeD_array三张图的对应像素点的(x, y, z)按z进行排序
    # 取z值位于中间对应的像素点作为最终结果
    # 结果19200 x 1 x 3
    # 再将其转为160 x 120 x 3
    # 结果9216 x 1 x 3
    # 再将其转为128 x 72 x 3
    #threeD_array_result = threePictureAnalysis(threeD_array)    

    # 降噪之后的结果
    #np.save("threeD_array_result.npy", threeD_array_result)

    # 坐标系转换
    #threeD_array_after_axes_transfer = axesTransfer(threeD_array_result, 30, 0)
    #threeD_array_after_axes_transfer = threeD_array_after_axes_transfer.astype(np.int16)
    # 坐标系转换之后的结果
    #np.save("threeD_array_after_axes_transfer.npy", threeD_array_after_axes_transfer)

    #print(threeD_array_after_axes_transfer)
    #print(threeD_array_result)

    #threeD_after_noise_reduction = threeD_array_result.copy()
    #cv2.namedWindow("After Noise Reduction", 0)
    #cv2.resizeWindow("After Noise Reduction", 640, 360)
    #cut_threeD_after_noise_reduction = threeD_after_noise_reduction[:, :, 2]
    #cut_threeD_after_noise_reduction = cut_threeD_after_noise_reduction.astype(np.uint8)
    #cv2.imshow("Before Noise Reduction", cut_threeD_after_noise_reduction)

    #print(threeD_array_result)

    #print(len(global_threeD_list))
    #print(len(threeD_list))
    #threeD_array = np.array(threeD_list)
    #threeD_array.reshape(9216, 1, 3)
    #print(threeD_list)

    #cut_threeD = threeD[threeD > 0];
    #cut_threeD[cut_threeD < 0] = 1500
    #cut_threeD[cut_threeD > 1400] = 1400
    #cut_threeD = cut_threeD.astype(np.uint16)
    
    #np.save("threeD.npy", threeD)
    #cut_threeD = threeD[0 : 360 : 90, 0 : 640 : 120, ]
    # 坐标
    #cut_threeD = threeD[0 : 360 : 5, 0 : 640 : 5,]
    #cut_threeD = cut_threeD.astype(np.uint16)
    # 横坐标
    #cutx_threeD = threeD[0 : 360 : 5, 0 : 640 : 5, 0]
    # 纵坐标
    #cuty_threeD = threeD[0 : 360 : 5, 0 : 640 : 5, 1]
    # 竖坐标
    #cutz_threeD = threeD[0 : 360 : 5, 0 : 640 : 5, 2]

    #np.save("cut_threeD.npy", cut_threeD)

    #np.save("x.npy", cutx_threeD)
    #np.save("y.npy", cuty_threeD)
    #np.save("z.npy", cutz_threeD)

    #np.savetxt("x.txt", cutx_threeD)
    #cut_threeD = cut_threeD.astype(np.uint16)
    #print(cut_threeD)

    #threeD = threeD.astype(np.uint16)

    #print(threeD)
    #for x in range(0, 128):
    #    for y in range(0, 72):
    #        print(cut_threeD[y][x])

    #print(len(threeD[2]))

    # 对像素点进行隔5采样
    # 1
    #cut_threeD = threeD[0 : 600 : 5, 0 : 800 : 5, 2]
    #print(cut_threeD.shape)
    #print(cut_threeD)

    # 2
    #for y in range(120):
    #    z = 650 / (np.cos(58 * math.pi / 180 + np.arctan((300 - y * 5) / 650)))
    #    temp = cut_threeD[y, :]
    #    temp[temp > z] = -1

    # 将单位转换为厘米
    # 3
    #cut_threeD = cut_threeD / 10

    # 4
    #cut_threeD[cut_threeD < 0] = 26000

    # 5
    #cut_threeD = cut_threeD.astype(np.uint16)

    # 6
    #interval_sampling = cut_threeD.copy()

    # 7
    #interval_sampling[interval_sampling > 25000] = 0

    # 采样之后
    # 8
    #cv2.namedWindow("interval sampling", 0)
    #cv2.resizeWindow("interval sampling", 400, 300)
    #cv2.moveWindow("interval sampling", 0, 335)
    #interval_sampling = interval_sampling.astype(np.uint8)
    #cv2.imshow("interval sampling", interval_sampling)

    # 转成1列
    # 9
    #cut_data = cut_threeD.reshape(160 * 120, 1)

    # 剔除过期数据
    # 10
    #cut_data_array = cut_data_array[:, 0 : 2]

    # 引入最新一帧
    # 11
    #cut_data_array = np.concatenate((cut_data, cut_data_array), axis = 1)

    # 12
    #cut_data_sequence = cut_data_array.copy()

    # 对三帧图像的相同像素点处的距离进行排序
    # 13
    #cut_data_sequence.sort(axis = 1)

    # 取最小的距离进行判断
    # 14
    #cut_data_mask = cut_data_sequence[:, 2]

    # 取中值
    # 15
    #cut_data_out = cut_data_sequence[:, 1]

    # 16
    #cut_data_out[cut_data_mask > 25000] = 26000

    # 17
    #cut_data_out = cut_data_out.reshape(120, 160)

    # 18
    #cut_data_out[cut_data_out > 25000] = 0
    #cv2.namedWindow("noise reduction", 0)
    #cv2.resizeWindow("noise reduction", 400, 300)
    #cv2.moveWindow("noise reduction", 404, 335)
    #cut_data_out = cut_data_out.astype(np.uint8)
    #cv2.imshow("noise reduction", cut_data_out)

    cv2.imshow("left", img1_rectified)
    cv2.imshow("right", img2_rectified)
    #disp = disp[20 : 340, 80 : 620]
    cv2.imshow("depth", disp)

    # 自动拍照
    #now = time.time()
    #if AUTO and now - utc >= INTERVAL:
    #    shot("left", frame1)
    #    shot("right", frame2)
    #    counter += 1
    #    utc = now

    # 手动拍照
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        #np.savetxt("cut_threeD.txt", cut_threeD)
        #a = np.loadtxt("cut_threeD.txt")

        #for x in range(0, 128):
        #    for y in range(0, 72):
        #        #print(cutx_threeD[y][x])
        #        print(cut_threeD[y][x])
        #        np.savetxt("test.txt", cut_threeD[y][x])
        #np.save("threeD.npy", threeD)
        #a = np.load("threeD.npy")
        #print(a)

        #plot3D()

        #removeInvalidPoint(cut_threeD)
        #removeInvalidPoint(threeD)

        #cloudPoint()
        #cloudPoint()

        #cutBlockAnalysis(threeD)
        #threeD_list = map(int, threeD_list)
        #print(threeD_list)
        #temp = np.array(threeD_list)
        #temp.reshape(20736, 1)
        #temp.reshape(128, 72, 3)
        #print(temp)
        #np.save("threeD_list.npy", threeD_list)
        #np.save("threeD_array_result.npy", threeD_array_result)
        #np.save("threeD_array_after_axes_transfer.npy", threeD_array_after_axes_transfer)
        #np.save("threeD_after_block_analysis.npy", threeD_after_block_analysis)
        #np.save("threeD_array_result.npy", threeD_array_result)
        #cloudPoint()

        #print(len(threeD_list))

        #threeD_array_after_axes_transfer_y = threeD_array_after_axes_transfer[:, :, 1]
        #print(threeD_array_after_axes_transfer)
        #print(threeD_array_after_axes_transfer_y)

        #print(threeD_array)
        #print(threeD_array_result)

        #print(global_threeD_list)
        #print(len(global_threeD_list))

        #threeD_array_sequence = np.concatenate((threeD_array, threeD_array_sequence), axis = 1)
        #print(threeD_array_sequence)

        #np.save("cut_data_out.npy", cut_data_out)

        shot("left", frame1)
        shot("right", frame2)
        counter += 1

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("./snapshot/BM_left.jpg", imgL)
        cv2.imwrite("./snapshot/BM_right.jpg", imgR)
        cv2.imwrite("./snapshot/BM_depth.jpg", disp)

camera1.release()
camera2.release()
cv2.destroyAllWindows()