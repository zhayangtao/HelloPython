def tracer():
    calls = 0

    def onCall():
        nonlocal calls
        calls += 1
        print('call %s' % calls)
    return onCall


"""
使用描述符装饰方法
"""


class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        return wrapper(self, instance)


class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)


@Tracer
def spam(a, b, c):
    print(a + b + c)


class Person:
    @Tracer
    def giveRaise(self, percent):
        ...


# 代码简化
class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        return wrapper


"""
编写类装饰器
"""


instances = {}


def getInstance(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]


def singleton(aClass):
    def onCall(*args):
        return getInstance(aClass, *args)
    return onCall


@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


bob = Person('bob', 40, 10)
print(type(bob))


# 简化 singleton
def singleton(aClass):
    instance = None

    def onCall(*args):
        nonlocal instance
        if instance is None:
            instance = aClass(*args)
        return instance
    return onCall


#######################################
# 元类
#######################################


class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaClass):
    pass


L = MyList()
L.add(1)
print(L)


"""
元类使用示例
"""


class Field:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# metaclass
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__attrs__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(r'"Model" object has no attribute "%s"' % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (
            self._table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


"""
理解元类
"""


class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)


class Eggs:
    pass


print('making class')


class Spam(Eggs, metaclass=MetaOne):
    data = 1

    def meth(self, arg):
        pass


print('making instance')
x = Spam()
print('data:', x.data)


"""
定制构建和初始化
"""


class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init:', classname, supers, classdict, sep='\n...')
        return type.__init__(Class, classname, supers, classdict)


class Spam2(Eggs, metaclass=MetaTwo):
    data = 1

    def meth(self, arg):
        pass


print('_' * 20)
x = Spam2()
print('data:', x.data)


"""
使用简单的工厂函数
"""


def MetaFunc(classname, supers, classdict):
    print('In metaFunc: ', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)


print('_' * 20)


class Spam(Eggs, metaclass=MetaFunc):
    data = 1

    def meth(self, args):
        pass


x = Spam()
print('data:', x.data)


"""
用元类重载类创建调用
"""


class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)


class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta.init: ', classname, supers, classdict, sep='\n...')


class Spam(Eggs, metaclass=SubMeta):
    data = 1

    def meth(self, arg):
        pass


x = Spam()
print('data: ', x.data)
print('_' * 20)
