"""
提供异常方法
"""


class FormatError(Exception):
    logfile = 'formaterror.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        log = open(self.logfile, 'w')
        print('Error at:', self.file, self.line, file=log)


def parser():
    raise FormatError(40, 'spam20180324.txt')


try:
    parser()
except FormatError as e:
    e.logerror()


"""
异常的设计
"""


def action2():
    print(1 + [])


def action1():
    try:
        action2()
    except TypeError:
        print('inner try')


try:
    action1()
except TypeError as e:
    print('outer try')


"""
语法嵌套
"""

try:
    try:
        action2()
    except TypeError as identifier:
        print('inner try')
except TypeError as e:
    print('outer try')


try:
    try:
        pass
        # raise IndexError
    finally:
        print('spam')
finally:
    print('SPAM')


def raise1():
    raise IndexError


def noraise():
    return


def raise2():
    raise SyntaxError


for func in (raise1, noraise, raise2):
    print('\n', func, sep='')
    try:
        try:
            func()
        except IndexError as identifier:
            print('caught IndexError')
    finally:
        print('finally run')


class Found(Exception):
    pass


def searcher():
    if 1:
        raise Found
    else:
        return
