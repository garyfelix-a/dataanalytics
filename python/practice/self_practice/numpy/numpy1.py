import numpy as np

# 0d array
arr2 = np.array(43)
print(arr2)

# 1d array
arr3 = np.array([1, 2, 3, 4, 5])
print(arr3)

# 2d array
arr4 = np.array([[1, 2], [2, 3]])
print(arr4)

# 3d array
arr5 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n",arr5)

print(arr5.ndim)

# slicing
arr_sli = np.array([1, 2, 3, 4, 5])
print(arr_sli[1:4])

# broadcasting
a = np.array([[1, 2], [2, 3]])
b = np.array([10, 20])
c = a + b
print("Broadcasting", c)