"""
类特性
"""


class classic:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError


x = classic()
print(x.age)


class newprops(object):
    def getage(self):
        return 40

    def setage(self, value):
        print('set age', value)
        self._age = value

    age = property(getage, setage, None, None)


x = newprops()
print(x.age)
x.age = 42
x.job = 'trainer'
print(x.job)


"""
静态方法和类方法只对经典类有效
类中的无实例方法不能通过实例调用
"""


class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances():
        print("Number of instances created: ", Spam.numInstances)


"""
静态方法替代方案
"""


def printNumInstances():
    print("Number of instances created: ", Spam2.numInstances)


class Spam2:
    numInstances = 0

    def __init__(self):
        Spam2.numInstances += 1


print('*' * 10)
a = Spam2()
b = Spam2()
c = Spam2()
printNumInstances()


class Spam3:
    numInstances = 0

    def __init__(self):
        Spam3.numInstances += 1

    def printNumInstances(self):
        print("Number of instances created: ", Spam3.numInstances)


a = Spam3()


"""
使用静态和类方法
"""


class Methods:
    def imeth(self, x):
        print(self, x)

    def smeth(x):
        print(x)

    def cmeth(cls, x):
        print(cls, x)

    smeth = staticmethod(smeth)  # 静态方法，允许通过一个实例调用
    # 类方法，python 自动把类传入类方法第一个参数中，
    # 不管是通过一个类或者一个实例调用
    cmeth = classmethod(cmeth)


print()
print('*' * 10)
obj = Methods()
obj.imeth(1)
Methods.imeth(obj, 2)
Methods.smeth(5)
obj.cmeth(6)
obj.smeth(7)


"""
使用静态方法统计实例
"""


class Spam4:
    numInstances = 0

    def __init__(self):
        Spam4.numInstances += 1

    def printNumInstances():
        print("Number of instances: ", Spam4.numInstances)
    printNumInstances = staticmethod(printNumInstances)


class Sub(Spam4):
    def printNumInstances():
        print("Extra stuff...")
        Spam4.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)


print()
print('*' * 10)
a = Sub()
b = Sub()
a.printNumInstances()
b.printNumInstances()
