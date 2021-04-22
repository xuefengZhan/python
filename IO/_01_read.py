#todo 1.读取文件  open方法
f=open('C:/Users/詹学丰/Desktop/git.txt',mode='r',encoding='utf-8')
print(type(f))    #todo 2.返回值是一个_io.TextIOWrapper类对象
print(f.read())   #todo 3.read()方法读取文件全部内容到内存


#todo 4.关闭文件流   用完后必须关闭
# 文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
f.close()



#todo 5. 文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('C:/Users/詹学丰/Desktop/git.txt',mode='r',encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()

#todo 5.每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open('C:/Users/詹学丰/Desktop/git.txt',mode='r',encoding='utf-8') as f:
    print(f.read())
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

