# 工厂函数
def maker(N):
    def action(X):
        return X ** N
    return action


def test():
    x = 1

    def test2():
        x = 2
        print(x)

    test2()
    print(x)


def func():
    x = 4
    action = (lambda n: x ** n)
    print(action)


def main():
    test()


if __name__ == '__main__':
    main()
