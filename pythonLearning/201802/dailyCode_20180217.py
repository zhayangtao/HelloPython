found = False
while True and not found:
    # break
    if False:
        print('Ni')
        found = True
        break
    else:
        break
else:
    pass


def func():
    found = 1
    print(found)


def insert():
    found = False

    def add():
        nonlocal found
        print('add')
    print('insert')
    return add


def main():
    func()
    insert()


if __name__ == '__main__':
    main()
