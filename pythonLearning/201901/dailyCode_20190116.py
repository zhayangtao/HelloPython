def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


def sum_of_powers(*args, power=1):
    result = 0
    for arg in args:
        result += arg ** power
    return result


def heron2(a, b, c, *, units="meters", d):  # * 表示之后不能再出现位置参数 *args
    s = (a + b + c) / 2


language = "en"
ENGLISH = {0: "zero", 1: "one", 2: "two"}
FRENCH = {}


def print_digits(digits):
    dictionary = ENGLISH if language == "en" else FRENCH
    for digit in digits:
        print(dictionary[int(digit)], end=" ")
    print()


s = lambda x: "" if x == 1 else 's'

import collections

minus_one_dict = collections.defaultdict(lambda: -1)
# print(minus_one_dict)
for k, v in minus_one_dict.items():
    print(k, v)
print(minus_one_dict[2])
point_zero_dict = collections.defaultdict(lambda: (0, 0))
point_zero_dict[1] = 1
print(point_zero_dict[2])
message_dict = collections.defaultdict(lambda: "No message available")

# 断言
assert minus_one_dict is not None

import datetime


def get_string(param, param1, param2):
    pass


def populate_information(information):
    name = get_string("Enter your name", "name", information['name'])


def main():
    information = dict(name=None, year=datetime.date.today().year, filename=None, title=None,
                       description=None, keywords=None, stylesheet=None)
    while True:
        try:
            print("\nMake HTML Skeleton\n")
            populate_information(information)
        except Exception:
            print("Cancelled")
