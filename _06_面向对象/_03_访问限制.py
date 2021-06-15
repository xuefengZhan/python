
#todo 说明：
#     前面数据封装只是说明了 类可以自己提供读写 类自己的数据的方法，从而避免用类外部的函数来访问类中的数据
#     但是，并没有限制类内部的数据 不可以被类外部的函数访问
#     而访问限制的目的就是： 限制实例数据不能在类外部被访问，只能由实例类提供的方法访问
#bart = Student('Bart Simpson', 59)
# print(bart.score)    读取
# bart.score = 99      修改

#todo 1. 限制类内部数据的访问
# 如果要让内部属性不被外部访问，必须将变量设置为私有变量，只有内部可以访问，外部不能访问
# 具体做法是： 在属性的名称前加上两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）

class Student(object):

    #__init__类似构造器方法
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

#todo 此时不能用类外部的函数来读取该类实例的数据，但是是可以修改的
s=Student('zxf',100)
s.print_score() #zxf: 100

# print(s.__score) #报错  AttributeError: 'Student' object has no attribute '__score'




#todo Private数据的set和get方法
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

# todo 3.
#  特殊变量： 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
#           特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
#  比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，
#             意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#  双下划线开头的实例变量是不是一定不能从外部访问呢？
#  其实也不是。
#  不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
#  所以，仍然可以通过_Student__name来访问__name变量
#  但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。



#todo 4. 错误示范
bart = Student('Bart Simpson', 59)
bart.__name = 'New Name'  # 设置__name变量！
print(bart.__name)
# 表面上看，外部代码“成功”地设置了__name变量，
# 但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，
# 而外部代码给bart新增了一个__name变量。不信试试：
print(bart.get_name())  # 还是 Bart Simpson !