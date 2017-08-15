from PythonExample import Person, Manager

bob = Person('bob')
sue = Person('Sue', job='dev', pay=100)
tom = Manager('Tom', 5000)

import shelve

db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()

from importlib import reload

import glob

glob.glob('person*')
print(open('persondb.dir').read())
print(open('persondb.dir', 'rb').read())

db = shelve.open('persondb')
print(len(db))

print(list(db.keys()))
bob = db['bob']
print(bob)

for key in sorted(db):
    print(key, '\t=>', db[key])
sue = db['Sue']
sue.giveRaise(.10)
db['Sue'] = sue
db.close()


class MixedNames:
    data = 'spam'

    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)


x = MixedNames(1)
MixedNames.display(x)


class Super:
    def __init__(self, x):
        ...

    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()

    def action(self):
        assert False, 'action must be defined!'


class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)
        ...

    def method(self):
        print('starting Sub.method')
        Super.method(self)
        print('ending Sub.method')


I = Sub(1, 2)

from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.method()

    @abstractmethod
    def method(self):
        pass


class Sub(Super):
    def method(self):
        pass
