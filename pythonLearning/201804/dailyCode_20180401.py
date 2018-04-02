"""
重访基于委托的 Manager
"""


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

    __repr__ = __str__


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)


sue = Person('Sue Jones', job='dev', pay=100000)
print(sue.lastName())
sue.giveRaise(.10)
print(sue)
tom = Manager('Tom Jones', 50000)
print(tom.lastName())
tom.giveRaise(.10)
print(tom)


"""
使用特性来验证
"""


class CardHolder:
    acctlen = 8
    retireage = 65

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value

    @property
    def acct(self):
        return self.__acct[:-3] + '***'

    @acct.setter
    def acct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invalid acct number')
        else:
            self.__acct = value

    def remainGet(self):
        return self.retireage - self.age
    remain = property(remainGet)


print('_' * 20)
bob = CardHolder('1234-5678', 'bob smith', 40, '123 main st')
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')


"""
使用描述符验证
"""


class CardHolder:
    acctlen = 8
    retireage = 65

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Acct:
        def __get__(self, innstance, owner):
            return self.acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number')
            else:
                self.acct = value

    acct = Acct()

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

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age

        def __set__(self, instance, value):
            raise TypeError('cannot set remain')

    remain = Remain()


"""
函数装饰器
"""


def decorator(F):
    def wrapper(*args):
        pass
    return wrapper


@decorator
def func():
    pass


print('_' * 20)
print(func(6, 7))
"""
类装饰器
"""


class decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print('__call__')
        pass


@decorator
def func(x, y):
    ...


print(func(6, 7))
