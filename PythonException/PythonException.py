def fetcher(obj, index):
    return obj[index]


try:
    x = 'spam'
    fetcher(x, 4)
except IndexError:
    print('got exception')
except (AttributeError, TypeError, SyntaxError):
    print("some exception")
except:
    print("got all exception")
else:
    print("no exception")
finally:
    print('finally')
# 抛错错误
raise IndexError

# 有条件抛错
assert False, 'Nobody expect the'


# 自定义异常
class Bad(Exception): ...


def doomed():
    raise Bad()


try:
    doomed()
except Bad:
    print('got bad')


def gobad(x, y):
    return x / y


def gosouth(x):
    print(gobad(x, 0))


seq = '-' * 32 + '\n'
print(seq + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(seq + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(seq + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

print(seq + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

try:
    ...
except IndexError:
    print('a')

# raise不包括异常名称或额外数据时，重新引发当前异常
try:
    raise IndexError('spam')
except IndexError:
    print('propagating')
    raise

# 异常链
try:
    1 / 0
except Exception as E:
    raise TypeError('Bad' * 8) from E


def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2


# 环境管理器
with open(r'C:\misc\data') as myfile:
    for line in myfile:
        print(line)
        ...


# 定义一个环境管理器对象
class TraceBlock:
    def message(self, arg):
        print('running', arg)

    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
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
    raise TypeError
    print('not reached')

with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line)


class General(Exception): pass


class Specific1(General): pass


class Specific2(General): pass


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
    except General:
        import sys

        print('caught:', sys.exc_info()[0])


# 提供异常方法
class FormatError(Exception):
    logfile = 'formaterror.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at', self.file, self.line, file=log)


def parser():
    raise FormatError(40, 'spam.txt')


try:
    parser()
except FormatError as exc:
    exc.logerror()
