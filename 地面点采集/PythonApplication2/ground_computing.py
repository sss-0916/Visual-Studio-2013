#coding=gbk

import numpy as np

# author = "张蒙蒙"
# date = "2019/04/18"

# 随机生成 12 * 16的二维矩阵
a = np.random.randint(-50, 50, size = (12, 16))
print(a)

# 选取第一行
#a_0 = a[0, :]
#a_1 = a[1, :]
#a_2 = a[2, :]

#a_0[a_0 < 0] = 0
#a_1[a_1 < 0] = 0
#a_2[a_2 < 0] = 0

#print(a_0)
#print(a_1)
#print(a_2)

#print(a)

# 对每一行进行判断, 低于地面的信息设为无效
for i in range(12):
    b = a[i, :]
    b[b < 0] = 100

print(a)