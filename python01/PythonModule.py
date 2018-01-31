'a test module'
__author__ = 'zhayangtao'
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print(f'Hello, $s!')
    else:
        print('Too many arguments')


if __name__ == '__main__':
    test()

"""
Module documentation
Words Go Here
"""
spam = 40


def square(x):
    """
    function documentation
    can we have your liver then?
    """
    return x ** 2


class Employee:
    "class documentation"
    pass


print(square(4))
print(square.__doc__)


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts


def makeActions2():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested


# 递归
def mysum(L):
    if not L:
        return 0
    return nonempty(L)


def nonempty(L):
    return L[0] + mysum(L[1:])


def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c


seplen = 60
sepchr = '_'
def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file)
        print(sepline)
    count = 0
    for attr in module.__dict__:
        print('%02d) %s' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<bulit-in name')
        else:
            print(getattr(module, attr))
        count += 1


# 比较浮点数
def equal_float(a, b):
    return abs(a - b) <= sys.float_info.epsilon


text = """abc \
    absf
"""
print(text)

s = ('1bv', '222')
s = ("bbb"
     "ssss")
print(type(s))

s = """sss \
\sss
"""
print(s)