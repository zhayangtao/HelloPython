'''
日常代码
'''
import sys


def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])


def mysum2(L):
    if not L:
        return 0
    else:
        def nonempty(L2):
            return L2[0] + mysum2(L2[1:])
        return nonempty(L)


sum = 0
for x in (1, 2, 3, 4):
    sum += x


def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


def echo1(message):
    print(message)


schedule = [(echo1, 'Spam!'), (echo1, 'ham!')]
for (func, arg) in schedule:
    func(arg)

print(echo1.__name__)
print(dir(echo1))


# 函数注解
def func(a, b, c):
    return a + b + c


def func2(a: 'spam', b: (1, 10), c: float)-> int:
    return a + b + c


print(func2.__annotations__)

# lambda 函数
def f(x, y, z): return x + y + z


print(f(1, 2, 4))

# 默认参数也可以在 lambda 中使用
x = (lambda a='fee', b='fie', c='foe': a + b + c)
print(x('wee'))


L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(2))


lower = (lambda x, y: x if x < y else y)
showall = lambda x: list(map(sys.stdout.write, x))


def action(x):
    return lambda y: x + y
print(action(99))
print(action(99)(2))

# map
def inc(x): return x + 10
counters = [1, 2, 3, 4]
list(map(inc, counters))

def main():
    print(mysum2([1, 2, 3, 4, 5]))
    print(mysum2((1, 2, 3, 4, 5)))
    L = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(sumtree(L))


if __name__ == '__main__':
    main()
