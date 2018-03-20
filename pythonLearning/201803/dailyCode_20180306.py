x = 88


def f():
    global x
    x = 99


from imp import reload

from dailyCode import line as L
# from dailyCode_20180304.dailyCode_20180304 import timer
import string  # 先从相对路径导入模块
print(string)

from  . import string
print(string)