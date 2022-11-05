import numpy as np

# dot乘积
print("\n---------二维矩阵的dot乘积---------")
matrix1 = np.arange(12).reshape(2,6)    # 2×6的矩阵
print("前矩阵：")
print(matrix1)

matrix2 = np.arange(12).reshape(6,2)    # 6×2的矩阵
print("后矩阵：")
print(matrix2)

a = np.dot(matrix1,matrix2)     # 当两个二维数组相乘，使用dot实现矩阵的乘积
print("矩阵乘积结果：")
print(a)

print("\n---------一维矩阵的dot乘积---------")
A = np.array([1, 2, 3])
print("前一维矩阵：")
print(A)

B = np.array([3, 2, 1])
print("后一维矩阵：")
print(B)

print("一维矩阵的内积结果:")
print(np.dot(A,B))

print("\n---------inner乘积---------")
# inner乘积:数组a和b最后一维的长度必须相同
matrix1 = np.arange(12).reshape(2,6)    # 2×6的矩阵
b = np.inner(matrix1,matrix1)
print(b)


print("\n---------outer乘积---------")
# outer乘积:两个一维数组相乘
matrix3 = np.array([1,2,3])
matrix4 = np.array([4,5,6])
c = np.outer(matrix3,matrix4)
print(c)
"""
此时matrix3和matrix4是一维数组
如果matrix3和matrix4定义为二维数组或多维数组，outer会将额日伪数组展平再相乘
"""
matrix3 = np.arange(12).reshape(2,6)
matrix4 = np.arange(12).reshape(3,4)
d = np.outer(matrix3,matrix4)   # 展平后即为12×12的列向量和行向量相乘，得到12×12的二维数组
print(d)
