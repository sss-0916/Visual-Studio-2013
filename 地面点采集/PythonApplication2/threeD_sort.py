#coding=gbk

import numpy as np

# author = "张蒙蒙"
# date = "2019/04/06"

#随机生成一个6*9*3的矩阵
a = np.random.randint(-50, 50, size = (6, 9, 3))

# 获取列表的第三个元素
def takeThird(ele):
    return ele[2]

# 块分析
def blockAnalysis(block, threeD_list):
    print(block)
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
    x = 0
    y = 0
    # 降噪后
    threeD_list = []
    while y >= 0 and y < 6:
        while x >= 0 and x < 9:
            cut_threeD = threeD[y : y + 3, x : x + 3]
            #print(cut_threeD)
            blockAnalysis(cut_threeD, threeD_list)
            x = x + 3
        y = y + 3
        x = 0
    #while y >= 0 and y < 360:
    #    while x >= 0 and x < 640:
    #        cut_threeD = threeD[y : y + 5, x : x + 5]
    #        blockAnalysis(cut_threeD, threeD_list)
    #        x = x + 5
    #    y = y + 5
    #    x = 0
    return threeD_list

print(a)

b = cutBlockAnalysis(a)
print(b)