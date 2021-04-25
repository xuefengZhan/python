#todo 操作二进制流
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
#todo 说明： str.encode() 是将字符串按照编码格式编码成二进制

