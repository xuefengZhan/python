#todo 通过列表生成式，我们可以直接创建一个列表。
# 但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
# 如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

#todo 生成器的写法：  和列表生成式仅差别在括号
g = (x * x for x in range(10))

#todo 区别： 列表生成式是直接在内存中生成一个list
# generator只保存算法不保存数据，只有访问到某个元素，才会计算出这个元素是什么
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#todo 当next(g)没有更多的元素时，抛出StopIteration的错误。

#todo generator也是可迭代对象
for n in g:
    print(n)

#todo 2. 无论是列表生成式还是生成器 for前面其实是一个匿名函数
# 当函数比较复杂，就可以用函数来实现
# 斐波拉契数列 1, 1, 2, 3, 5, 8, 13, 21, 34, ..
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# 定义了每个元素的计算方式  b是输出
# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(5):
    print(n)      #1 1, 2, 3, 5

#todo 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator;

#todo 函数式generator的执行流程和普通函数不同
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# 而变成generator的函数：
#       1.在每次调用next()的时候执行
#       2.遇到yield语句返回
#       3、再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
for i in o :
    print(i)
#step 1
#1

#step 2
#3

#step 3
#5

#todo 函数式generator中有return的时候，必须捕获越界异常才能执行到return

