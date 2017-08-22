class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while 1:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'Converter must be defined'


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == "__main__":
    import sys

    obj = Uppercase(open('../python01/siniin-ok.html', encoding='utf8'), sys.stdout)
    obj.process()


class HTMLize:
    def write(self, line):
        print('<PRE> %s</PRE>' % line.rstrip())


class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        print('Trace:', item)
        return getattr(self.wrapped, item)


class C1:
    def meth1(self):
        self.__x = 88


# 无绑定方法
class Spam:
    def doit(self, message):
        print(message)


object1 = Spam()
x = object1.doit
x('hello')

object2 = Spam()
t = Spam.doit
t(object2, 'hello')


class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


for act in Number(2).double, Number(3).double, Number(4).double:
    print(act())


def square(arg):
    return arg ** 2


class Sum:
    def __init__(self, val):
        self.val = val

    def __call__(self, *args, **kwargs):
        return self.val + args


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


class Spam:
    def __init__(self):
        self.data1 = "food"


class ListInherited:
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\tname %s=<>\n' % attr
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result
