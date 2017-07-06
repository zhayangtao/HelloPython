from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Month.Jan

# 元类，使用 type() 创建 class
def fn(self, name='world'):  #先定义函数
    print('Hello, %s' % name)
Hello = type('Hello', (object,), dict(hello=fn)) #创建 Hello class
h = Hello()

