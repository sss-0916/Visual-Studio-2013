#coding=gbk

import numpy as np

# author = "������"
# date = "2019/04/18"

# ������� 12 * 16�Ķ�ά����
a = np.random.randint(-50, 50, size = (12, 16))
print(a)

# ѡȡ��һ��
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

# ��ÿһ�н����ж�, ���ڵ������Ϣ��Ϊ��Ч
for i in range(12):
    b = a[i, :]
    b[b < 0] = 100

print(a)