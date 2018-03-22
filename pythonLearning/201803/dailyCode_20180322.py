"""
装饰器和元类
"""


class Super:
    def __init__(self, *args):
        print('super')


class Sub(Super):
    # ...
    # def __init__(self):
    #     print('sub')

    def __call__(self, *args):
        print('sub call')


s = Sub()
s(1)


class C:
    @staticmethod
    def meth():
        ...


class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    @staticmethod
    def printNumInstances():
        print('Number of instances created: ', Spam.numInstances)


print()
print('*' * 10)
# 函数装饰器例子


class Tracer:
    def __init__(self, func):
        print('init')
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)


@Tracer
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
spam('a', 'b', 'c')
spam(4, 5, 6)


# 类装饰器和元类
def count(aClass):
    aClass.numInstances = 0
    return aClass


@count
class Spam1:
    ...


# 修改可变的类属性可能产生副作用
class C1:
    shared = []

    def __init__(self):
        self.perobj = []


print()
print('*' * 10)
x = C1()
y = C1()
x.shared.append('spam')
x.perobj.append('spam')
print(x.shared, x.perobj)
print(y.shared, y.perobj)


"""
异常
"""


def fetcher(obj, index):
    return obj[index]


x = 'spam'


def catcher():
    try:
        fetcher(x, 4)
    except IndexError as identifier:
        print('got exception')
    else:
        print('continuing')


catcher()
