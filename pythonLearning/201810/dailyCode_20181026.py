"""
ax ** 2 + bx + c = 0
"""
import cmath
import math
import sys

li = [lambda: x for x in range(10)]
print(li[1]())
print('45' '8888')
print('45', '8888')

for x in range(10):
    print(x)

flist = []
for i in range(3):
    def makefunc(i):
        def func(x):
            return x * i
        return func
    flist.append(makefunc(i))


def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print('Zero is not allowed')
                x = None
        except ValueError as err:
            print(err)
    return x


print('ax\N{SUPERSCRIPT TWO} + bx + c = 0')
a = get_float('enter a:', False)
b = get_float('enter b:', True)
c = get_float('enter c:', True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

print('root=', root)  # python 没有块级作用域
equation = ('{0}\N{SUPERSCRIPT TWO} + {1}x + {2} = 0' 
            '\N{RIGHTWARDS ARROW}x = {3}').format(a, b, c, x1)
if x2 is not None:
    equation += ' or x = {0}]'.format(x2)
print(equation)

