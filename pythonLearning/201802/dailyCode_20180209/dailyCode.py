"""
Module documentation
"""
spam = 40


def square(x):
    '''
    function documentation
    can we have your liver then?
    '''
    return x ** 2


class Employee:
    '''class documentation'''
    pass


print(square(4))
print(square.__doc__)
print(Employee.__doc__)

import sys
print(sys.__doc__)
import this