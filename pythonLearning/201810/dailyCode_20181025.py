# s = input('enter an integer:')
# try:
#     # i = int(s)
#     print('valid integer entered:', i)
# except ValueError as err:
#     print(err)


# python 列表可变
seeds = ['sesame', 'sunflower']
seeds += ['pumpkin']
print(seeds)

seeds.append(['111'])
print(seeds)

seeds.append('111')
print(seeds)

import random


def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print('must be >=', minimum)
            else:
                return i
        except ValueError as err:
            print(err)


rows = get_int('rows:', 1, None)
"""
columns = get_int('columns:', 1, None)
minimum = get_int('minimum (or enter for 0):', -1000000, 0)
default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int('maximum (or enter for' + str(default) + '):', minimum, default)

row = 0
while row < rows:
    line = ''
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:
            s += " "
        line += s
        column += 1
    print(line)
    row += 1

"""


def generate_grid():
    pass


import decimal
import math

print(decimal.Decimal(value="555"))
decimal.Decimal(value="555")
print(round(4.51))
print(round(4.6))
print(math.ceil(4.5))
decimal.Decimal(111)

s = 'he ate camel food'
print(s[::-2])


