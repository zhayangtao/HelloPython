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
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
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
s.score = 88  # 'Student' object has no attribute 'score'

class GradStudent(Student):
    pass
g = GradStudent()
g.score = 666