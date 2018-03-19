x = (x for x in 'abcdg')
print('-----'.join(x))


class Iter():
    def __next__(self):
        print('next')
        return self


from dailyCode_20180318_listTree import ListTree
from tkinter import Button


class MyButton(ListTree, Button):
    pass


B = MyButton(text='spam')


"""
类是对象：通用对象的工厂
"""


def factory(aClass, *args, **kargs):
    return aClass(*args, **kargs)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job


object1 = factory(Spam)
object2 = factory(Person, "Guido", "guru")


class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if x not in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + repr(self.data)


x = Set([1, 3, 4, 5])
print(x.union(Set([1, 4])))
print(x | Set([1, 4, 6]))

"""
通过子类扩展定义
"""

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)


def main():
    print(list('abc'))
    x = MyList('abc')
    print(x)

    print(x[1])
    print(x[3])

    x.append('spam')
    print(x)
    x.reverse()
    print(x)

if __name__ == '__main__':
    main()