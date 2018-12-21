import numpy as np

# 生成 numpy 数组
x = np.array([1.0, 2.0, 3.0])
print(x)
# 算数运算
y = np.array([2.0, 4.0, 6.0])
print(x + y)
# n 维数组
A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

# matplotlib
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0, 6, 0.1)  # 以 0.1 为单位，生成0-6的数据
y = np.sin(x)
# 绘制图像
plt.plot(x, y)
plt.show()

y2 = np.cos(x)
# 绘制图形
plt.plot(x, y, label='sin')
plt.plot(x, y2, linestyle='--', label='cos')  # 用虚线绘制
plt.xlabel('x')  # x轴标签
plt.ylabel('y')
plt.title('sin $ cos')  # 标题
plt.legend()
plt.show()
