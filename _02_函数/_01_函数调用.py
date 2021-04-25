#todo 1.内置函数直接调用
#todo 2.函数调用方式： 直接函数名+参数即可
abs(100)


#todo 3.函数调用时，参数个数不对、类型不对都会报错

#todo 4.函数名 其实就是指向一个函数对象的引用
# ，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

a = abs # 变量a指向abs函数
print(a(-1) )


#todo 5. 导入函数
# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，
# 那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）