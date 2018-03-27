"""
描述符
"""


class Descriptor:
    "docstring goes here"

    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')

    def __set__(self, instance, value): ...

    def __delete__(self, instance): ...


class Subject:
    attr = Descriptor()


x = Subject()
x.attr

Subject.attr


"""
只读描述符
"""


class D:
    def __get__(*args):
        print('get')

    def __set__(*args):
        raise AttributeError('cannot set')


class C:
    a = D()


print()
print()
print()
x = C()
x.a
C.a
# x.a = 99
print(x.a)


class Name:
    "name descriptor docs"

    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    def __delete(self, instance):
        print('remove...')
        del instance._name


class Person:
    def __init__(self, name):
        self._name = name

    name = Name()


print()
print()
print()
print()
bob = Person('Bob smith')
print(bob.name)


class Super:
    def __init__(self, name):
        self._name = name

    name = Name()


class Person(Super):
    pass


"""
嵌套描述符
"""


class Person:
    def __init__(self, name):
        self._name = name

    class Name:
        "name descriptor docs"

        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name

        def __set__(self, instance, value):
            print('change...')
            instance._name = value

        def __delete__(self, instance):
            print('remove...')
            del instance._name
    name = Name()
