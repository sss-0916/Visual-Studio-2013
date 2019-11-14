import numpy as np
from numpy import random

# author = "张蒙蒙"
# date = "2019/03/21"

# 获取列表的第三个元素
def takeThird(ele):
    return ele[2]

def blockAnalysis(block, threeD_list):
    #print(block)
    #block.astype(np.uint8)
    #cv2.namedWindow("block", 0)
    #cv2.resizeWindow("block", 5, 5)
    #cv2.imshow("block", block)
    #print(block)
    #print(block)
    temp = np.reshape(block, (-1, 3))
    #print(temp)
    block_list = temp.tolist()
    #print(block_list)
    block_list.sort(key = takeThird)
    print(block_list)
    threeD_list.append(block_list[1])

# 切块
def cutBlockAnalysis(threeD):
    x = 0
    y = 0
    # 降噪后
    threeD_list = []
    while y >= 0 and y < 8:
        while x >= 0 and x < 6:
            cut_threeD = threeD[y : y + 2, x : x + 2]
            #print(cut_threeD)
            blockAnalysis(cut_threeD, threeD_list)
            x = x + 2
        y = y + 2
        x = 0
    #while y >= 0 and y < 360:
    #    while x >= 0 and x < 640:
    #        cut_threeD = threeD[y : y + 5, x : x + 5]
    #        blockAnalysis(cut_threeD, threeD_list)
    #        x = x + 5
    #    y = y + 5
    #    x = 0
    return threeD_list

def rowAnalysis(temp):
    threeD_list = []
    temp1 = numpy.reshape(temp, (-1, 3))
    temp_list = temp1.tolist()
    temp_list.sort(key = takeThird)
    threeD_list.append(temp_list[1])
    return threeD_list

#def threePictureAnalysis(threeD_array):
#    three_picture_list = []
#    i = 0
#    while i >= 0 and i < 5:
#        temp = threeD_array[i, :, :]
#        rowAnalysis(temp, three_picture_list)
#        ++i
#    return three_picture_list

#随机生成一个5*3*3的矩阵
a = random.randint(-50,50,size=(8,6,3))
print(a)

b = cutBlockAnalysis(a)
print(b)

#hehe = threePictureAnalysis(a)
#print(hehe)
#temp = a[0, :, :]
#print(temp)
#temp_list = temp.tolist()
#print(temp_list)

#a.sort(axis = 1, order = a[:, :, 2])
#print(a)

#a.sort(axis = 1)
#print(a)

# 转为二维矩阵
#b = numpy.reshape(a, (-1, 3))
#print(b)
#将矩阵转化为列表
#list_1=b.tolist()   

#list_1.sort(key = takeThird)

#print(list_1)

#print(list_1[13])

#print(list_1)

#print(list_1.sort(key = takeThird))
#list_2=[]

#for i in range(len(list_1)):
#    for j in range(len(list_1[0])):
#         list_2.append(list_1[i][j][2])

#去掉<0的数      
#newnums=[k for k in list_2 if k>0]      
#从小到大排序
#newnums.sort() 
#print(newnums)
#print(newnums[int((len(newnums)-1))//2])