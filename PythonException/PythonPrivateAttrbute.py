"""
Privacy for attributes fetched from class instances.
see self-test code at end of file for a usage example.
Decorator same as
"""
traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


def Private(*privates):
    def onDecorator(aClass):
        class onInstances:
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)

            def __getattr__(self, item):
                trace('get:', item)
                if item in privates:
                    raise TypeError('private attribute fetch: ' + item)
                else:
                    return getattr(self.wrapped, item)

            def __setattr__(self, key, value):
                trace('set:', key, value)
                if key == 'wrapped':
                    self.__dict__[key] = value
                elif key in privates:
                    raise TypeError('private attribute change: ' + key)
                else:
                    setattr(self.wrapped, key, value)

        return onInstances

    return onDecorator

"""
if __name__ == '__main__':
    traceMe = True


    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print('%s => %s' % (self.label, self.data))


    x = Doubler('X is', [1, 2, 3])
    y = Doubler('Y is', [-10, -20, -30])

    # The following all succeed
    print(x.label)
    x.display();
    x.double();
    x.display()
    # print(x.size())
    # print(x.data)

"""
# 访问控制
def accessControl(failIf):
    def onDecorator(aClass):
        class OnInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)

            def __getattr__(self, item):
                trace('get:', item)
                if failIf(item):
                    raise TypeError('private attribute fetch: ' + item)
                else:
                    return getattr(self.__wrapped, item)
            def __setattr__(self, key, value):
                trace('set:', key, value)
                if key == '_OnInstance__wrapped':
                    self.__dict__[key] = value
                elif failIf(key):
                    raise TypeError('private attribute change:' + key)
                else:
                    setattr(self.__wrapped, key, value)

        return OnInstance
    return onDecorator


def private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))


def public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))

if __name__ == '__main__':
    @private('age')
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    x = Person('Bob', 40)
    x.name

