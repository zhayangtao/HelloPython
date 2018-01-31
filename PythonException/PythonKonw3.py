def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            print('before de init')
            self.wrapped = cls(*args)
            print('after de init')

        def __getattr__(self, item):
            print('getattr')
            return getattr(self.wrapped, item)

    return Wrapper


@decorator
class C:
    def __init__(self, x, y):
        print('c init')
        self.attr = 'spam'


# x = C(6, 7)
# print(x.attr)


# 装饰器嵌套
def decorator1(cls): ...


def decorator2(cls): ...


@decorator
@decorator1
@decorator2
class C1:
    ...


# 装饰器参数：在装饰之前解析
def decorator3(A, B):
    def actualDescrator(F):
        return callable

    return actualDescrator


# 使用类实例属性
class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@Tracer
def spam(a, b, c):
    print(a + b + c)


@Tracer
def eggs(x, y):
    print(x ** y)


spam(1, 2, 3)
spam(4, 5, 6)

eggs(2, 16)
eggs(4, y=4)
print('****************************')


# 使用nonlocal属性
def Tracer1(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper


@Tracer1
def spam(a, b, c):
    print(a + b + c)


@Tracer1
def eggs(x, y):
    print(x ** y)


spam(1, 2, 3)
spam(4, 5, 6)

eggs(2, 16)
eggs(4, y=4)
print('****************************')


#错误验证：基于类的装饰器
class Tracer4:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @Tracer4
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @Tracer4
    def lastName(self):
        return self.name.split()[-1]

bob = Person('bob smith', 5000)
bob.giveRaise(.25)
# print(bob.lastName())



