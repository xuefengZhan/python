
#todo 1. 某些代码可能会出错时，就可以用try来运行这段代码，
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

# try:
#     print('try...')
#     r=10/0
#     print('result',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally')
# print('end')

#todo 2.多错误处理：错误类型比较多时
# int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，
# 用另一个except捕获ZeroDivisionError。

# try:
#     print('try......')
#     r=10/int('a')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)

#todo 3.如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句

# try:
#     r=10/int('1')
#     print('r: ',r)
# except ValueError as e:
#     print('ValueError: ',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('a没问题啊')


#todo 4.Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽
# 如果第一个except捕获了一个父类Exception，name后续的except如果是子类就啥都捞不到了





#todo 5.跨方法捕获
# try-catch最本质是捕获语句发生异常，但是往往会被方法封装
# try—catch可以捕获 发生错误的方法所抛出来的异常
# 如果当前方法内部没有捕获此异常， 此异常会一值往调用方法抛，直到main方法


#todo 6.调用栈
# 如果错误没有被捕获，它就会一直往上抛，
# 最后会由Python解释器捕获，并且打印一个错误信息，然后程序退出。
# 错误信息就会记录这个错误是如何由外向内一层一层抛出来的，从而找到错误源头

# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
#
# def main():
#     bar('0')
# main()
# print('end')  #由于main()报错了，所以这个print()不会执行了



#todo 7.如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
# Python内置的logging模块可以非常容易地记录错误信息：

# import logging
# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('end')  #也会执行
#通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

#todo 8.错误处理方式2：抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。
# 因此，错误并不是凭空产生的，而是有意创建并抛出的。
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，
# 然后，用raise语句抛出一个错误的实例：
# class FooError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value : %s' % s)
#     return 10/0
# foo('0')

#todo 9.错误处理方式3：捕获并抛出
# 在bar()函数中，我们明明已经捕获了错误，
# 但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
# 捕获错误目的只是记录一下，便于后续追踪。
# 但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise   #在except中 将错误抛出
# bar()

# todo 说明： 1.raise语句如果不带参数，就会把当前错误原样抛出。
#            2.此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
            #try:
            #    10 / 0
            #except ZeroDivisionError:
            #    raise ValueError('input error!')
            # 只能将错误转换为父类错误
