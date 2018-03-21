class newstyle(object):
    ...


class C:
    pass


x = C()
print(type(x))
print(isinstance(x, C))


"""
钻石继承法则
"""


class A:
    attr = 1


class B(A):
    # attr = 4
    pass


class C(A):
    attr = 2


class D(B, C):
    pass


x = D()
print(x.attr)


"""
__slots__ 实例
"""


class limiter(object):
    __slots__ = ['age', 'name', 'job']


x = limiter()
# print(x.age)
x.age = 40
print(x.age)

# x.app = 490


class ct:
    __slots__ = ['a', 'b']


x = ct()
x.a = 1
# print(x.__dict__) #AttributeError: 'ct' object has no attribute '__dict__'
getattr(x, 'a')
# setattr(x, 'c', 1)

print('b' in dir(x))


# 不能给不在 slots 列表中名称的实例分配名称
class D:
    __slots__ = ['a', 'b']

    def __init__(self):
        self.d = 4


# x = D() # AttributeError: 'D' object has no attribute 'd'

# 可以通过在 slots 中包含 __dict__ 设置额外属性
class D:
    __slots__ = ['a', 'b', '__dict__']
    c = 3

    def __init__(self):
        self.d = 4


x = D()
print(x.d)
x.a = 3
x.b = 4


print('*' * 10)
for attr in list(x.__dict__) + x.__slots__:
    print(attr, '=>', getattr(x, attr))


class E:
    __slots__ = ['c', 'd']


class F(E):
    __slots__ = ['a', '__dict__']


print()
print()
print('*' * 10)
x = F()
x.a = 1
x.b = 2
x.c = 3
print(E.__slots__)
print(F.__slots__)
print(x.__slots__)
print(x.__dict__)

for attr in list(getattr(x, '__dict__', [])) + getattr(x, '__slots__', []):
    print(attr, '=>', getattr(x, attr))
