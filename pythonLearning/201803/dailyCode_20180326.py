import sys


L = [1, 2, 4]
print(L[0:2])


def func():
    try:
        ...
    except:
        ...


def bye():
    sys.exit(40)


try:
    bye()
except:
    print('got it')
print('continuing...')

print(sys.getdefaultencoding())
b = b'spam'
s = 'eggs'
print(type(b), type(s))

print(s.encode())
print(bytes(s, 'utf8'))
b = b'spam'
print(b.decode())
print(str(b, encoding='utf8'))


# bytes(s)  # error

s = 'spam'
c = bytearray(s, encoding='utf-8')
print(c)
# c[0] = 'x'  # TypeError: an integer is required
c[0] = 198
print(c)
print(set(dir(b'abc')) - set(bytearray(b'abc')))


file = open('temp', 'w')
size = file.write('abc\n')
file.close()
file = open('temp')
text = file.read()
print(text)

open('temp', 'w').write('abc\n')
open('temp', 'r').read()


"""
管理属性
__getattr__ 和 __setattr__ 方法，把未定义的属性获取和所有的属性赋值只想通用的处理器方法
"""


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


print()
print()
print()
print()

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print(Person.name.__doc__)


"""
计算的属性
"""


class PropSquare:
    def __init__(self, start):
        self.value = start

    def getX(self):
        return self.value ** 2

    def setX(self, value):
        self.value = value

    x = property(getX, setX)


p = PropSquare(3)
q = PropSquare(32)
print(p.x)


"""
使用装饰器编写特性
property对象也有 getter 、 setter 和 deleter 方法，
"""


class Person:
    def __init__(self, name):
        self._name = name

    @property   # name = property(name)
    def name(self):
        "name property docs"
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name


print()
print()
print()
print()
bob = Person('BOb smith')
print(bob.name)