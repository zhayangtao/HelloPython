# 元类
class Meta(type):
    def __new__(cls, classname, supers, classdict):
        # Run by inherited type.__call_
        return type.__new__(cls, classname, supers, classdict)


# 示例：将打印添加到元类和文件以便追踪
class MetaOne(type):
    def __new__(cls, classname, supers, classdict):
        print('In MetaOne.new:', classname, supers, classdict, sep='\n...')
        # Run by inherited type.__call_
        return type.__new__(cls, classname, supers, classdict)


class Eggs:
    pass


print('making class')


class Spam(Eggs, metaclass=MetaOne):
    data = 1

    def meth(self, arg):
        pass


print('making instance')
X = Spam()
print('data:', X.data)


# 定制构建和初始化
class MetaTwo(type):
    def __new__(cls, classname, supers, classdict):
        print('In MetaTwo.new:', classname, supers, classdict, sep='\n...')
        # Run by inherited type.__call_
        return type.__new__(cls, classname, supers, classdict)

    def __init__(cls, classname, supers, classdict):
        print('In MetaTwo init:', classname, supers, classdict, sep='\n...')


class Eggs:
    pass


print('*************************')
print('making class')


class Spam(Eggs, metaclass=MetaTwo):
    data = 1

    def meth(self, arg):
        pass


print('making instance')
X = Spam()
print('data:', X.data)


# 使用简单的工厂函数，任何可调用对象都可以用作一个元类
# A simple function can serve as a metaclass too
def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)


class Eggs:
    pass


print('*************************')
print('making class')


class Spam(Eggs, metaclass=MetaFunc):
    data = 1

    def meth(self, arg):
        pass


print('making instance')
X = Spam()
print('data:', X.data)


# 示例：向类添加方法
# 1 手动扩展
# Extend manually - adding new methods to classes
class Client1:
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2:
    value = 'ni?'


def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


print('********************')
Client1.eggs = eggsfunc
Client1.ham = hamfunc

Client2.eggs = eggsfunc
Client2.ham = hamfunc

X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


# 基于元类的扩展
# Extend with a metaclass - supports future changes better
def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


class Extender(type):
    def __new__(cls, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(cls, classname, supers, classdict)


class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2(metaclass=Extender):
    value = 'ni?'


print('********************')
X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


# 基于装饰器的扩展
# Extend with a decorator: same as providing __init__ in a metaclass
def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


def Extender(aClass):
    aClass.eggs = eggsfunc
    aClass.ham = hamfunc
    return aClass


@Extender
class Client1:
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


@Extender
class Client2:
    value = 'ni?'


print('********************')
X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


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


class Person:
    @tracer
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


print('********************')
bob = Person('Bob smith', 50000)
sue = Person('sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())

# 用元类和装饰器跟踪
# Metaclass that adds tracing decorator to every method of a client class
from types import FunctionType


class MetaTrace(type):
    def __new__(cls, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType:
                classdict[attr] = tracer(attrval)
        return type.__new__(cls, classname, supers, classdict)


class Person(metaclass=MetaTrace):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


print('********************')
bob = Person('Bob smith', 50000)
sue = Person('sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())


# 把任何装饰器应用于方法
# Metaclass factory:apply any decorator to all methods of a class


def decorateAll(decorator):
    class MetaDecorate(type):
        def __new__(cls, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if type(attrval) is FunctionType:
                    classdict[attr] = decorator(attrval)
            return type.__new__(cls, classname, supers, classdict)

    return MetaDecorate


class Person(metaclass=decorateAll(tracer)):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


print('********************')
print("decorateAll")
bob = Person('Bob smith', 50000)
sue = Person('sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())

#  元类与类装饰器的关系
# class decorator factory: apply any decorator to all methods of a class
from types import FunctionType


def decoratorAll(decorator):
    def DecoDecorator(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(aClass, attr, decorator(attrval))
        return aClass

    return DecoDecorator


@decoratorAll(tracer)
class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


print('********************')
print("decoratorAll***")
bob = Person('Bob smith', 50000)
sue = Person('sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())
