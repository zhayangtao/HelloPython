# 阶跃函数的图形
import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # 指定 y 轴 范围
plt.show()


# sigmoid 函数的实现
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))
