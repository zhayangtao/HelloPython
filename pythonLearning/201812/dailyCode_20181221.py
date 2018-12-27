# 实现 softmax 函数
import numpy as np

a = np.array([1010, 1000, 990])
# np.exp(a) / np.sum(np.exp(a))
c = np.max(a)
print(a - c)
np.exp(a - c) / np.sum(np.exp(a - c))


# 定义 softmax 函数
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


# 使用 softmax 函数
a = np.array([.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))

# 导入 mnist
import sys, os
import pickle

sys.path.append(os.pardir)  # 导入父目录的文件


def init_network():
    with open('sample_weight.pkl', 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np


x = np.array([[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.2, 0.5, 0.3], [0.8, 0.1, 0.1]])
y = np.argmax(x, axis=1)
print(y)


#  神经网络的学习
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)

# 交叉熵误差
