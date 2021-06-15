#todo 1.判断对象类型，使用type()函数
# 1.判断基本数据类型
print(type(123))
# 2.判断变量的类型
# 3.函数类型也可以判断
def fn():
    pass


print(type(fn))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in range(10))))


#todo 2.isinstance()
# type 只能判断基本类型，变量，函数的类型 不能获取子父类关系
# isinstance()可以判断和父类是否有关系 比type()更强大


#todo 3.dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
# 比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))

#todo 类似__xxx__的属性和方法在Python中都是有特殊用途的，
# 比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
len('ABC')
'ABC'.__len__()


 