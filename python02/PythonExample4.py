def factory(aClass, *args, **kwargs):
    return aClass(*args, **kwargs)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job


object1 = factory(Spam)
object2 = factory(Person, "Guido", "guru")


class MyList(list):
    def __getitem__(self, item):
        print('indexing %s at %s)' % (self, item))
        return list.__getitem__(self, item - 1)


class Set(list):
    def __init__(self, value=[]):
        list.__init__([])
        self.concat(value)

    @staticmethod
    def intersect(other):
        res = []
        for x in other:
            res.append(x)
        return Set(res)

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)

