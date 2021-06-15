#todo
# 这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。


#todo 1.__str__
# 作用是 打印对象的时候，调用的是对象的__str__方法    类似于java的toString
# 这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name : %s)' % self.name

print(Student("超人不会飞"))  #Student object (name : 超人不会飞)

# todo  2.__repr__
#  但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
#>>>s = Student('Michael')
#>>>s
#<__main__.Student object at 0x109afb310>
#这是因为直接显示变量调用的不是__str__()，而是__repr__()
# 两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。
# 但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__


# todo 3.__iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。
# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib():
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
for i in Fib():
    print(i)

