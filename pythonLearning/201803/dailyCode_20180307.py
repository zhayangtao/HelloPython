#######################################
# 高级模块话题
########################################
_all_ = ['Error', 'encode', 'decode']


def tester():
    print("It's Christmas in Heaven")


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y):
    return x < y


def grtthan(x, y):
    return x > y


"""
Various specialized string display formatting utilities.
"""


def commas(N):
    """
    format positive integer-like N for display with commas
    between digit groupings: xxx, yyy, zzz
    """
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, lasts = digits[:-3], digits[-3:]
        result = (lasts + ',' + result) if result else lasts
    return result


def money(N, width=0):
    """
    format number N for display with commas, 2 decimal digits,
    leading $ and sign, and optional paddings: $ -xxx,yyy.zz
    """
    sign = '-' if N < 0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = ('%.2f' % N)[-2:]
    format = '%s%s.%s' % (sign, whole, fract)
    return '$%*s' % (width, format)


def main():
    tester()
    print(minmax(lessthan, 4, 2, 5, 7))
    print(minmax(grtthan, 4, 6, 3))
    print('I am: %s' % __name__)


"""
lists the namespaces of other modules
"""


seplen = 60
sepchr = '-'


def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name', module.__name__, 'file:', module.__file__)
        print(sepline)

    count = 0
    for attr in module.__dict__:
        print('%02d) %s' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)


if __name__ == '__main__':
    main()

    def selftest():
        tests = 0, 1
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))

        print('')
        tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))

    import sys
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))
