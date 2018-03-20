from dailyCode_20180310_classtools import AttrDisplay


class Person(AttrDisplay):
    """
    create and process person records
    """

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    """
    A customized Person with special requirements
    """

    def __init__(self, name, pay):
        super().__init__(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=10):
        super().giveRaise(percent + bonus)


class MixedNames:
    data = 'spam'

    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)


class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)


class Super:
    def method(self):
        print('in Super.method')
        self.action()

    def action(self):
        raise NotImplementedError('action must be defined')


class Sub(Super):
    def method(self):
        print('starting Sub.method')
        super().method()
        print('ending Sub.method')


class INheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extender.method')
        super().method()
        print('ending Extender.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')


########################################
# 抽象类
########################################
from abc import ABCMeta, abstractmethod


class abstractClass(metaclass=ABCMeta):
    @abstractmethod
    def method(self, *args):
        pass


def main():
    x = Super()
    x.method()
    y = Sub()
    y.method()
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)


if __name__ == '__main__':
    main()
