# a = int(input('a='))
# b = int(input('b='))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d %% %d = %d' % (a, b, a % b))

a = 100
b = 12.345
c = 1 + 5j
d = 'hello,world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


"""
练习1：华氏温度转摄氏温度
F = 1.8C + 32
"""

f = float(input('请输入华氏温度：'))
c = (f -32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

"""
练习2：输入圆的半径计算周长和面积
"""
import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)

"""
练习3：输入年份判断是不是闰年
"""
year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)