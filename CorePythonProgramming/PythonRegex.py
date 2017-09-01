import re

m = re.match('foo', 'foo')
if m is not None:
    m.group()