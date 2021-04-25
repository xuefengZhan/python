#todo 1.很多时候，数据读写不一定是磁盘上的文件，也可以在内存中读写。
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

# from io import StringIO
# f=StringIO()
# f.write('hello')
#
# f.write(' world')
#
# print(f.getvalue())
# f.close()
#往内存中写，读取内存中的字符串

# todo 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
from io import StringIO
f = StringIO('你哭着对我说\n童话里的故事都是骗人的')
while True:
    r = f.readline()
    if r == '':
        break
    print(r.strip())
