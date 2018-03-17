"""
重访流处理器
"""


def processor(reader, converter, writer):
    while True:
        data = reader.read()
        if not data:
            break
        data = converter(data)
        writer.write(data)


class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'converter must be defined'


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


def main():
    import sys
    obj = Uppercase(
        open('E:\workspaceForPyCharm'
             '\HelloPython\pythonLearning'
             '\dailyCode_20180316.py', encoding='utf8'),
        sys.stdout)
    obj.process()


if __name__ == '__main__':
    # main()
    pass


"""
为私有属性
"""


class C1:
    def meth1(self):
        self.__x = 88

    def meth2(self):
        print(self.__x)


class C2:
    def meth1(self):
        self.__x = 99

    def meth2(self):
        print(self.__x)


class C3(C1, C2):
    pass


I = C3()
print(I.meth1(), I.meth2())
print(I.__dict__)


"""
方法是对象：绑定或者无绑定
"""


class Spam:
    def doit(self, message):
        print(message)


object1 = Spam()
object1.doit('hello world')

object2 = Spam()
x = object2.doit
x('hello world')

object3 = Spam()
t = Spam.doit  # 无绑定方法
t(object3, 'hello world')


class Selfless:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def selfless(arg1, arg2):
        return arg1 + arg2

    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2


x = Selfless(2)
print(x.normal(3, 4))
Selfless.normal(x, 3, 4)
Selfless.selfless(3, 4)


def square(arg) -> int:
    return arg ** 3


class Sum:
    def __init__(self, val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]
for act in actions:
    print(act(5))


class Negate:
    def __init__(self, val):
        self.val = -val

    def __repr__(self):
        return str(self.val)

    # def __repr__():
    #     print(' no self repr')
