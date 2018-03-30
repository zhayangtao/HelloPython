from weakref import WeakKeyDictionary
"""
property 的不足
"""


class Movie:
    def __init__(self, title, rating, runtime, budget, gross):
        self._rating = None
        self._runtime = None
        self._budget = None
        self._gross = None

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
            raise ValueError('Negative value not allowed: %s' % value)
        self._budget = value

    ...
    # 其他属性也要类似书写，balabala


"""
使用描述符
"""


class NonNegative:
    """ 
    A descriptor that forbids negative values
    """

    def __init__(self, default):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.data[instance] = value


class Movie:
    rating = NonNegative(0)
    runtime = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)

    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    def profit(self):
        return self.gross - self.budget


m = Movie('Cashblance', 97, 102, 964000, 1300000)
print(m.budget)
m.rating = 100
try:
    m.rating = -1
except ValueError as e:
    print('oops, negative value')


"""
描述符必须定义在类的层次上
"""


class Broken(object):
    y = NonNegative(5)

    def __init__(self):
        self.x = NonNegative(0)  # 实例层次的描述符只会返回描述符本身


b = Broken()
print('x is %s, y is %s' % (b.x, b.y))


"""
确保实例数据只属于实例本身
"""


class BrokenNonNegative:
    def __init__(self, default):
        self.value = default

    def __get__(self, instance, owner):
        print(type(owner))
        print(type(instance))
        return self.value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Negative value not allowed: %s' % value)
        self.value = value


class Foo:
    bar = BrokenNonNegative(5)


f = Foo()
try:
    f.bar = 2
    print(f.bar)
    f.bar = -1
except ValueError:
    print('Caught the invalid assignment')


"""
所有 Foo 的实例共享相同的 bar，所以需要使用其他方式保存数据
比如 NonNegative 使用了一个字典来保存专属于实例的数据，
一般来说没有问题，除非使用了不可哈希的对象
"""


class MoProblems(list):
    x = NonNegative(5)


m = MoProblems()
print(m.x)
