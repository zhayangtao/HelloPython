"I am: docstr.__doc__"


def func(args):
    "I am: docstr.func.__doc__"
    pass


class Spam:
    "I am: spam.__doc__ or docstr.spam.__doc__"

    def method(self, arg):
        "I am: spam.method.__doc__ or self.method.__doc__"
        pass


#################################################
# 运算符重载
##################################################

class Number:
    def __init__(self, start):
        self.data = start
    
    def __sub__(self, other):
        return Number(self.data - other)


class Indexer:
    def __getitem__(self, index):
        return index ** 2
    
    def __setitem__(self, index, value):
        self.value[index] = 2


class Stepper:
    def __getitem__(self, i):
        return self.data[i]


class Squares:
    def __init__(self, start, stop):
        self.value = start -1
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2



def main():
    import dailyCode_20180313
    print(dailyCode_20180313.__doc__)
    print(dailyCode_20180313.func.__doc__)
    print(dailyCode_20180313.Spam.__doc__)
    print(dailyCode_20180313.Spam.method.__doc__)
    print(Spam().method.__doc__)


if __name__ == '__main__':
    main()
