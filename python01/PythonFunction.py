from functools import reduce


def normalize(aL):
    def touppercase(L):
        return L[0].upper() + L[1:].lower()
    return map(touppercase, aL)

L = ['adam', 'LISA', 'barT']
print(list(normalize(L)))


def prod(L):
    def star(x, y):
        return x * y
    return reduce(star, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2Num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    dot = s.index('.')
    s = s[:dot] + s[dot+1:]
    result = reduce(fn, map(char2Num, s))
    result /= 10 ** (len(s) - dot)
    return result


# filter
print(10 ** 5)
def is_odd(n):
    return n % 2 == 0
print(list(filter(is_odd, [1,2,3,4,5,6,7])))


def not_empty(s):
    return s and s.strip()
list(filter(not_empty, ['a','','b']))


# 用filter实现素数查找
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# sorted函数
sorted([45, 46,22, 7])
sorted([-14, -13, 65, -6] , key=abs)
sorted([-14, -13, 65, -6] , key=abs, reverse=True)


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)


# 返回函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

for i in range(1, 4):
    print(i)


# 匿名函数
list(map(lambda x:x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 装饰器 在代码运行期间动态增加功能的方式，称之为“装饰器
def now():
    print('2017-04-23')
now.__name__
f = now
f.__name__


# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2017-04-23')

now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('executor')
def now():
    print('2017')

now()


# 完整的decorator
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 偏函数
int2 = functools.partial(int, base=2)
print(int2('10000'))
print(int2('10000', base=10))

