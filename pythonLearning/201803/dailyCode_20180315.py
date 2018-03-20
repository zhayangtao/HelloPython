
def test(i: list, s: set) -> int:
    """
    function doc
    """
    return 1


print(test(1, 2))


map(bin, [1, 2])


"""
定义 __repr__ 和 __str__ 的云算法重载方法
"""


class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


x = Adder()
print(x)


class Addrepr(Adder):
    def __repr__(self):
        return 'Addrepr(%s)' % self.data

    __str__ = __repr__


print('*' * 10)
print(Addrepr())


"""
__add__ 方法不支持 + 运算符右侧使用实例对象
当右侧是对象时，可以重写 __radd__ 方法，
"""


class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val


print('*' * 10)
x = Commuter(88)
y = Commuter(99)
print(x + 1)
print(1 + y)


class Commuter2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter2):
            other = other.val
        return Commuter2(self.val + other)

    def __radd__(self, other):
        return Commuter2(other + self.val)

    def __str__(self):
        return '<Commuter2: %s>' % self.val

    __repr__ = __str__


print('*' * 10)
x = Commuter2(88)
y = Commuter2(99)
print(x + 10)
z = x + y
print(z)

# 原处加法 __iadd__


class Number:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        print('__iadd__')
        self.val += other
        return self


print('*' * 10)
x = Number(5)
x += 1
x += 1
print(x.val)


class Number2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('__add__')
        return Number2(self.val + other)


x = Number2(5)
x += 1
x += 1
print(x.val)


class Prod:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value * other


print('*' * 10)
x = Prod(2)
print(x(3))


"""
函数回调和回调代码
"""


class Callback:
    def __init__(self, color):
        self.color = color

    def __call__(self):
        print('turn', self.color)


cb3 = (lambda color='red': 'turn ' + color)
print(cb3())
