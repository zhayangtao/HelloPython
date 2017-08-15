x = 11


def f():
    print(x)


def g():
    x = 22
    print(x)


class C:
    x = 33

    def m(self):
        x = 44
        self.x = 55


if __name__ == '__main__':
    print(x)
    f()
    g()
    print(x)

    obj = C()
    print(obj.x)

    obj.m()
    print(obj.x)
    print(C.x)

    # print(C.m.x)
    # print(g.x)

x = 11


def g1():
    print(x)


def g2():
    global x
    x = 22


def h1():
    x = 33

    def nested():
        print(x)


def h2():
    x = 33

    def nested():
        nonlocal x
        x = 44


def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)


def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)


def selftest():
    class A: pass

    class B(A): pass

    class C(A): pass

    class D(B, C): pass
