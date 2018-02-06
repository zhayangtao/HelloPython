for line in open('README.MD'):
    print(line, end='')

import os

p = os.popen('dir')

f = open('README.MD')
lines = f.readlines()
lines = [line.rstrip() for line in lines]
print(lines)
lines = [line.rstrip() for line in open('README.MD') if line[0] == '#']
print(lines)

import sys

print(sys.path)
map(str.upper, open('README.MD'))
list(map(str.upper, open('README.MD')))
list(map(lambda x: x.upper(), open('README.MD')))
zip([1, 2, 3, 4], [2, 3, 4])
zip([1, 2, 3, 4], [2, 3, 4, 5, 7])

# 内置函数
import functools, operator

sorted(open('README.MD'))
list(zip([1, 2, 3, 4], [2, 3, 4, 5, 7]))
list(enumerate(open('README.MD')))
list(filter(bool, open('README.MD')))
functools.reduce(operator.add, open('README.MD'))

sorted((1, 2, 3, 5, 4)) # sorted返回列表
tuple(1, 2, 3)

# range支持在其结果上的多个迭代器，zip、map、filter不支持
r = range(3)
# next(r) # TypeError
I1 = iter(r)
I2 = iter(r)
I3 = iter(r)

d = dict(a=1, b=2, c=3)
