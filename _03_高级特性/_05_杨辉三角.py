def fib(m):
    a=0
    b=1
    n=1
    while(n<=m):
        yield b
        a,b=b,a+b
        n=n+1
g=fib(6)

for i in g:
    print(i)


# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
#把每一行看做一个list，试写一个generator，不断输出下一行的list：
# def yang(m):
#     n=1
#     while n<= m:


