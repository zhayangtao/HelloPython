"""
理解装饰器
装饰器的返回值也是一个函数对象，用于为已经存在的对象添加额外的功能。
"""

import logging


def use_logging(func):
    def wrapped(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapped


def bar():
    print('i am bar')


bar = use_logging(bar)
bar()


# @符号是装饰器的语法糖
@use_logging
def foo():
    print('i am foo')


foo()


"""
带参数的装饰器
"""


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                logging.warn("%s is running" % func.__name__)
            return func(*args)
        return wrapper
    return decorator


"""
类装饰器
使用类装饰器还可以依靠类内部的 __call__ 方法，当使用 @ 符号形式将装饰器附加到
函数上时，就会调用此方法。
"""


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator running')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()


"""
使用 functools.wraps 保留原始信息
"""

from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + ' was called')
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
    return x + x * x


"""
函数装饰器在函数定义的时候进行名称重绑定，提供一个逻辑层来管理函数和方法或随后对他们的调用；
类装饰器在类定义的时候进行名称重绑定，提供一个逻辑层来管理类
"""


# 拦截类实例未定义的属性
def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Wrapper


@decorator
class C:
    def __init__(self, x, y):
        self.attr = 'spam'


x = C(6, 7)
print(x.attr)


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))


@tracer
def spam(a, b, c):  # spam 实际上是 tracer 的一个实例
    print(a + b + c)


""""
状态信息保持选项
"""

# 1、类实例属性


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(x, y):
    print(x ** y)


print('_' * 20)
spam(1, 2, 3)
spam(a=4, b=5, c=6)

eggs(2, 16)
eggs(4, y=4)
