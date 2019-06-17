import numpy as np
import matplotlib.pylab as plt


# 感知机的实现
# 与门
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    return 1


# 测试 AND
print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

# 导入权重和偏置
import numpy as np

x = np.array([0, 1])  # 输入
w = np.array([0.5, 0.5])  # 权重
b = -.7  # 偏置
print(w * x)
print(np.sum(w * x))
print(np.sum(w * x) + b)


#  使用权重和偏置的实现
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, .5])
    b = -.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    return 1


# 与非门：仅当 x1 和 x2 同时为 1 时输出0，其他时候输出 1
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-.5, -.5])  # 仅权重和偏置与 AND 不同
    b = .7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    return 1


# 或门：当 x1 或 x2 中任意一方为1，输出1
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    return 1


# 异或门：仅当 x1 或 x2 中一方为1,不同时为1时，才会输出1，
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))


# 激活函数
# 阶跃函数的实现
def step_function(x):
    y = x > 0
    return y.astype(np.int)


x = np.array([-1.0, 1.0, 2.0])
y = x > 0
print(y)
y = y.astype(np.int)
print(y)


# 阶跃函数的图形
def step_function(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()


# sigmoid 函数的实现
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # 指定 y 轴的范围
plt.show()


# ReLU 函数
def relu(x):
    return np.maximum(0, x)


X = np.array([1,2])
print(X.shape)
W = np.array([[1,3,5],[2,4,6]])
Y = np.dot(X, W)
print(Y)


X = np.array([1.0, .5])
W1 = np.array([[.1, .3, .5], [.2, .4, .6]])
B1 = np.array([.1, .2, .3])

A1 = np.dot(X, W1) + B1
print(A1)