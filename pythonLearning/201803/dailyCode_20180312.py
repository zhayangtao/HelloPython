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


class super:
    def hello(self):
        self.data1 = 'spam'


class sub(super):
    def hola(self):
        self.data2 = 'eggs'


def main():
    print(x)
    f()
    g()
    print(x)
    obj = C()
    print(obj.x)
    obj.m()
    print(obj.x)
    print(C.x)

    print('*' * 8)
    s = sub()
    s.__dict__
    s.__class__
    print(sub.__bases__)
    print(sub.__base__)
    super.__bases__

    y = sub()
    s.hello()
    print(s.__dict__)
    s.hola()
    print(s.__dict__)
    print(list(sub.__dict__.keys()))
    print(list(super.__dict__.keys()))


"""
classtree
"""
import types


def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent+3)


def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)


def selftest():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, A):
        pass

    class E:
        pass

    class F(D, E):
        pass
    instancetree(B())
    instancetree(F())


if __name__ == '__main__':
    # main()
    selftest()
