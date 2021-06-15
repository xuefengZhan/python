#todo 1.给实例动态绑定方法
class Student(object):
    pass

s=Student()

#  1.1 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age

#  1.2 导入MethodType模块
from types import MethodType
#  1.3 给实例绑定方法
s.set_age = MethodType(set_age,s)
#  1.4 通过实例调用方法
s.set_age(25)
#  测试
print(s.age)

#todo 2.给类绑定方法
#给实例绑定方法仅限于这个实例
def set_score(self, score):
    self.score = score
# 绑定给类
Student.set_score = set_score

# 类的所有实例均可以调用
s.set_score(100)
s2= Student()
s2.set_score(100)
print(s2.score)