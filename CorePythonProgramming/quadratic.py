# _*_coding:utf8_*_
import cmath
import math
import sys
import collections


def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print('zero is not allowed')
                x = None
        except ValueError as err:
            print(err)
    return x


Sale = collections.namedtuple("Sale", "productid customerid date quantity price")

sales = []
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2008-09-15", 1, 7.99))

d1 = dict({"id": 1946, "name": "washer", "size": 4})
d2 = dict(id=1946, name="washer", size=3)
d3 = dict([("id", 1948)])


names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']


d = {}
for name in names:
    key = len(name)
    d[key].append(name)

