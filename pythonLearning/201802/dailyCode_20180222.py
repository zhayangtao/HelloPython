x = 99


def setX(new):
    global x
    x = new


var = 99


def local():
    var = 0


def glob1():
    global var
    var += 1


def glob2():
    var = 0
    import dailyCode_20180222
    dailyCode_20180222.var += 1


def glob3():
    var = 0
    import sys
    glob = sys.modules['dailyCode_20180222']
    glob.var += 1


def test():
    print(var)
    local()
    glob1()
    glob2()
    glob3()
    print(var)


def main():
    test()


if __name__ == '__main__':
    main()
