

#todo 1. 关键字lambda表示匿名函数，冒号前面的x表示函数参数
#todo 2. 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


#todo 3. 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x

#todo 4. 匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
# 注意：这里lambda表达式省略了参数x和y， 至简原则

L = list(filter(lambda n : n % 2 == 1, range(1, 20)))