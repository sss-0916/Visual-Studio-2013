#coding=gbk

import numpy as np
import operator
from numpy import random
import math

# author = "张蒙蒙"
# date = "2019/04/01"

#随机生成一个5*4*3的矩阵
a=random.randint(-50,50,size=(10,10,3))
print(a)

#a = np.array([1, 1, 1])

b = np.array(
    [1,
     1,
     1]
    )

#sum = a + b
#print(sum)

#b = a.reshape(20, 3)
#print(b)

#list_a = b.tolist()
#print(list_a)

#cos_a = math.cos(60 * math.pi / 180)
#print(cos_a)

#spin_matrix = np.array(
#    [[1, 0, 0],
#     [0, 1, 4]]
#    )
#print(spin_matrix)

# 矩阵相乘
def matrixMul(ele_list, spin_matrix, translation_matrix):
    temp_array = np.array(ele_list)
    #print(temp_array)
    ele_array = temp_array.reshape(3, 1)
    #print(ele_array)
    #ele_result = spin_matrix * ele_array
    ele_result = np.matmul(spin_matrix, ele_array)
    #print(ele_result)
    ele_result = ele_result + translation_matrix
    ele_result_list = ele_result.tolist()
    #print(ele_result_list)
    return ele_result_list

# 坐标系转换
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

    #print(spin_matrix)

    # 平移矩阵
    translation_matrix = np.array(
        [1, 
         1, 
         1]
        )

    array_after_axes_transfer = np.matmul(threeD_array, spin_matrix)
    #print(array_after_axes_transfer)
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
    #print(array_after_axes_transfer.astype(np.int16))

    #array_after_axes_transfer = array_after_axes_transfer + translation_matrix
    return array_after_axes_transfer

after_axes_transfer = axesTransfer(a, 30, 0)
#print(after_axes_transfer.astype(np.int16))
print(after_axes_transfer)