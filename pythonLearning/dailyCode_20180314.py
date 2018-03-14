"""
运算符重载
"""


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data[i]

    def __iter__(self):
        print('iter=> ', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data


X = Iters([1, 2, 3, 4, 5])
print(3 in X)
for i in X:
    print(i, end=' | ')
print()
print([i ** 2 for i in X])
print(list(map(bin, X)))

I = iter(X)
while True:
    try:
        print(next(I), end=' @ ')
    except StopIteration as e:
        break


"""
属性引用
"""


class Empty:
    def __getattr__(self, attr):
        if attr == 'age':
            return 40
        else:
            raise AttributeError(attr)


X = Empty()
X.age
# X.name


class AccessControl:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value  # 不能使用 self.attr = value，会引起无限递归
        else:
            raise AttributeError(attr + ' not allowed')


X = AccessControl()
X.age = 40
X.age

# X.name = 'mel'

"""
模拟实力属性的私有性
"""


class PrivateExc(Exception):
    pass


class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


print('*' * 10)
X = Test1()
Y = Test2()
print(X.privates)
X.name = 'Bob'
# Y.name = 'Sue'
Y.age = 30
X.age = 40

""" 
import dailyCode_20180314


print('*' * 10)
print(dailyCode_20180314.X) """
