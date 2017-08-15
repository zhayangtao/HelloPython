class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, item):
        print('getitem:', item)
        return self.data[item]

    def __setitem__(self, index, value):
        self.data[index] = value


class Stepper:
    def __getitem__(self, item):
        return self.data[item]


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        print('call __iter__')
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


'''
for i in Squares(1, 5):
    print(i, end=' ')
'''


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return StopIteration(self.wrapped)


'''
if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next((I), next(I), next(I)))

    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
'''


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        print('get[%s]:' % item, end='')
        return self.data[item]

    def __iter__(self):
        print('iter=>', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, item):
        print('contains: ', end='')
        return item in self.data


x = Iters([1, 2, 3, 4, 5])
print(3 in x)
for i in x:
    print(i, end=' | ')

print()
print([i ** 2 for i in x])
print(list(map(bin, x)))
I = iter(x)
while True:
    try:
        print(next(I), end='@')
    except StopIteration:
        break


class Empty:
    def __getattr__(self, item):
        if item == 'age':
            return 40
        else:
            raise AttributeError


x = Empty()
print(x.age)


class AccessControl:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError


class PrivateExc(Exception):
    pass


class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


class Adder:
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        self.data += other

    def __repr__(self):
        return 'Adder(%s)' % self.data


class Printer:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Commuter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print('add', self.value, other)
        return self.value + other

    def __radd__(self, other):
        print('radd', self.value, other)
        return other + self.value


class Commuter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Commuter):
            other = other.value
        return Commuter(self.value + other)


class Number:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self


class Callee:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)

    def __init__(self):
        print('init')


class C:
    data = 'spam'

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other


class Life:
    def __init__(self, name='unknown'):
        print('Hello', name)
        self.name = name

    def __del__(self):
        print('Goodbye', self.name)


class C:
    def meth(self, *args):
        if len(args) == 1:
            ...
        elif type(args[0]) == int:
            ...

