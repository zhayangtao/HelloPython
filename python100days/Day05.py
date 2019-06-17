"""
寻找水仙花数
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
"""
num = int(input('请输入正整数：'))
length = len(str(num))
count = length
num_sum = 0
while count:
    num_sum += ((num // 10 ** (count - 1)) % 10) ** length
    count -= 1
else:
    if num_sum == num:
        print("%d is %d bit narcissistic_number" % (num, length))
    else:
        print("%d is not a narcissistic_number" % num)

print(153 // 100)
print(153 // 10)
print(153 // 1)

"""
完全数
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是6，
第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
"""

num = int(input('请输入正整数：'))


# 获取最大约数
def getmax(n):
    count = num // 2
    while count > 1:
        if n % count == 0:
            return count
        else:
            count -= 1


print(getmax(num))

'''
斐波那契数列
'''


def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
    a, b = b, a + b
    fib(100)
