#coding=gbk

import numpy as np

# author = "张蒙蒙" 
# date = "2019/04/08"

# 三张图
global_threeD_list = [[0, 0, 0]] * 3 * 2 * 3

#print(global_threeD_list)

#随机生成一个5*3*3的矩阵
a = np.random.randint(-50, 50, size = (3, 2, 3))
b = np.random.randint(-50, 50, size = (3, 2, 3))
c = np.random.randint(-50, 50, size = (3, 2, 3))
d = np.random.randint(-50, 50, size = (3, 2, 3))

#print(a)
#print(b)
#print(c)
#print(d)

a = a.reshape(6, 3)
list_a = a.tolist()
#print(list_a)

#b = b.reshape(6, 3)
#list_b = b.tolist()
#print(list_b)

#c = c.reshape(6, 3)
#list_c = c.tolist()
#print(list_c)

#d = d.reshape(6, 3)
#list_d = d.tolist()
#print(list_d)

#threeD_list = []

#threeD_list = threeD_list + list_a
#threeD_list = threeD_list + list_b
#threeD_list = threeD_list + list_c
#threeD_list = threeD_list + list_d
#print(threeD_list)

#threeD_list = threeD_list[3 : 12]
#print(threeD_list)

#threeD_array = np.array(threeD_list).reshape(6, 3, 3)
#print(threeD_array)

#print(global_threeD_list)

while True:
    global_threeD_list = global_threeD_list + list_a
    global_threeD_list = global_threeD_list[6 : 24]
    #print(global_threeD_list)
    print(len(global_threeD_list))