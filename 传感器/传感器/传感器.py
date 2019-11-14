#coding=gbk

import numpy as np
import matplotlib.pyplot as plt

N = 20 # ÿһ���������ɵĵ������
D = 2 # ÿ�����ά�ȣ�����ʹ��ƽ�棬������2ά����
K = 5 # �������������һ������5�����ĵ�

# ���е��������ݣ�һ��100���㣬ÿ������2��ά�ȱ�ʾ
# ����ѵ�����ݾ���һ��20*5�Ķ�ά����
X = np.zeros((N * K, D))

# ��ǩ���ݣ�һ����100���㣬ÿ�����Ӧһ�����
# ���Ա�ǩ��һ��100*1�ľ���
y = np.zeros(N * K, dtype='uint8')

# ����ѵ������
for j in range(K):
    ix = range(N * j, N * (j + 1))
    r = np.linspace(0.0, 1, N)
    t = np.linspace(j * 4, (j + 1) * 4, N) + np.random.randn(N) * 0.2
    X[ix] = np.c_[r * np.sin(t), r * np.cos(t)]
    y[ix] = j

plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
plt.show()