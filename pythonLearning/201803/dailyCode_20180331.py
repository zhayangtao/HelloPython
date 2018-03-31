"""
特性和描述符是如何相关的
"""


class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, instanceType=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fget is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)


class Person:
    def getName(self):
        ...

    def setName(self, value):
        ...

    name = MyProperty(getName, setName)


class Person:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        if attr == 'name':
            print('fetch...')
            return self._name
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if attr == 'name':
            print('change...')
            attr = '_name'
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        if attr == 'name':
            print('change...')
            attr = '_name'
        del self.__dict__[attr]


print('_' * 20)
bob = Person('BOb Smith')
print(bob.name)
bob.name == 'Robert Smith'
print(bob.name)
del bob.name

print('_' * 20)
sue = Person('Sue Jones')
print(sue.name)


"""
计算属性
"""


class AttrSquare:
    def __init__(self, start):
        self.value = start

    def __getattr__(self, attr):
        if attr == 'X':
            return self.value ** 2
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value


"""
管理技术比较
"""


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def getSquare(self):
        return self._square ** 2

    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)


print('_' * 20)
x = Powers(3, 4)
print(x.square)
print(x.cube)
x.square = 5
print(x.square)


# 使用描述符做同样的逻辑
class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2

    def __set__(self, instance, value):
        instance._square = value


class DescCube:
    def __get__(self, instance, owner):
        print(self)
        print(instance)
        print(owner)
        return instance._cube ** 3


class Powers:
    square = DescSquare()
    cube = DescCube()

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube


print('_' * 20)
x = Powers(3, 4)
print(x.square)
print(x.cube)
x.square = 5
print(x.square)
