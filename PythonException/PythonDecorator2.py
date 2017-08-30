"""
Fole devtools.py: function decorator that performs range-test
validation for passed arguments, arguments are specified by
keyword to the decorator. In the actual call, arguments may
by passed by position or keyword, and defaults may be omitted.
See devtools_dev.py for example use cased;
"""

trace = True

def rangetest(**argchechecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            import sys
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__

            def onCall(*pargs, **kwargs):
                positionals = list(allargs)
                positionals = positionals[:len(pargs)]

                for (argname, (low, high)) in argchechecks.items():
                    if argname in kwargs:
                        if kwargs[argname] < low or kwargs[argname] > high:
                            errmsg = ...