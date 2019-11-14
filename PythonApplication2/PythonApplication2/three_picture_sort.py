import numpy as np
import operator
from numpy import random

# author = "白静静" 
# date = "2019/03/27"

# 获取列表的第三个元素
#def takeThird(ele):
#    return ele[2]

#随机生成一个5*3*3的矩阵
a=random.randint(-50,50,size=(5,3,3))
print(a)
list1 = []
for i in range(len(a)):
    idex=np.lexsort([a[i][:,2]])
    sorted_a= a[i][idex, :]
    list1.append(sorted_a[1].tolist())
    #sorted_a = sorted_a.reshape(5, 3, 3)
    #print(a)
    print(sorted_a)
    #list1 = []
    #for j in range(3):
    #    list1.append(sorted_a[j])
    #print(list1)
#print(sorted_a)
print(list1)
arr2 = np.array(list1).reshape(5, 1, 3)
print(arr2)


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