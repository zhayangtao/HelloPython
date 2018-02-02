import pickle

x, y, z = 43, 44, 45
d = {'a': 1, 'b': 2}
f = open('datafile.pkl', 'wb')
pickle.dump(d, f)
f.close()

f = open('datafile.pkl', 'rb')
e = pickle.load(f)
print(e)

with open('datafile.pkl', mode='rb') as file:
    for line in file:
        print(line)

f = {1, 2, 3}


# 深度复制
import copy
import types

copy.deepcopy(f)
# def f(): pass
# type(f) == types.FunctionType

# while True:
#     reply = input('Enter a num:')
#     if reply == 'stop':
#         break
#     if reply.isdigit():
#         pass
#     else:
#         print('invalid value')
#     print(int(reply) ** 2)

while True:
    reply = input('Enter a num:')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('bad')
    else:
        print(int(reply) ** 2)
print('Bye')