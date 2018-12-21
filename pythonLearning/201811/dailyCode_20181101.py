# 字典内涵
import os
import collections
import sys
import random

print('2' '2')
print('2', '2')
file_sizes = {name: os.path.getsize(name) for name in os.listdir(".") if os.path.isfile(name)}

# 默认字典
words = collections.defaultdict(int)
# 在默认字典中查找不存在的 key 时，会返回默认值，例如，words['dddd'] 返回 0
# 有序字典 collections.OrderedDict
d = collections.OrderedDict([('z', -4), ('e', 19)])
d['f'] = 'backup'
# 排序字典
d = collections.OrderedDict(sorted(d.items()))

"""
# 组合数据类型的迭代与复制
if len(sys.argv) < 3:
    sys.exit()
word = sys.argv[1]
for filename in sys.argv[2:]:
    for lino, line in enumerate(open(filename), start=1):
        if word in line:
            print(f'{filename}:{lino}:{line.rstrip()[:40]}')
"""


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "data/forenames.txt"), (surnames, "data/surnames.txt")):
        for name in open(filename, encoding='utf8'):
            names.append(name.rstrip())
    return forenames, surnames


# 可以导入 os 模块，并调用 pathsep.replace("/", os.sep) 来讲正斜杠替换为平台特定的目录分隔符
print(os.path.sep)
os.pathsep.replace("/", os.sep)

# zip() 函数以一个或者多个 iterables 为参数，病房一个迭代子，只要有某个 iterable 中的
# 元素用完，就终止这一过程
for t in zip(range(4), range(0, 10, 2), range(1, 10, 2)):
    print(t)

forenames, surnames = get_forenames_and_surnames()
limit = 100
years = list(range(1970, 2013)) * 3
print(years)
for year, forename, surname in zip(random.sample(years, limit), random.sample(forenames, limit),
                                   random.sample(surnames, limit)):
    name = f'{forename}{surname}'

x = sorted(forenames, key=str.lower)

x = list(zip((1, 2, 1, 3), {'pram', 'dorie', 'kayak', 'canoe'}))
x = sorted(x)


def swap(t):
    return t[1], t[0]


x = sorted(x, key=swap)

# 深拷贝
import copy
x = [63, 44, ['A', 'b', 'c']]
y = copy.deepcopy(x)

offset = 20 if sys.platform.startswith("win") else 10

try:
    1
finally:
    1
