"""
单体类
"""


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


bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())


x = Spam(42)
y = Spam(99)
print(x.attr, y.attr)


def singleton2(aClass):
    instance = None

    def onCall(*args):
        nonlocal instance
        if instance is None:
            instance = aClass(*args)
        return instance
    return onCall


class singleton:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args):
        if self.instance is None:
            self.instance = self.aClass(*args)
        return self.instance


"""
跟踪对象接口
"""


# 非装饰器委托
class Wrapper:
    def __init__(self, object):
        self.wrapper = object

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapper, attrname)


print('_' * 20)
x = Wrapper([1, 2, 3])
x.append(4)
print(x.wrapper)


def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)

        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper
