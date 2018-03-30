"""
在元类中使用带标签的描述符
"""
from weakref import WeakKeyDictionary


class Descriptor:
    def __init__(self):
        self.label = None

    def __get__(self, instance, owner):
        print('__get__.label=%s' % self.label)
        return instance.__dict__.get(self.label, None)

    def __set__(self, instance, value):
        print('__set__')
        instance.__dict__[self.label] = value


class DescriptorOwner(type):
    def __new__(cls, name, bases, attrs):
        for n, v in attrs.items():
            if isinstance(v, Descriptor):
                v.label = n
        return super(DescriptorOwner, cls).__new__(cls, name, bases, attrs)


class Foo:
    __metaclass__ = DescriptorOwner
    x = Descriptor()


f = Foo()
f.x = 10
print(f.x)


"""
访问描述符的方法
"""


class CallbackProperty:
    """
    A property that will alert observers when upon updates
    """

    def __init__(self, default=None):
        self.data = WeakKeyDictionary()
        self.default = default
        self.callbacks = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        for callback in self.callbacks.get(instance, []):
            callback(value)
        self.data[instance] = value

    def add_callback(self, instance, callback):
        """
        Add a new function to call everytime the descriptor updates
        """
        if instance not in self.callbacks:
            self.callbacks[instance] = []
        self.callbacks[instance].append(callback)


class BankAccount:
    balance = CallbackProperty(0)


def low_balance_warning(value):
    if value < 100:
        print("you are poor")


ba = BankAccount()
# 使用实例调用描述符时，第一个参数是实例 instance=ba
# ba.balance.add_callback(ba, low_balance_warning) # error,ba.balance returns 0

# 使用类访问描述符时，第一个参数是类 instance=None
BankAccount.balance.add_callback(ba, low_balance_warning)
ba.balance = 5000
print('Balance is %s' % ba.balance)
ba.balance = 99
print('Balance is %s' % ba.balance)


"""
装饰器
"""


def outer(some_func):
    def inner():
        print('before some_func')
        ret = some_func()
        return ret + 1
    return inner


def foo():
    return 1


decorated = outer(foo)
decorated()


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)


def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


one = Coordinate(100, 200)
two = Coordinate(300, 200)
print(add(one, two))


def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0,
                             ret.y if ret.y > 0 else 0)
        return ret
    return checker


"""
通用装饰器
"""


def logger(func):
    def inner(*args, **kwargs):
        print('Arguments were: %s, %s' % (args, kwargs))
        return func(*args, **kwargs)
    return inner


@logger
def foo1(x, y=1):
    return x * y
