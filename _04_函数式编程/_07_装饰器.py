#todo 装饰器就是给函数增加额外功能的,但是不改动函数本身的定义
#  在代码运行器件动态增加函数功能

#todo 被装饰函数
# def now():
#     print('2021-04-27')

#todo 装饰器 decorator
# 特点：接受一个被装饰函数作为参数，并返回一个装饰函数
#      装饰函数中调用了被装饰函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#todo 使用decorator
@log
def now():
    print('2015-3-25')

#todo 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)
# 由于log()是一个decorator，返回一个函数，
# 所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
print(now())
#call now():
#2015-3-25


#todo 2.带参数的装饰器   需要再嵌套一层
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#使用
@log('execute')
def en():
    print('2015-3-25')

en()
# execute en():
# 2015-3-25

# todo 说明
#  now = log('execute')(now)
#  首先执行log('execute')，返回的是decorator函数，
#  再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

# todo 验证 装饰后的now函数，其实是wrapper函数
print(now.__name__) #wrapper  不再是now

# todo 将被装饰函数的属性赋值给装饰函数
# 因为返回的那个wrapper()函数名字就是'wrapper'，
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错。
# Python内置的functools.wraps就是干这个事的

# 使用方法： @functools.wraps(func)   参数是被装饰函数   位置放在装饰函数定义的上面
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator