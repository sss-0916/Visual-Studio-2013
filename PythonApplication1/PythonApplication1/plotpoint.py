# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:37:21 2015

@author: Eddy_zheng
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#data = np.random.randint(0, 255, size=[40, 40, 40])

data = np.load("cut_threeD.npy")

#data = np.load("threeD.npy")

x = data[:, :, 0]
y = data[:, :, 1]
z = data[:, :, 2]

#x = np.load("x.npy")
#y = np.load("y.npy")
#z = np.load("z.npy")


#x, y, z = data[0], data[1], data[2]
ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
#ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
#ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
#ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
ax.scatter(x, y, z, c='r')

ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
ax.set_zlim(0, 6000)
ax.set_xlim(-4000, 2000)
ax.set_ylim(-4000, 2000)

plt.show()