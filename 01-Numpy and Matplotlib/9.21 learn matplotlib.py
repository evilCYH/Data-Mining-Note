import numpy as np
import matplotlib.pyplot as plt

"""
np.linspace(0,10,10)涉及到x轴的刻度问题
np.linspace与np.arange类似，生成的是等差数列
linspace常用的三个参数是start、stop和num
num是数组中元素的个数
比如np.linspace(0,10,10)的结果是
array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])
如果只画这十个点对应的函数值，可以看到很不准确，甚至num=100也不准确
np.linspace(0,10,1000)才有点准确

"""
x = np.linspace(0, 10, 10)
y = np.sin(x)
z = np.cos(x ** 2)

plt.figure(figsize=(8, 4))

plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2, 1.2)
plt.legend()

plt.show()

# plt.figure(1)
# plt.figure(2)
# """
# subplot()方法包含三个参数
# 第三个参数代表选择第几个子图(figure)
# 前两个参数代表生成几行几列的子图矩阵，比如21就代表生成2行一列的子图
# """
# ax1 = plt.subplot(211)
# ax2 = plt.subplot(212)
#
# x = np.linspace(0,3,100)
# for i in range(5):
#     plt.figure(1)
#     plt.plot(x, np.exp(i*x/3))
#     """
#     使用plt.sca()指定绘图区域
#     """
#     plt.sca(ax1)
#     plt.plot(x, np.sin(i*x))
#     plt.sca(ax2)
#     plt.plot(x, np.cos(i*x))
#
#
# plt.show()

# print(np.linspace(1,50,50))
