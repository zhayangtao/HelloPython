class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances():
        print("Number of instances created: ", Spam.numInstances)

    #静态方法
    printNumInstances = staticmethod(printNumInstances)


# 静态方法不需要实例，类方法需要一个类参数
class Methods:
    def imeth(self, x):
        print(self, x)

    def smeth(x):
        print(x)

    def cmeth(cls, x):
        print(cls, x)


class Sub(Spam):
    def printNumInstances():
        print("Extra stuff...")
        Spam.printNumInstances()

    printNumInstances = staticmethod(printNumInstances)


# 类可以继承静态方法
class Other(Spam): pass


c = Other()
c.printNumInstances()


class Spam1:
    numInstances = 0
    def __init__(self):
        Spam1.numInstances += 1

    def printNumInstances(cls):
        print("Number of instances:", cls.numInstances)
    #类方法
    printNumInstances = classmethod(printNumInstances)

