def insersect(*args):
    res = []
    for x in args[0]:
        for other in args[1]:
            if x not in other:
                break
            else:
                res.append(x)


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)


import sys


def print30(*args, **kargs):
    '''
    自定义 print 函数
    '''
    sep = kargs.get('sep', ' ')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print30(1)
print30()
