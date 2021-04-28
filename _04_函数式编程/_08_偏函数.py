#todo 偏函数是Python的functools模块提供了的一个功能

#todo 举例说明
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print(int('1234'))            #1234
# int()其实提供了第二个参数base，但是是个默认参数，所以不写这个base的时候，默认按照十进制
print(int('12345', base=8))  # 5349

print(int('10',base=16)) #按照16进制转

#todo 偏函数定义方法：
import functools #导入模块
int2=functools.partial(int,base=2) #定义新的函数变量   参数是原函数对象和默认变量赋值
#todo 等价于
# def int2(x, base=2):
#     return int(x, base)

#todo 使用
print(int2('10010'))   #18

# todo 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。