list(zip(['a', 'b', 'c'], [1, 2, 3]))
# 字典解析表达式
d = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(d)
d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
dict.fromkeys(['a', 'b', 'c'], 0)
if 'a' in d:
    print(True)
t = tuple('spam')

def foo(t: tuple):
    pass
with open('/rrrrr.txt', 'w') as f:
    print(f)