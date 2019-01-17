# 实现 softmax 函数
import numpy as np
import matplotlib.pylab as plt


# 定义 softmax 函数
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


# sigmoid 函数的实现
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 交叉熵误差
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

e = cross_entropy_error(np.array(y), np.array(t))
print(e)


# mini-batch 版交叉熵误差的实现
def cross_entropy_error_mini_batch(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size


# 当监督数据是标签形式（非one-hot表示，而是像“2”“7”这样的
# 标签）时，交叉熵误差可通过如下代码实现。
def cross_entropy_error(y: np.array, t: np.array):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


# 计算导数
def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


# 数值微分的例子
def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x


# 绘制 function_1 的图像
x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel('x')
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))


# 偏导数
def function_2(x):
    return x[0] ** 2 + x[1] ** 2


def function_tmp1(x0):
    return x0 * x0 + 4.0 ** 2


print(numerical_diff(function_tmp1, 3))


# 梯度
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)  # 生成和 x 形状相同的数组

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x + h) 的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x - h) 的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 还原值
    return grad


# 梯度下降算法
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x


def function_3(x):
    return x[0] ** 2 + x[1] ** 2


init_x = np.array([-3.0, 4.0])
gradient_descent(function_3, init_x=init_x, lr=0.1, step_num=100)


# 以一个简单神经网络为例，实现求梯度的代码
class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)  # 用高斯分布进行初始化

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss


net = SimpleNet()
print(net.W)
x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)
print(np.argmax(p))  # 最大值的索引
t = np.array([0, 0, 1])
print(net.loss(x, t))


def f(W):
    return net.loss(x, t)


# dW = numerical_gradient(f, net.W)
# print(dW)

f = lambda w: net.loss(x, t)
# dw = numerical_gradient(f, net.W)


# 两层神经网络的类
class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重
        self.params = {}
        self.params['W1'] = weight_init_std * \
                            np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * \
                            np.random.randn(hidden_size, output_size)

        self.params['b2'] = np.zeros(output_size)

    def predict(self, x):
        W1, W2 = self.params["W1"], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)
        return y

    # x：输入数据，t：监督数据
    def loss(self, x, t):
        y = self.predict(x)
        return cross_entropy_error(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_w = lambda W: self.loss(x, t)
        grads = {}
        grads['W1'] = numerical_gradient(loss_w, self.params['W1'])
        grads['W2'] = numerical_gradient(loss_w, self.params['W2'])
        grads['b1'] = numerical_gradient(loss_w, self.params['b1'])
        grads['b2'] = numerical_gradient(loss_w, self.params['b2'])
        return grads


net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
print(net.params['W1'].shape)