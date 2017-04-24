std1 = {'name': 'Micheal'}


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_score(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lili = Student('Lili Simpson', 67)
bart.print_score()
lili.print_score()


# 访问限制  在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


bart = Student('bart Simpson', 87)


# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
# bart.__name  # 'Student' object has no attribute '__name'


# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')

    def eat(self):
        print("Eating meat")


class Cat(Animal):
    def run(self):
        print('Cat is running')

    def eat(self):
        print('Eating mouse')


# 获取对象信息
# 1、使用type
type(123)
type(None)
type(123) == int
# 使用 types模块定义的常量判断一个对象是否是函数
import types


def fn():
    pass


type(fn) == types.FunctionType  # True
type(abs) == types.BuiltinFunctionType  # True
type(lambda x: x) == types.LambdaType  # True
type((x for x in range(10))) == types.GeneratorType  # True

# 使用 isinstance 判断继承关系
a = Animal()
d = Dog()
isinstance(a, Animal)

isinstance([1, 2, 3], (list, tuple))

# 使用dir获取对象所有属性和方法
dir('ABC')


class MyDog(object):
    def __len__(self):
        return 100

    def act(self):
        print('woof')


dog = MyDog()
print(len(dog))  # 100

# 使用 getattr、setattr、hasattr直接操作一个对象的状态
hasattr(dog, 'x')
setattr(dog, 'x', 19)
getattr(dog, 'x')
getattr(dog, 'x', 404)
# 也可以获得对象的方法
hasattr(dog, 'act')
fn = getattr(dog, 'act')
fn()


# 面向对象高级编程
# 给实例绑定一个属性
class Student(object):
    pass


s = Student()
s.name = 'Mike'
print(s.name)


# 给实例绑定给一个方法
def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(34)
print(s.age)
# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
# s2.set_age(44)  # 'Student' object has no attribute 'set_age'


# 可以给class绑定方法，所有实例均可调用
Student.set_age = set_age


# __slots__变量，来限制该class实例能添加的属性，
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = 'jojo'
s.age = 34


# s.score = 88  # 'Student' object has no attribute 'score'


class GradStudent(Student):
    pass


g = GradStudent()
g.score = 666


# 使用 @property
class Student(object):
    def get_score(self):
        return self.get_score()

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100!')
        self._score = value


# Python内置的 @property 装饰器就是负责把一个方法变成属性调用的：
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100!')
        self._score = value


# 还可以定义只读属性，只定义getter方法，不定义setter方法
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth


# 多重继承
class Runnable(object):
    def run(self):
        print('Running')


class Flyable(object):
    def fly(self):
        print('Flying')


class Chicken(Runnable, Flyable):
    pass


# MixIn


# 定制类
# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student('Michael'))  # Student object (name: Michael)
s = Student('Micheal')
s  # <__main__.Student object at 0x109afb310>


# 直接显示变量调用的不是__str__()，而是__repr__()
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


# __iter__ 如果一个类想被用于for ... in循环，类似list或tuple那样，
# 就必须实现一个__iter__()方法，该方法返回一个迭代对象
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法，直到遇到StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)


# __getitem__ 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a
f = Fib()[12]
print(f)

class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            