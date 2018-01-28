from types import MethodType


class Student(object):
    pass


# 给实例绑定属性
s = Student()
s.name = 'Mike'


# 给实例绑定方法
def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)

# 给class绑定方法
Student.set_age = set_age


# 使用 __slots__ 限制实例能创建的属性，仅对当前类实例起作用，对继承的子类无效
class Student1:
    __slots__ = ('name', 'age')


# 使用 @property 把方法变成属性
class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0 - 100')
        self._score = value


def teststudent2():
    student2 = Student2()
    student2.score = 2
    print(student2.score)


def testPy(a: list):
    print(a)

if __name__ == '__main__':
    title = "meaning " 'of' " life"
    teststudent2()
    mantra = """
    Always look on the bright side of life
    """
    testPy("1")

