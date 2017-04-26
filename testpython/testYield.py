def h():
    print('Wen Chuan')
    m = yield 5
    print(m)
    d = yield 12
    print('We are one')
c = h()
next(c)
c.send('Fight')
# next(c)

def h1():
    print('Wen Cha')
    m = yield 5
    print(m)
    d = yield 12
    print('We are together')
c = h1()
m = next(c)
d = c.send('Fighting')
print('We will never forger the date', m, '.', d)
