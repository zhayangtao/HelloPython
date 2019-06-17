from random import randint


def roll_dice(n=2):
    """
    摇色子
    :param n:
    :return:
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


'''
练习1：实现计算求最大公约数和最小公倍数的函数
'''


def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)


'''
练习2：实现判断一个数是不是回文数
'''


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


'''
判断一个数是不是素数
'''


def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


def foo():
    b = 'hello'

    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()


if __name__ == '__main__':
    a = 100
    foo()
