class CardHolder:
    acctlen = 8
    ratireage = 59

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattr__(self, item):
        if item == 'acct':
            return self._acct[:-3] + '***'
        elif item == 'remain':
            return self.retireage - self.age
        else:
            raise AttributeError(item)

    def __setattr__(self, key, value):
        if key == 'name':
            value = value.lower().replace(' ', '_')
        elif key == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif key == 'acct':
            key = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif key == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[key] = value

if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    bob.acct

#函数装饰器
def decorator(F):
    def wrapper(*args):

        return wrapper

@decorator
def func(): ...

#类装饰器
class decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        ...

@decorator
def func(x, y):
    ...

