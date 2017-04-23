a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print(True and True)
print(10 / 3)

classmates = ['Michael', 'Bod', 'Tracy']
print(len(classmates))
classmates.insert(1, 'Jack')

if a >= 3:
    print('adult')
elif a >= 5:
    print('child')
else:
    pass

for name in classmates:
    print(name)

# dict
d = {'Micheal': 98, 'Bob': 45}
print(d['Micheal'])
print(d.get('Thomas', -1))

# set
s = {1, 2, 3}
s.add(3)
s.remove(3)

# list
L = {1, 2, 3}


# 函数
def m_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('类型错误')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


# m_abs('a')


# 默认参数 必须只想不变对象
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


# 使用 *nums 将list所有参数传入
nums = [1, 2, 3]
calc(*nums)


# calc(nums)


# 关键字参数
def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)


person(name='Jovi', age=25)
person(name='Jovi', age=25, city='SH')
person(name='Jovi', age=25, gender='M', city='SH')
extra = {'city': 'SH', 'job': 'Engineer'}
person(name='Jovi', age=25, **extra)


def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'jopb' in kw:
        pass
    print('name', name, 'age', age, 'other', kw)


person('Jovi', 25, city='SH', addr='Zhangjiang')


# 命名关键字参数：限制关键字参数名字，* 号后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jovi', 25, city='SH', job='Engineer')


# 如果已存在可变参数，后面的命名关键字参数就不需要 *
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数可以设置默认值
def person(name, age, *, city='SH', job):
    print(name, age, city, job)


person('Jovi', 25, job='Engineer')

# 切片
L = ['Micheal', 'Spark', 'Bob', 'Jack']
print(L[: 3])
print(L[-1])

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, ':', v)

from collections import Iterable

print(isinstance('abv', Iterable))

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

# 列表生成式
list(range(1, 11))
var = [x * x for x in range(1, 11)]
var = [x * x for x in range(1, 11) if x % 2 == 0]
[m + n for m in 'ABC' for n in 'ZYX']

import os

d = [d for d in os.listdir('..')]
print(d)

# 生成器
g = (x * x for x in range(10))
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


g = fib(6)
while True:
    try:
        x = next(g)
        print('g', x)
    except StopIteration as e:
        print('Generator return Value', e.value)
        break


# 杨辉三角
def triangles(line):
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


n = 0
for t in triangles(10):
    print(t)
    n = n + 1
    if n == 10:
        break

# 迭代器
isinstance((x for x in range(10)), Iterable)


# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


# map
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4])
print(list(r))
list(map(str, [1, 2, 3]))

from functools import reduce


def add(x, y):
    return x + y


reduce(add, [1, 3, 5, 7, 9])


def str2Int(s):
    def fn(x, y):
        return x * 10 + y

    def char2Num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2Num, s))


# 使用 y 表达式
def char2Num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2Int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2Num, s))

