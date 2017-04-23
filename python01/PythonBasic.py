a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print(True and True)
print(10 / 3)

classmates = ['Michael', 'Bod', 'Tracy']
print(len(classmates))
classmates.insert(1, 'Jack')

if a >= 3:
    print('adult')
elif a >= 5:
    print('child')
else:
    pass

for name in classmates:
    print(name)

# dict
d = {'Micheal': 98, 'Bob': 45}
print(d['Micheal'])
print(d.get('Thomas', -1))

# set
s = {1, 2, 3}
s.add(3)
s.remove(3)

# list
L = {1, 2, 3}


# 函数
def m_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('类型错误')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


# m_abs('a')


# 默认参数 必须只想不变对象
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

# 使用 *nums 将list所有参数传入
nums = [1, 2, 3]
calc(*nums)
# calc(nums)


# 关键字参数
def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)
person(name='Jovi', age=25)
person(name='Jovi', age=25, city='SH')
person(name='Jovi', age=25, gender='M', city='SH')
extra = {'city' : 'SH', 'job' : 'Engineer'}
person(name='Jovi',age=25, **extra)


def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'jopb' in kw:
        pass
    print('name', name, 'age', age, 'other', kw)
person('Jovi', 25, city='SH', addr='Zhangjiang')


# 命名关键字参数：限制关键字参数名字，* 号后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jovi', 25, city='SH', job='Engineer')


# 如果已存在可变参数，后面的命名关键字参数就不需要 *
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数可以设置默认值
def person(name, age, *, city='SH', job):
    print(name, age, city, job)
person('Jovi', 25, job = 'Engineer')


# 切片

