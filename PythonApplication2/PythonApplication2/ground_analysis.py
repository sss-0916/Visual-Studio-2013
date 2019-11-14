#coding=gbk

import cv2
import numpy as np

#cv2.namedWindow("random", 0)
#cv2.namedWindow("rgb", 0)

#随机生成一个5*3*3的矩阵
#a = np.random.randint(-50,50,size=(5,3,3))
#print(a)
#a = a.astype(np.uint8)

#b = np.random.randint(254 ,255 ,size=(5,3,3))

#b = np.zeros((5, 3, 3))

#b = np.array(
#    [[[255, 255, 255], 
#      [255, 255, 255],
#      [255, 255, 255]],
#     [[255, 255, 255],
#      [255, 255, 255], 
#      [255, 255, 255]],
#     [[255, 255, 255],
#      [255, 255, 255], 
#      [255, 255, 255]],
#     [[255, 255, 255],
#      [255, 255, 255], 
#      [255, 255, 255]],
#     [[255, 255, 255],
#      [255, 255, 255],
#      [255, 255, 255]]]
#    )

#a_x = a[:, :, 0]
#a_y = a[:, :, 1]
#a_z = a[:, :, 2]

#b = a.reshape(5 * 3, 3)
#print(a)
#list_a = b.tolist()
#print(list_a)

#a_x = a_x.reshape(5 * 3, 1)
#print(a_x)

#list_x = a_x.tolist()
#list_y = a_y.tolist()
#list_z = a_z.tolist()

#print(a_x)
#print(a_y)
#print(a_z)

#print(list_x)
#print(list_y)
#print(list_z)

#cut_a = a[:, :, 1]
#cut_a = cut_a.astype(np.uint8)
#print(cut_a)

#threeD = np.load("threeD_array_after_axes_transfer.npy")
#threeD = np.load("threeD.npy")
# 三张图片降噪之后的结果
#threeD = np.load("threeD_array_result.npy")
# 5 x 5降噪之后的结果
threeD = np.load("threeD_after_block_analysis.npy")
#print(threeD)

threeD = threeD.astype(np.int16)

cut_threeD = threeD[:, :, :]
#cut_threeD = threeD[0 : 600 : 5, 0 : 800 : 5, :]

cut_threeD_rgb = cut_threeD.copy()

cut_threeD_display = cut_threeD[:, :, 2]
print(cut_threeD_display)

cut_threeD_display = cut_threeD_display.astype(np.uint8)
cv2.namedWindow("gray", 0)
cv2.imshow("gray", cut_threeD_display)

cut_threeD_rgb = cut_threeD_rgb.astype(np.uint8)
cv2.namedWindow("rgb", 0)
cv2.imshow("rgb", cut_threeD_rgb)

#b = b.astype(np.uint8)

#c = a.astype(np.uint8)

#def groundAnalysis(threeD, ground):


#cv2.imshow("random", a)
#cv2.imshow("random", c)
#cv2.imshow("rgb", cut_a)
cv2.waitKey(0)