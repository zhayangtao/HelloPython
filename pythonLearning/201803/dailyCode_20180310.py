class Rec:
    ...


print(Rec.__dict__.keys())


def upperName(self):
    return self.name.upper()


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def info(self):
        return (self.name, self.job)

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

    __repr__ = __str__


class Manager(Person):
    def __init__(self, name, pay):
        super.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=10):
        ...

    # 定制类
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    
    def __str__(self):
        return str(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)
    
    def addMember(self, person):
        self.members.append(person)
    
    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    
    def showAll(self):
        for person in self.members:
            print(person)

