# 导入numpy模块
import numpy as np

# 使用array函数创建一维数组
b = np.array([1, 2, 3, 4, 5, 6])
print(b)
print('b 数组的维度：', b.shape)

a = np.array([1, 2, 3, 4])
print(a)
print(type(a))

# 使用array函数创建二维数组
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print('b 数组的维度：', b.shape)

# 使用array函数创建三维数组
c = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(c)
print('c数字的维度', c.shape)

# array函数中dtype的使用
d = np.array([1, 2, 3, 4, 5, 6], dtype=float)
print(d)
print(type(d))

# array函数中dtype的使用
d = np.array([1, 2, 3, 4, 5, 6], dtype=complex)
print(d)
print(type(d))

# array函数中ndmin的使用
e=np.array([1,2,3,4,5,6],ndmin=3)
print(e)

f = np.array([5, 6, 7], dtype=float, ndmin=3)
print(f)