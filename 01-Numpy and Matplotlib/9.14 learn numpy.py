import numpy as np

# print("\n---------数组的创建---------")
# # 通过array创建
# print("array创建：")
# a = np.array([[1, 3, 5, 7], [2, 4, 6, 8], [9, 9, 9, 9]])
# print(a)
# # 通过arange创建
# print("arange创建：")
# c1 = np.arange(0,10,2)      # 给定三个参数，则分别为开始值、终值和步长
# print(c1)
# c2 = np.arange(5,10)      # 给定两个个参数，则分别为开始值、终值，步长默认为1
# print(c2)
# c3 = np.arange(10)      # 给定一个参数，则为终值，开始值和步长默认为0和1
# print(c3)
#
# print("\n---------shape与reshape方法的应用---------")
# # shape方法的应用
# a
# print("矩阵的大小为：" + str(a.shape))
#
# # reshape方法的应用
# b = a.reshape(2, 6)
# print(a)  # 原数组形状不变
# print(b)
# print("新矩阵b的大小为：" + str(b.shape))
#
# print("\n---------对a,b其中一个重新赋值，两个都会收到影响---------")
#
# # 对a,b其中一个重新赋值，两个都会收到影响
# a[0][0] = 100
#
# print(a)
# print(b)        # 可以发现b矩阵的值也改变了
#
# print("\n---------最值、和、平均值、方差、标准差---------")
# # 求矩阵所有元素的最大值、最小值
# print(np.max(a))
# print(np.min(a))
#
# # 求矩阵所有元素的和
# print(np.sum(a))
#
# # 还可以在指定axis轴参数的条件下求和
# # axis的值只有0,1。即只有第0轴和第1轴。第0轴为竖向，第1轴为横向
# print(np.sum(a, axis=0))
# print(np.sum(b, axis=1))
#
# # 平均值(整数数组的结果为双精度浮点数)
# print(np.mean(a, axis=1))
# print(np.average(a))
#
# # 方差
# print(np.var(a))
#
# # 标准差
# print(np.std(a))

print("\n---------线性代数~矩阵计算---------")
# 矩阵乘积(首先使用reshape((-1,1))实现转置/转化为列向量)
C = np.array([1, 2, 3])
D = np.array([3, 2, 1])
print(C.reshape(-1,1))
print(D.reshape(-1,1))
print(np.dot(C,D.reshape(-1,1)))    # 没有出现报错
# print(np.dot(D.reshape(-1, 1), C))       # 出现报错
print(np.dot(D.reshape(-1, 1), C.reshape(1,-1)))       # 正确写法

print("\n---------报错探索---------")
x = np.array([1, 2, 3])
print(x)
x = x.reshape(1,-1)
print(x)

matrix1 = np.arange(12).reshape(2,3,2)
print("\n"+str(matrix1))
matrix2 = np.arange(12).reshape(2,2,3)
print("\n"+str(matrix2))