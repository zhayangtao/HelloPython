'''
参数
'''


def f(a):
    a = 99


def changer(a, b):
    a = 2
    b[0] = 'spam'


L = [1, 2]
changer(1, L[:])


def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y


X = 1
x, L = multiple(X, L)
