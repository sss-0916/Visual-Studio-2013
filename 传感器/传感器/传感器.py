#coding=gbk

import numpy as np
import matplotlib.pyplot as plt

N = 20 # 每一个类别的生成的点的数量
D = 2 # 每个点的维度，这里使用平面，所以是2维数据
K = 5 # 类别数量，我们一共生成5个类别的点

# 所有的样本数据，一共100个点，每个点用2个维度表示
# 所有训练数据就是一个20*5的二维矩阵
X = np.zeros((N * K, D))

# 标签数据，一共是100个点，每个点对应一个类别，
# 所以标签是一个100*1的矩阵
y = np.zeros(N * K, dtype='uint8')

# 生成训练数据
for j in range(K):
    ix = range(N * j, N * (j + 1))
    r = np.linspace(0.0, 1, N)
    t = np.linspace(j * 4, (j + 1) * 4, N) + np.random.randn(N) * 0.2
    X[ix] = np.c_[r * np.sin(t), r * np.cos(t)]
    y[ix] = j

plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
plt.show()