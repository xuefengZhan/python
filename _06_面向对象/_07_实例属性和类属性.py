#todo 1.动态语言，可以给类的实例任意绑定属性


#todo 2.给实例绑定属性的两种方法：
# （1）实例必绑定的属性
#  在定义类的时候，定义__init__方法，这样在构建实例的时候，必须绑定该属性
#  (2) 实例可扩展属性
#  在实例创建好之后，给实例绑定属性

#方式1：
class Student(object):
    def __init__(self, name):
        self.name = name
s = Student('Bob')

# 方式2：给Student的实例s绑定属性
s.score = 90

#todo 2.  给类绑定属性   这些是类属性，所有实例都有的
class teacher(object):
    name = 'cang'

#todo 2.1 类属性可以通过实例访问
t1 = teacher();
print(t1.name) #cang
#todo 2.2 类属性可以通过类名直接访问
print(teacher.name)

#todo 2.3 实例属性优先级高于类属性，属性重了以实例的为主
t1.name = 'Michael'
print(t1.name) #Student

#todo 2.4删除实例属性，恢复沿用类属性
del t1.name
print(t1.name) #cang
