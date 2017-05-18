import sys
import time

timer = time.clock() if sys.platform[:3] == 'win' else time.time()


def total(reps, func, *args, **kwargs):
    """total time to run func() reps times"""
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, *args, **kwargs):
    """Quickset func() among reps runs"""
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)


def bestoftotal(reps1, reps2, func, *args, **kwargs):
    """Best of totals"""
    return bestof(reps1, total, reps2, func, *args, **kwargs)


class FileFaker:
    def write(self, string):
        pass


x = 'Killer rabbit'
if x == 'roger':
    print('shave and a haircut')
elif x == 'bugs':
    print("what's up doc?")
else:
    print('Run away! Run away!')

choice = 'ham'
print({'spam': 1.25,
       'ham': 1.99,
       'eggs': 0.99,
       'bacon': 1.10}[choice])

branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99,
          'bacon': 1.10}
print(branch.get('spam', 'bad choice'))
choice = 'bacon'
if choice in branch:
    print(branch[choice])
else:
    print('bad choice')

x = 1
if x:
    y = 2
    if y:
        print('block2')
    print('block1')
print('block0')

x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)

L = ['Good', "Bad", "Ugly"]
x = 1 + 2 + 3 \
    + 4
s = """
aaa
bbb
ccc"""
s = ('aaa'
     'bbb'
     'ccc')

while s:
    pass
else:
    pass

x = 'spam'
while x:
    print(x, end='')
    x = x[1]
x = 10
while x:
    x = x - 1
    if x % 2 != 0:
        continue
    print(x, end='')

x = 1 // 2
while x > 1:
    if 2 % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')

x = True
while x:
    x = next(object)
    if x:
        x = False

prod = 1
for item in [1, 2, 3, 4]:
    prod *= item

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])

items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]
for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found")

for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key, "not found!")
[x for x in items if x in tests]

