class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must be between 0 - 100")
        self._score = value

    @property
    def age(self):
        return 2018 - 1992


s = Student()
s.score = 1
# s.age = 2


"""
使用枚举类
"""


from enum import Enum, unique


Month = Enum("Month", ('jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)


"""
异常处理
"""


print('_' * 20)
try:
    print("try...")
    r = 10 / 2
    print("result:", r)
except ValueError as e:
    print("valueError:', e")
else:
    print("no error")
finally:
    print("finally")
print("end")


"""
记录错误
"""
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar("0")
    except Exception as e:
        logging.exception(e)


main()
print("ENd")


"""
抛出错误
"""


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError("invalid value: %s" % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('valueError')
        raise  # raise语句如果不带参数，就会把当前错误原样抛出。


bar()
