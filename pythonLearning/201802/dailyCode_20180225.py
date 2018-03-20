def func1(name): pass


def func2(name='value'): pass


def func3(*name): pass


def func4(**name): pass


def func5(*args, name): pass


def func6(*, name='value'): pass


func6(name='3')
func6()
print(func5(1, 2, name=2))


def kwonly(a, *, b, c):
    print(a, b, c)
