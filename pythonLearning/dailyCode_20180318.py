"""
用 __dict__ 列出实例属性
"""


class ListInstance:
    """
    Mix-in class that des a formatted print() or str() of
    instances via inheritance of __str__, coded here; displays
    instance attrs only
    """

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            id(self),  # 使用内置方法 id() 获取对象内存地址
            self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result


class Spam(ListInstance):
    def __init__(self):
        self.data = 'food'


x = Spam()
# print(x)


class Super:
    def __init__(self):
        self.data1 = 'spam'

    def ham(self):
        pass


class Sub(Super, ListInstance):
    def __init__(self):
        super().__init__()
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass


"""
使用 dir 列出继承的属性
"""


class A:
    def __init__(self):
        self.a = 1


class B(A, ListInstance):
    def __init__(self):
        self.b = 2


class ListInherited:
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr.startswith('__') and attr.endswith('__'):
                result += '\tname %s=<>\n' % attr
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result


"""
main
"""


def main():
    # x = Sub()
    # print(x)

    b = B()
    print(b)

    class Sub(Super, ListInherited):
        pass
    
    sub = Sub()
    print(sub)


if __name__ == '__main__':
    main()
