"""
常用内建模块
"""


from datetime import datetime

now = datetime.now()  # 获取当前 datetime
print(now)
dt = datetime(2018, 4, 21, 23, 3)
print(dt)

# datetime 转换为 timestamp
t = 1429417200.0
print(datetime.fromtimestamp(t))
# str 转换为 datetime
cday = datetime.strptime('2018-4-21 23:07:44', '%Y-%m-%d %H:%M:%S')
print(cday)
# datetime 转换为 str
print(now.strftime('%a, %b %d %H:%M'))

# datetime 运算
from datetime import timedelta

print(now + timedelta(days=1))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))


# collections
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

Circle = namedtuple('Circle', ['x', 'y', 'z'])

# deque ：用于搞笑实现插入和删除操作的双向列表
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict：当 key 不存在时，返回一个默认值
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key'] = 'abc'
print(dd['key'])
print(dd['key2'])

# OrderedDict：有序 dict
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

# 用 OrdereDict 实现一个 FIFO 的 dict


class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# Counter：统计字符个数
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] += 1
print(c)


# hashlib
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 将数据分多块计算
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
