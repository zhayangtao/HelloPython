def f(x):
    return x * x


r = list(map(f, [1, 2, 3, 4, 5]))
print(r)


from functools import reduce


def multiply(x, y):
    return x * y


re = reduce(multiply, [1, 2, 3, 4, 5])
print(re)


def fn(x, y):
    return x * 10 + y


digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, digits.values())))


def not_empty(s: str):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


"""
用 filter 求素数
"""


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


"""
筛选器
"""


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


import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


"""
偏函数
"""

int2 = functools.partial(int, base=2)
print(int2('10000'))
