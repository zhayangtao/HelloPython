from functools import reduce


def normalize(aL):
    def touppercase(L):
        return L[0].upper() + L[1:].lower()
    return map(touppercase, aL)

L = ['adam', 'LISA', 'barT']
print(list(normalize(L)))


def prod(L):
    def star(x, y):
        return x * y
    return reduce(star, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2Num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    dot = s.index('.')
    s = s[:dot] + s[dot+1:]
    result = reduce(fn, map(char2Num, s))
    result /= 10 ** (len(s) - dot)
    return result


# filter
print(10 ** 5)