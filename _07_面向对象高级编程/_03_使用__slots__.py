#todo 1.限制Class实例能够动态添加的属性

# 1.在定义class的时候，定义特殊变量__slots__ 限制该class实例能够添加的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

s=Student()
s.name='asd'
s.age=99
# s.score=23   报错
# Traceback (most recent call last):
#   File "E:/python/study/_07_面向对象高级编程/_03_使用__slots__.py", line 10, in <module>
#     s.score=23
# AttributeError: 'Student' object has no attribute 'score'

#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

# todo 2. __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass
g=GraduateStudent()
g.score=29
print(g.score)

#todo 3.除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。