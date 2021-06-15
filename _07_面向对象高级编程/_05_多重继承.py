class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

#
# class Runnable(object):
#     def run(self):
#         print('Running...')
#
# class Flyable(object):
#     def fly(self):
#         print('Flying...')
#
#
# class Dog(Mammal, Runnable):
#     pass
#
# class Bat(Mammal, Flyable):
#     pass



#todo MixIn
# 多重继承又叫MixIn,表示一个类除了单线继承，还混入了额外的功能
# 其实只是一个标识作用，标识这是额外混入功能
# 将这些混入的类用MixIn做后缀进行标识

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, RunnableMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass
# todo MixIn的目的就是给一个类增加多个功能，
#  这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，
#  而不是设计多层次的复杂的继承关系。
#
#  Python自带的很多库也使用了MixIn。
#  举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
#  而要同时服务多个用户就必须使用多进程或多线程模型，
#  这两种模型由ForkingMixIn和ThreadingMixIn提供。
#  通过组合，我们就可以创造出合适的服务来。

