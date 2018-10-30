def tupleTest():
    return ()


if __name__ == '__main__':
    t = tupleTest()
    print(type(t))

    tu = tuple((1,2))
    tu *= 3
    print(tu)

# 命名元组
import collections

sale = collections.namedtuple('sale', 'productid customerid date quantity price')
sales = []
sales.append(sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(sale(419, 974, "2008-09-15", 1, 18.49))
print(sales[0][-1])

Aircraft = collections.namedtuple('Aircraft', 'manufacturer model seating')
Seating = collections.namedtuple('Seating', 'minimum maximum')
aircraft = Aircraft('Airbus', 'A320-200', seating=Seating(100, 220))
print(aircraft.seating.maximum)
format_str = '{0.manufacturer}{0.model}'.format(aircraft)
print(format_str)