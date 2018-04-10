def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kargs):
            self.fetched = 0
            self.wrapped = aClass(*args, **kargs)

        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            self.fetched += 1
            return getattr(self.wrapped, attrname)
    return Wrapper


@Tracer
class Spam:
    def display(self):
        print('spam' * 8)


@Tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


food = Spam()
food.display()
print([food.fetched])
food = Spam()
food.display()
print([food.fetched])

print('_' * 20)
bob = Person('Bob', 40, 50)
print(bob.name)
print(bob.pay())

print('')
sue = Person('Sue', rate=100, hours=60)
print(sue.name)
print(sue.pay())

print(bob.name)
print(bob.pay())
print([bob.fetched, sue.fetched])


"""
类错误之二：保持多个实例
"""


class Tracer:
    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args):
        self.wrapped = self.aClass(*args)
        return self

    def __getattr__(self, attrname):
        print('Trace:' + attrname)
        return getattr(self.wrapped, attrname)


@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)


print('_' * 20)
food = Spam()
food.display()


"""
直接管理函数和类
"""


registry = {}


def register(obj):
    registry[obj.__name__] = obj
    return obj


@register
def spam(x):
    return (x ** 2)


@register
def ham(x):
    return (x ** 3)


@register
class Eggs:
    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)


print('_' * 20)
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))
print(ham(2))
x = Eggs(2)
print(x)

print('\nRegistry calls:')
for name in registry:
    print(name, '=>', registry[name](3))


def decorate(func):
    func.marked = True
    return func


@decorate
def spam(a, b):
    return a + b


print('_' * 20)
print(spam.marked)


def annotate(text):
    def decorate(func):
        func.label = text
        return func
    return decorate


@annotate('spam data')
def spam(a, b):
    return a + b


print('_' * 20)
print(spam(1, 2), spam.label)
