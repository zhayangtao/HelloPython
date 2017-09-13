import urllib
import sys
import decimal


a = decimal.Decimal(3333)

s = input('enter an integer:', )
i = int(s)
print('valid integer entered:', i)


Digits = [
    ['***']
]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + ""
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <mumber>")
except ValueError as err:
    print(err, "in", digits)


s = ("This is the nice way to join two long strings"
     "together")


def extract_from_tag(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        j = line.find(closer, start)
        if j != -1:
            return line[start:]
    return None


"The novel '{0}' was published in {1}".format("Hard Times", 1835)
"{who} turned {age} this year".format(who="She", age=88)

stock = ['paper', 'envelopes', 'notepads', 'paper clips']
"we have {0[1]} and {0[2]} in stock".format(stock)

d = dict(animal="elephant", weight=12000)
"The {0[animal]} weighs {0[weight]}kg".format(d)