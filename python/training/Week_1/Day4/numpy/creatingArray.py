import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# print(np.zeros((2,3)))
# print(np.ones((3,2)))
# print(np.arange(0, 10, 2))
# print(np.linspace(2,3))
# print(np.random.rand(2,2))

A = np.array([[1,2], [3,4]])
B = np.array([[2, 0], [1, 3]])

print("Matrix Multiplication:", np.dot(A,B))
print("Transpose of A:",np.transpose(A))
print(np.linalg.inv(A))

arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr[0, 1])
print(arr[:, 1])
print(arr[1])

print(arr.mean())
print(arr.sum())
print(arr.std())
print(arr.max())
print(arr.min())


