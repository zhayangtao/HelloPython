#函数装饰器
class Person:
    def giveRaise(self, percent):
        if percent < 0.0 or percent > 1.0:
            raise TypeError('Percent invalid')
        self.pay = int(self.pay * (1 + percent))


def rangetest(*argchecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator

print(__debug__)

@rangetest(1, 0, 120)
def persinfo(name, age):
    print('%s is %s years oid' % (name, age))

@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
def birthday(M, D, Y):
    print('birthday = {0}/{1}'.format(M, D, Y))


class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay

    @rangetest([1, 0.0, 1.0])
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

