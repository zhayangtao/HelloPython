"""
装饰器参数
"""


def decorator(A, B):
    # save or use function F
    def actualDecorator(F):
        return F
    return actualDecorator


"""
类错误之一：装饰类方法
"""


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


spam(1, 2, 3)
spam(a=4, b=5, c=6)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


bob = Person('bob smith', 500000)
# bob.giveRaise(.25)
# print(bob.lastName())


"""
使用嵌套函数来装饰方法
"""


def tracer(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall


@tracer
def spam(a, b, c):
    print(a + b + c)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


"""
计时调用
"""


import time


class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@timer
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer
def mapcall(N):
    return map((lambda x: x * 2), range(N))


result = listcomp(5)
listcomp(500000)
listcomp(5000000)
print(result)
print('alltime = %s' % listcomp.alltime)


"""
添加装饰器参数
"""


def timer(label=''):
    def decorator(func):
        def onCall(*args):
            ...
            print(label, ...)
        return onCall
    return decorator


@timer('==>')
def listcomp(N):
    ...
