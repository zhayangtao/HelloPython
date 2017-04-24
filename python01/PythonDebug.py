# 断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
def main():
    foo('0')
main()

import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
