# 导入模块
import numpy as np


def randomTest():
  # 使用random创建一维数组 [0.0,1.0)
  a = np.random.random(size=4)
  print("一维数组")
  print(a)
  print(type(a))

  # 创建二维数组
  b = np.random.random(size=(3, 4))
  print("二维数组")
  print(b)

  # 创建三维数组
  c = np.random.random(size=(2, 3, 4))
  print("三维数组")
  print(c)


# 随机整数
def randomintTest():
  # 生成[0,low)范围的随机整数
  a = np.random.randint(5, size=10)
  print(a)
  print(type(a))

  # 生成[low,high)范围的随机整数
  b = np.random.randint(5, 10, size=10)
  print(b)

  # 生成[low,high)范围的2*4 的随机整数
  c = np.random.randint(5, 10, size=(2, 4))
  print(c)

  # dtype的使用
  d = np.random.randint(10, size=5, dtype=np.int64)
  print('默认的dtype', d.dtype)


# 创建标准的正太分布  期望为0  方差为1
def randnTest():
  a = np.random.randn(4)
  print(a)

  # 创建二维的
  b = np.random.randn(2, 3)
  print(b)

  # 创建三维的数组
  c = np.random.randn(2, 3, 4)
  print(c)


# 创建指定期望和方差的正太分布
def normalTest():
  # 默认的期望是loc=0.0  方差scale=1.0
  a = np.random.normal(size=5)
  print(a)

  # 指定期望和方差
  b = np.random.normal(loc=2, scale=3, size=(3, 4))
  print(b)

  # 正太分布（高斯分布）loc：期望scale：方差size 形状
  print(np.random.normal(loc=3, scale=4, size=(2, 2, 3)))


# 调用
# randomTest()
# randomintTest()
# randnTest()
normalTest()
