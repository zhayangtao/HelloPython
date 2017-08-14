class C3: ...


class C2: ...


class C1(C2, C3):
    def setname(self, who):
        self.name = who


I1 = C1()
T2 = C1()
I1.setname('bob')


class Employee:
    def computeSalary(self): ...

    def giveRaise(self): ...

    def promote(self): ...

    def retire(self): ...


class Engineer(Employee):
    def computeSalary(self): ...


def proccssor(reader, converter, writer):
    while 1:
        data = reader.read()
        if not data: break
    data = converter(data)
    writer.write(data)


class FirstClass:
    def setData(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Currnt value = "%s"' % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass:%s]' % self.data

    def mul(self, other):
        self.data *= other


class Person1:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def info(self):
        return (self.name, self.job)
