x = set('spam')
print(x)
x = set('spam')
print(x)
x = {'spam'}
print(x)

import decimal

temp = decimal.getcontext().prec = 2
decimal.getcontext().prec = temp


import math

math.sqrt(144)


import random

random.random()
random.choice(['life of brian', 'holy shit', 'meaning of life'])

print(0.1 + 0.1 + 0.1 - 0.3)  # 缺失精度

from decimal import Decimal
a = Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)
print(a)  # 缺失精度
b = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(b)

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))


if True:
    def func():
        pass
else:
    def func():
        pass
