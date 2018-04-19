class Dict(dict):
    """
    simple dict but also support access as x.y style
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    """

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest
    doctest.testmod()


"""
StringIO
"""


from io import StringIO


f = StringIO()
f.write('hello')
f.write(' ')
f.write(' world!')
print(f.getvalue())


"""
操作文件和目录
"""


import os
print(os.name)
print(os.environ)
print(os.path.abspath('.'))

[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('.') if os.path.isfile(
    x) and os.path.splitext(x)[1] == '.py']


"""
序列化
"""


import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)  # picker.dumps() 把任意对象序列化成一个 bytes
f = open('dump.txt', 'wb')
pickle.dump(d, f)  # picker.dump() 把对象序列化后写入一个 file-like Object
f.close()
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)


"""
JSON
"""

import json

d = dict(name='Bob', age=20, score=88)
print()
print('_' * 20)
print(json.dumps(d))  # 返回一个 str
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))


"""
json 进阶
"""


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# json 转换函数


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)
# print(json.dumps(s))  # TypeError: Object of type 'Student' is not JSON serializable
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
