# 日常训练代码
line = 'aaa bbb ccc'
print(line)
print(line.split())
d = {'food': 'Spam', 'quantity': '4', 'color': 'pink'}
print(d['food'])
print(list(d.keys()))
list(d.keys()).sort()

line = "i'm SPAMaSPAMlumberjack"
print(line.split("SPAM"))
'That is %d %s bird!' % (1, 'dead')
'{0:d}'.format(5555555)

type([])
list(map(abs, [-1, -2, 0, 1, 2]))
L = ['abc', 'ABD', 'aBe']
sorted(L, key=str.lower, reverse=True)
sorted([x.lower() for x in L], reverse=True)
L.extend([1, 2, 3])
# L.sort() not supported between instances of 'int' and 'str'
