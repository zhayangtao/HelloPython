# 偏函数
import functools

int2 = functools.partial(int, base=2)


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self, std):
        print('%s: %s' % (std.__name, std.__score))
