"Assorted class utilities and tools"
class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append("%s=%s" % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


class TopTest(AttrDisplay):
    ...

    def gatherAttrs(self):
        return 'Spam'


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

    __repr__ = __str__



class Manager(Person):
    def __init__(self, name, pay=0):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

    # def __getattr__(self, item):
    #     return getattr(self.person, item)

    def __str__(self):
        return str(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)
