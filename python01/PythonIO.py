# 读文件
f = open('E:\车险文档\旧车测试数据.txt', 'r')
print(f.read())
f.close()

try:
    f = open('E:\车险文档\旧车测试数据.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('E:\车险文档\旧车测试数据.txt', 'r') as f:
    print(f.read())


# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲
# with open('F:\图片\093234.jpg', 'rb') as f:
#     print(f.read())

with open('E:\车险文档\旧车测试数据.txt', 'r', encoding='utf8') as f:
    print(f.read())

with open('E:\车险文档\旧车测试数据.txt', 'r', encoding='utf8', errors='ignore') as f:
    print(f.read())


# 写文件
with open('E:\车险文档\旧车测试数据.txt', 'w') as f:
    f.write('Hello, world')


# StringIO 与 ByteIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))


# 操作文件和目录
import os
print(os.name)
# print(os.uname()) # uname()函数在Windows上不提供
print(os.environ)
print(os.environ.get('PATH'))


# 序列化
# Python提供了pickle模块来实现序列化
import pickle
d = dict(name='BOb', age=20, score=99)
# pickle.dump(d)

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)
# 反序列号
with open('dump.txt', 'rb') as f:
    pickle.load(f)


# JSON
import json
d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)
print(json_str)
print(json.loads(json_str))


# json 进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)
# print(json.dumps(s))  # TypeError: Object of type 'Student' is not JSON serializable
# 需要定义 下面方法让python知道如何将 student 实例转换为一个json对象
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
print(json.dumps(s, default=student2dict))

# 把任意class的实例变为 dict
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(json_str, object_hook=dict2student))
