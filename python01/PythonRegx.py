# 正则表达式
s = 'ABC\\-001'
s = r'ABC\-001'

import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

# 分组 用()表示的就是要提取的分组（Group）。
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))  # 原始字符串
print(m.group(1))
print(m.group(2))

# 预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
