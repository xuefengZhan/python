#todo 迭代
# 迭代是一种遍历方式：用for in这种方式遍历我们称为迭代（Iteration）。

#todo 可迭代对象
# 可迭代对象指的就是可以用for in 来迭代遍历的对象
# list,tuple,dict,str 都是可迭代对象 可迭代对象不要求有索引



#todo 3. dict的迭代
# dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

#todo 3.1迭代key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print('%s : %i' % (key,d[key]))

#todo 3.2迭代value
for value in d.values():
    print('%s ' % value)

#todo 3.3迭代k-v
for item in d.items():
    print(item)

#todo 4.str
a='asdgsdf'
for i in a:
    print(i)

#todo 5.判断判断一个对象是可迭代对象
# 通过collections模块的Iterable类型判断
from collections import Iterable
isinstance('abc', Iterable)

#todo 6.把一个list变成索引-元素对 python内置函数enumerate
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

l=[1,2,3,4]
len(l)

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for i in L:
        if min > i:
            min = i
        if max < i:
            max = i
    return (min, max)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')