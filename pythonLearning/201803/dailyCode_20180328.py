"""
描述符
"""


class DescSquare:
    def __init__(self, start):
        self.value = start

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value


class Client1:
    x = DescSquare(3)


class Client2:
    x = DescSquare(32)


c1 = Client1()
c2 = Client2()
print(c1.x)
c1.x = 4
print(c1.x)
print(c2.x)


"""
在描述符中使用状态信息
"""


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
    x = DescState(2)
    y = 3

    def __init__(self):
        self.z = 4


print()
print()
print()
print('*' * 32)
obj = CalcAttrs()
print(obj.x, obj.y, obj.z)
obj.x = 5
obj.y = 6
obj.z = 7
print(obj.x, obj.y, obj.z)


"""
对描述符存储或使用附加到客户类的实例的一个属性，而不是自己的属性，是可行的
"""


class InstState:
    "附加到实例的属性"

    def __get__(self, instance, owner):
        print('InstState get')
        return instance._Y * 100

    def __set__(self, instance, value):
        print('InstState set')
        instance._Y = value


class CalcAttrs:
    x = DescState(2)
    y = InstState()

    def __init__(self):
        self._Y = 3
        self.z = 4


print()
print()
print()
print('*' * 32)
obj = CalcAttrs()
print(obj.x, obj.y, obj.z)
obj.x = 5
obj.y = 6
obj.z = 7
print(obj.x, obj.y, obj.z)


class Movie(object):
    def __init__(self, title, rating, runtime, budget, gross):
        self._budget = None

        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.gross = gross
        self.budget = budget

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._budget = value

    def profit(self):
        return self.gross - self.budget


print()
print()
print()
print('*' * 32)
m = Movie('Casablanca', 97, 102, 964000, 1300000)
print(m.budget)
