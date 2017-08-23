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


#装饰器例子
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a, b, c)


def decorator(aClass): ...

@decorator
class C: ...


def count(aclass):
    aclass.numInstances = 0
    return aclass

@count
class Spam: ...

@count
class Sub(Spam): ...

@count
class Other(Spam): ...



#元类
class Meta(type):
    def __new__(cls, *args, **kwargs): ...


class C(metaclass=Meta): ...


class test:
    def __init__(self):
        print("init")

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)

