x = 1


def selector():
    print(x)
    # x = 88


def selector2():
    global x
    print(x)
    x = 55


def selector3():
    import __main__
    print(__main__.x)
    x = 88
    print(x)


def saver(x=[]):
    x.append(1)
    print(x)


def saver2(x=None):
    if x is None:
        x = []
    x.append(1)
    print(x)


# 使用函数属性
def saver3():
    saver3.x.append(1)
    print(saver3.x)


def main():
    selector()
    x = []
    x.append(1)
    print(x)
    print('*' * 8)
    saver([2])
    saver()
    saver()  # 坑
    saver()  # 坑
    print('saver2 begin')
    saver2([2])
    saver2()
    saver2()
    saver2()
    print('saver3 begin')
    saver3.x = []
    saver3()
    saver3()
    saver3()


import dailyCode_20180303
import dailyCode_20180303


if __name__ == '__main__':
    main()
