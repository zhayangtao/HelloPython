# 将二进制转换为字符串
import base64
e = base64.b64encode(b'binary\x00string')
print(e)
d = base64.b64decode(b'binary\x00string')
print(d)