"""
raise from
"""


try:
    1 / 0
except Exception as e:
    ...
    # raise TypeError('bad!' * 8) from e


def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2


# f(1)
"""
环境管理协议
"""


class TraceBlock:
    def message(self, arg):
        print('running', arg)

    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception!', exc_type)
            return False


with TraceBlock() as action:
    action.message('test 1')
    print('reached')

with TraceBlock() as action:
    action.message('test 2')
    # raise TypeError
    print('not reached')
# 嵌套环境管理器
with TraceBlock() as a, TraceBlock() as b:
    a.message('test 1')
    b.message('test 2')

""" 
异常对象
"""


class General(Exception):
    pass


class Specific1(General):
    pass


class Specific2(General):
    pass


def raiser0():
    x = General()
    raise x


def raiser1():
    x = Specific1()
    raise x


def raiser2():
    x = Specific2()
    raise x


for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General as e:
        import sys
        print('caught:', sys.exc_info()[0])


try:
    raise General()
    1 / 0
except (General, Specific1, Specific2) as e:
    import sys
    print('caught:', sys.exc_info()[0])
    pass

"""
定制打印显示
默认情况下，捕获并打印基于类的异常的实例的时候，
它们会显示我们传递给类构造函数的任何内容。
"""


class MyBad(Exception):
    def __str__(self):
        return 'Always look on the bright side of life...'


try:
    raise MyBad('Sorry-my mistake!')
except MyBad as e:
    print(e)


"""
提供异常细节
"""


class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file


def parser():
    raise FormatError(442, file='spam.txt')


try:
    parser()
except FormatError as e:
    print('Error at', e.file, e.line)
except FormatError as e:
    print('Error at:', e.args[0], e.args[1])
