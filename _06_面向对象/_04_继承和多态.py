class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Dog类和Cat类继承了Animal类
# todo 1.继承的功能1：
#      子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法
dog = Dog()
print(dog.run()) #Animal is running...

#todo 2.子类可以重写父类方法
class Dog(Animal):

    def run(self):
        print('Dog is running...')

 # todo 3.子类可以对父类进行扩展
    def eat(self):
        print('Eating meat...')

#todo 4.继承可以用于多态
