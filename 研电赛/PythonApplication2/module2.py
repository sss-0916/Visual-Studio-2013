import numpy as np

a = np.array(
    [[[1, 2, 3], [2, 1, 3], [3, 1, 2]], 
     [[5, 6, 8], [7, 3, 5], [8, 3, 4]], 
     [[5, 6, 8], [7, 3, 5], [8, 3, 4]], 
     [[3, 1, 1], [5, 1, 3], [4, 2, 1]]]
    )

print(a)

cut_a = a[:, :, 2]
print(cut_a)

for i in range(4):
    temp = cut_a[i, :]
    temp[temp < 8] = 0

print(cut_a)