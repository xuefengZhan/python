# 在上面的Student类中，每个实例就拥有各自的name和score这些数据。

# todo 所谓的数据封装指的就是在类内部定义函数用来访问这些数据，而不要用类外部的函数访问
#  类内部定义的函数可以访问类的数据，这些函数是和类是关联的，称之为类的方法；
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


# todo 通过实例调用类方法
s=Student('zxf',100)
s.print_score()