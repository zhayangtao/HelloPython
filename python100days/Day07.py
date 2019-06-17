def main():
    str1 = 'hello world'
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.find('or'))
    print(str1.find('shit'))
    print(str1.index('or'))
    # print(str1.index('shit')) 找不到则抛异常
    print(str1.startswith('He'))
    print(str1.startswith('hel'))
    print(str1.endswith('!'))
    print(str1.center(50, '*'))
    print(str1.rjust(50, '*'))


def listtest():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    print(len(list2))


if __name__ == '__main__':
    main()
    listtest()
