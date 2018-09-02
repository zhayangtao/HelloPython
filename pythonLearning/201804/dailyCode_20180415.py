"""
用常规类重载类创建调用
"""


class SuperMeta:
    def __call__(self, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class


class SubMeta(SuperMeta):
    def __New__(self, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


class Eggs:
    pass


print('making class')


class Spam(Eggs, metaclass=SubMeta()):
    data = 1

    def meth(self, arg):
        pass


print('making instance')
x = Spam()
print('data:', x.data)
print('_' * 20)


"""
元类声明由子类继承
元类属性没有由类实例继承
"""


class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict)

    def toast(self):
        print('toast')


class Super(metaclass=MetaOne):
    def spam(self):
        print('spam')


class C(Super):
    def eggs(self):
        print('eggs')


x = C()
x.eggs()
x.spam()
# x.toast() # object has no attribute 'toast'


"""
基于元类的扩展
"""


def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)


class Client(metaclass=Extender):
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2(metaclass=Extender):
    value = 'ni?'


x = Client('Ni!')
print(x.spam())
print(x.eggs())
print(x.ham('bacon'))

y = Client2()
print(y.eggs())
print(y.ham('bacon'))


"""
基于装饰器的扩展
"""


def Extender(aClass):
    aClass.eggs = eggsfunc
    aClass.ham = hamfunc
    return aClass


@Extender
class Client3:
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


@Extender
class Client4:
    value = 'Ni?'


"""
类装饰器可以管理类和实例
元类可以管理类和实例，但管理实例需要额外工作
"""

# 用装饰器手动跟踪


def tracer(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall


import time


def timer(label='', trace=True):
    def onDecorator(func):
        def onCall(*args, **kwargs):
            start = time.clock()
            result = func(*args, **kwargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                value = (label, func.__name__, elapsed, onCall.alltime)
                print(format % value)
                return result
            onCall.alltime = 0
        return onCall
    return onDecorator


"""
用元类和装饰器跟踪
"""


from types import FunctionType


class MetaTrace(type):
    def __new__(meta, classname, supers, classdict: dict):
        for attr, val in classdict.items():
            if type(val) is FunctionType:
                classdict[attr] = tracer(val)
        return type.__new__(meta, classname, supers, classdict)


class Person(metaclass=MetaTrace):
    def __init__(self, name: str, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


bob = Person('bob', 400)
"""Person
把任何装饰器应用于方法
"""


def decorateAll(decorator):
    class MetaDecorate(type):
        def __new__(meta, classname, supers, classdict):
            for attr, val in classdict.items():
                if type(val) is FunctionType:
                    classdict[attr] = decorator(val)
            return type.__new__(meta, classname, supers, classdict)
    return MetaDecorate


class Person(metaclass=decorateAll(tracer)):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]
