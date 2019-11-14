from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')  #1行一列第一个

#data = np.load("cut_threeD.npy")    #读取npy数据
#x=data[:, :, 0]
#y=data[:, :, 1]
#z=data[:, :, 2]

#data = np.load("threeD.npy")    #读取npy数据
#x=data[:, :, 0]
#y=data[:, :, 1]
#z=data[:, :, 2]

#x = np.load("x.npy")
#y = np.load("y.npy")
#z = np.load("z.npy")
#print(x)
#print(y)
#print(z)


#x, y, z = axes3d.get_test_data()

print(axes3d.__file__)
ax1.plot_wireframe(x,y,z, rstride = 3, cstride = 3)   #列数上限，行数上限

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()