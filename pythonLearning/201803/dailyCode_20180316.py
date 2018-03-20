from pathlib import Path

""" 
dataset = 'wiki_images'
datasets_root = Path('/path/to/datasets')

train_path = datasets_root / dataset / 'train'
test_root = datasets_root / dataset / 'test'

for image_path in train_path.iterdir():
    with image_path.open() as f:
        print("8888")
 """


def repeat_each_entry(data):
    """
    Each entry in the data is doubled
    """


"""
 对象析构函数：__del__
"""


class Life:
    def __init__(self, name='unknown'):
        print('Hello', name)
        self.name = name

    def __del__(self):
        print('Goodbye', self.name)


"""
类的设计
"""


class C:
    def meth(self, x):
        ...

    def meth(self, x, y, z):
        ...


class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary += (self.salary * percent)

    def work(self):
        print(self.name, "does stuff")

    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, "makes food")


class Server(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)

    def work(self):
        print(self.name, "interfaces with customer")


class PizzaRobot(Chef):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print(self.name, "makes pizza")


class Customer:
    def __init__(self, name):
        self.name = name
    
    def  order(self, server):
        print(self.name, "orders from", server)
    
    def pay(self, server):
        print(self.name, 'pays for item to', server)


class Oven:
    def bake(self):
        print("oven banes")


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('bob')
        self.oven = Oven()
    
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


def main():
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.2)
    print(bob)
    print()

    for clazz in Employee, Chef, Server, PizzaRobot:
        obj = clazz(clazz.__name__)
        obj.work()


if __name__ == '__main__':
    main()
