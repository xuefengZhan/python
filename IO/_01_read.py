#todo 1.读取文件  open方法

# f=open('C:/Users/詹学丰/Desktop/git.txt',mode='r',encoding='utf-8')
# print(type(f))    #todo 2.返回值是一个_io.TextIOWrapper类对象
# print(f.read())   #todo 3.read()方法读取文件全部内容到内存，内容是一个str对象


#todo 4.关闭文件流   用完后必须关闭
# 文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
# f.close()



#todo 5. 文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

# try:
#     f = open('C:/Users/詹学丰/Desktop/git.txt',mode='r',encoding='utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()

#todo 6.每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

# with open('C:/Users/詹学丰/Desktop/git.txt',mode='r',encoding='utf-8') as f:
#     print(f.read())


#todo 7.read()是将文件内容一次性读取到内存中的，如果文件有10G，内存就爆了
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
# 因此，要根据需要决定怎么调用。

# with open('C:/Users/詹学丰/Desktop/git.txt',mode='r',encoding='utf-8') as f:
#     i = 1
#     for line in f.readlines():
#         print('第 %i 行 ' % i + line.strip())
#         i = i+1

#todo 8.file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。


#todo 9.二进制文件
# 对于文本文件，可以指定编码方式，直接读取；
# 但是对于二进制文件，如图片，视频等，需要用rb模式打开文件
f=open('C:/Users/詹学丰/Desktop/git.txt',mode='rb')
print(f.read())
f.close()

# todo 10.字符编码
#  读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数,表示读取什么编发方式的文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')


#todo 11.忽略非法编码字符
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

