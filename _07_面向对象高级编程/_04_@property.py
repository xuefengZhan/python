#todo 1.使用@property 限制属性 的赋值范围

# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，
# 但是，没办法检查参数，导致可以把成绩随便改  这显然不合逻辑。

# 为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
class Student():
    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s=Student()
# s.set_score(101)  报错

#todo 简化set()和get()
#但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
#对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

# 在get()上面添加@property
# 在set()上面添加：属性名.setter
class Teacher(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

t=Teacher()
t.score=60  # OK，实际转化为s.set_score(60)
print(t.score) # OK，实际转化为s.get_score()

#todo 3.定义属性只读，只添加@property
class School(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

#todo 4.注意