#python中循环有两种：

# 1是for in循环，用于迭代迭代器
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

