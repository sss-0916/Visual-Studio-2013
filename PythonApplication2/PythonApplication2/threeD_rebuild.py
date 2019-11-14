import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter 

# author = "白静静"
# date = "2019/04/15"

fig = plt.figure(figsize=(16,12))
ax = fig.gca(projection="3d")

threeD = np.load("threeD.npy")
#print(threeD)

threeD = threeD.astype(np.int16)

#cut_threeD = threeD[:, :, :]
cut_threeD = threeD[0 : 600 : 5, 0 : 800 : 5, :]
cut_threeD_rgb = cut_threeD.copy()

cut_threeD_display = cut_threeD[:, :, 1]  #第二个通道绿色
#print(cut_threeD_display)

cut_threeD_display = cut_threeD_display.astype(np.uint8)
cv2.namedWindow("gray", 0)
cv2.imshow("gray", cut_threeD_display)

#cut_threeD_rgb = cut_threeD_rgb.astype(np.uint8)
#cv2.namedWindow("rgb", 0)
#cv2.imshow("rgb", cut_threeD_rgb)

imgd = np.array(cut_threeD_display) 

# 准备数据
sp = cut_threeD_display.shape
h = int(sp[0])#height(rows) of image
w = int(sp[1])#width(colums) of image

x = np.arange(0,w,1)
y = np.arange(0,h,1)
x,y = np.meshgrid(x,y)
z = imgd
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)  # cmap指color map

# 自定义z轴
ax.set_zlim(-10, 255)
ax.zaxis.set_major_locator(LinearLocator(10))  # z轴网格线的疏密，刻度的疏密，20表示刻度的个数
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # 将z的value字符串转为float，保留2位小数

# 设置坐标轴的label和标题
ax.set_xlabel('x', size=15)
ax.set_ylabel('y', size=15)
ax.set_zlabel('z', size=15)
ax.set_title("Surface plot", weight='bold', size=20)

# 添加右侧的色卡条
fig.colorbar(surf, shrink=0.6, aspect=8)  # shrink表示整体收缩比例，aspect仅对bar的宽度有影响，aspect值越大，bar越窄
plt.show()

cv2.waitKey(0)
