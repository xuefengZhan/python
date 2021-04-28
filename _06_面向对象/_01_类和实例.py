#todo  1..类的定义
class Student(object):
    pass
print(Student)   #<class '__main__.Student'>
# class后面紧接着是类名，即Student，类名通常是大写开头的单词
# 紧接着是(object)，表示该类是从哪个类继承下来的,通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

#todo 2.根据类创建实例
# 创建实例是通过类名+()实现的
bart = Student()
print(bart) #<__main__.Student object at 0x0000020685207490>

#todo 3.自由地给实例变量绑定属性
bart.name = 'Bart Simpson'
print(bart.name)

#todo 4.每个实例的必要属性需要在定义类的时候绑定
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

# todo 5.定义了__init__方法的类创建实例：
#  有了__init__方法，在创建实例的时候，就不能传入空的参数了
#  必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)

# todo 6.类中的函数定义特点
#  和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
#  并且，调用时，不用传递该参数。
#  除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
