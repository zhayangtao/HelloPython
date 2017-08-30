# 计时调用
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
    return list(map((lambda x: x * 2), range(N)))


result = listcomp(5)
listcomp(500000)
listcomp(5000000)
listcomp(10000000)
print(result)
print('allTime = %s' % listcomp.alltime)
print('*****************')

result = mapcall(5)
mapcall(500000)
mapcall(5000000)
mapcall(10000000)
print(result)
print('allTime = %s' % mapcall.alltime)


# 添加装饰器参数
def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
            return result

    return Timer


# 单体类
instances = {}


def getInstance(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]


def singleton(aClass):
    def onCall(*args):
        return getInstance(aClass, *args)

    return onCall


@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton
class Spam:
    def __init__(self, val):
        self.attr = val


bob = Person('bob', 40, 10)
print(bob.name, bob.pay())

sue = Person('sue', 50, 20)
print(sue.name, sue.pay())


def singleton(aClass):
    instance = None

    def onCall(*args):
        nonlocal instance
        if instance is None:
            instance = aClass(*args)
        return instance

    return onCall


class singleton:
    def __init__(self, aClass):
        self.aClsss = aClass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.aClsss(*args)
        return self.instance


# 跟踪对象接口
class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        print('Trace:', item)
        return getattr(self.wrapped, item)


def Tracer(aClass):
    class wrapper:
        def __init__(self, *args, **kwargs):
           self.fetches = 0
           self.wrapped = aClass(*args, **kwargs)

        def __getattr__(self, item):
            print('Trace:' + item)
            self.fetches += 1
            return getattr(self.wrapped, item)
    return Wrapper

@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)

@Tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate

