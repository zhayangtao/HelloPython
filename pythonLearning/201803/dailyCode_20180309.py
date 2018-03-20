"""
class
"""


class C1:
    def __init__(self, who):
        self.name = who


class Employee:
    def computeSalary(self):
        pass

    def giveRaise(self):
        pass

    def promote(self):
        pass

    # 实例方法
    def retire(self):
        pass

    # 类方法
    def nonself():
        print('self')


e = Employee()
Employee.nonself()


def processor(reader, converter, writer):
    while 1:
        data = reader.read()
        if not data:
            break
    data = converter(data)
    writer.write(data)


class Reader:
    def read(self):
        pass

    def other(self):
        pass


class FileReader(Reader):
    def read(self):
        ...


class SocketReader(Reader):
    def read(self): ...


# processor(FileReader(...), None, None)


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()
z = FirstClass
z.a = 1
print(x.a)
x.setdata("king Arthur")
y.setdata(3.15)


class SecondClass(FirstClass):
    def display(self):
        print('Current value')


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    
    def __add__(self, other):
        return ThirdClass(self.data + other)
    
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    
    def mul(self, other):
        self.data *= other

a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()
print(b)
