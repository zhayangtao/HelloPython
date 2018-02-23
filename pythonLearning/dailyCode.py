# 日常训练代码
line = 'aaa bbb ccc'
print(line)
print(line.split())
d = {'food': 'Spam', 'quantity': '4', 'color': 'pink'}
print(d['food'])
print(list(d.keys()))
for key in d:
    print(key, '=>', d[key])
for key in sorted(d):
    print(key, '=>', d[key])
