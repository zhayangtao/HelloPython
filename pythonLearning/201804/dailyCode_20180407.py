
"""
装饰器嵌套
"""


def F1(F):
    return lambda: 'X' + F()


def F2(F):
    return lambda: 'Y' + F()


def F3(F):
    return lambda: 'Z' + F()


@F1
@F2
@F3
def func():
    return 'spam'


print(func())


"""
装饰器参数：在装饰发生之前解析
"""


# 跟踪调用
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a + b + c)


print(spam(1, 2, 3))


"""
状态信息保持选项
"""


# 类实例属性
class tracer1:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer1
def spam1(a, b, c):
    print(a + b + c)


@tracer1
def eggs(x, y):
    print(x ** y)


print('_' * 20)
spam1(1, 2, 3)
spam1(a=4, b=5, c=6)

eggs(2, 16)
eggs(4, y=4)


"""
封闭作用域和全局作用域
"""


def testC():
    calls = 1
    print(calls)


calls = 0
print('testC()=', testC())


def tracer2(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper


@tracer2
def spam1(a, b, c):
    print(a + b + c)


@tracer2
def eggs(x, y):
    print(x ** y)


print('_' * 20)
spam1(1, 2, 3)
spam1(a=4, b=5, c=6)


"""
封闭作用域和 nonlocal 作用域
"""


def tracer3(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper


@tracer3
def spam(a, b, c):
    print(a + b + c)


@tracer3
def eggs(x, y):
    print(x ** y)


print('_' * 20)
spam(1, 2, 3)
spam(a=4, b=5, c=6)

