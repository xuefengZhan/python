#todo 1.字符编码
# 计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理;
# 最早的计算机在设计时采用8个比特（bit）作为一个字节（byte）,
# 所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），
# 如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是65535，
# 4个字节可以表示的最大整数是4294967295;


#todo 2. ASCII码
# ASCII 只有1字节
# 最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号
# 大写字母A的编码是65，小写字母z的编码是122


#todo 3.处理中文
# 中国制定了GB2312编码，用来把中文编进去

#todo 4.Unicode
# Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
# Unicode编码通常是2个字节;
# Unicode编码兼容ASCII码，ASCII编码的A用Unicode编码，只需要在前面补0就可以
# 但是如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算
# 本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。

#todo 5.UTF
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节：
# 常用的英文字母被编码成1个字节
# 汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。
# 如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间。


#todo 6.字符串
#todo 6.1python字符串是Unicode编码的
# 1字节可以包含ASCII码的内容，字母，数字都可以用1字节装下，因此对于纯英文，数字可以将字符串转为字节串
x=b'ABC'
print(x)

# todo 6.2 解码 ： 将字节串转为Unicode字符串
print(x.decode('ascii'))

#todo 6.3 编码：将Unicode字符串按照某种编码方式转为字节串
y='ABC'
print(y.encode('ascii'))

z='我的老嘎'
print(z.encode('utf-8'))


#todo 7.格式化字符串
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

#占位符	替换内容
#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数