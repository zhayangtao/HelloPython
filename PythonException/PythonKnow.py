# _*_ coding:utf-8 _*_\
import re

s = 'Bugger all down here on earth!'
b = b'Buffer all down here on earth!'
re.match('(.*) down (.*) on (.*)', s).group()


class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('remove...')
        del self._name

    name = property(getName, setName, delName, "name property docs")


# 装饰器
class person2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        "name property docs"
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name


class Descriptor(object):
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:
    attr = Descriptor()


# 描述符类
class Name:
    "name descriptor docs"

    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    def __delete__(self, instance):
        print('remove...')
        del instance._name


class Person:
    def __init__(self, name):
        self._name = name

    name = Name()


class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('DescState get')
        return self.value * 10

    def __set__(self, instance, value):
        print('DescState set')
        self.value = value


class CalcAttrs:
    X = DescState(2)
    Y = 3

    def __init__(self):
        self.Z = 4


# 计算属性
class AttrSquare:
    def __init__(self, start):
        self.value = start

    def __getattr__(self, item):
        if item == 'x':
            return self.value ** 2
        else:
            raise AttributeError(item)

    def __setattr__(self, key, value):
        if key == 'X':
            key = 'value'
        self.__dict__[key] = value


# 使用超类object的getAttribute 避免循环
class AttrSquare:
    def __init__(self, start):
        self.value = start

    def __getattribute__(self, item):
        if item == 'X':
            return self.value ** 2
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'X':
            key = 'value'
        object.__setattr__(self, key, value)


class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, item):
        print('get: ' + item)
        return 3


# 不重载的情况下拦截方法调用
class GetAttr:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattr__(self, item):
        print('getattr: ' + item)
        if item == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttrbute(object):
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__:442')
        return 42

    def __getattribute__(self, item):
        print('getattrbute:' + item)
        if item == '__str__':
            return lambda *args: ['Getattribute str']
        else:
            return lambda args: None


'''
for Class in GetAttr, GetAttrbute:
    print('\n' + Class.__name__.ljust(50, '='))
    X = Class()
    X.eggs
    X.spam
    X.other
    len(X)

    try:
        X[0]
    except Exception:
        print('fail []')

    try:
        X()
    except Exception:
        print('fail ()')
    X.__call__()
'''


# 基于委托的Manager
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, item):
        print('getattr: ' + item)
        return getattr(self.person, item)

    def __str__(self):
        return str(self.person)


if __name__ == '__main__':
    sue = Person('Sue', job='dev', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)

    tom = Manager('Tom', pay=500000)
    print(tom.lastName())


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattribute__(self, attr):
        print('**', attr)
        if attr in ['person', 'giveRaise']:
            return object.__getattribute__(self, attr)
        else:
            return getattr(self.person, attr)


class CardHolder:
    acctlen = 8
    retireage = 59

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(getName, setName)

    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value

    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'

    def setAcct(self, value):
        value = value.replace('_', '')
        if len(value) != self.acctlen:
            raise TypeError('invalid acct number')
        else:
            self.__acct = value

    acct = property(getAcct, setAcct)

    def remainGet(self):
        return self.retireage - self.age

    remain = property(remainGet)


bob = CardHolder('1234-5678', 'bob smith', 40, '123 main st')
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
bob.name = 'bob Q. Smith'
bob.age = 50
bob.acct = '23-45-67-89'
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')


class CardHolder:
    acctlen = 8
    retireage = 59

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name:
        def __get__(self, instance, owner):
            return self.name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value

    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value

    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace('_', '')
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number')
            else:
                self.acct = value

    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age

        def __set__(self, instance, value):
            raise TypeError('cannot| set remain')

    remain = Remain()


