"""
异常
"""


try:
    raise IndexError
except IndexError as e:
    print('got IndexError')


"""
自定义异常
"""


class Bad(Exception):
    pass


def doomed():
    raise Bad()


try:
    doomed()
except Bad as bad:
    print('got bad')
finally:
    print('finally')


try:
    print(1)
    # raise(Exception)
except Exception as e:
    print('e')
else:
    print('else')
finally:
    print('finally')


"""
捕捉内置异常
"""


def kaboom(x, y):
    print(x + y)


try:
    kaboom([0, 1, 2], 'spam')
except TypeError as e:
    print('typeError')
print('resuming here')


"""
合并 try 的例子
"""


sep = '_' * 32 + '\n'
print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError as e:
    print('except run')
finally:
    print('finally run')
print('after run')


print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')


print(sep + 'EXCEPTIO RAISED BUT NOT CAUGHT')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')
