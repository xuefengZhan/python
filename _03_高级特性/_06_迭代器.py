# todo  1.回顾可迭代对象的概念
#  可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#  list、tuple、dict、set、str，generator
#  可以使用isinstance()判断一个对象是否是Iterable对象：


#todo 2.迭代器对象的概念
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 因此只有生成器是迭代器
# 可以使用isinstance()判断一个对象是否是Iterator对象：


#todo 3.可以使用iter()函数把list、dict、str等Iterable变成Iterator:
from collections.abc import Iterator
isinstance(iter([]), Iterator)
isinstance(iter('abc'), Iterator)


#todo 4.iterator的特点
# #Python的Iterator对象表示的是一个数据流，是一个惰性序列
# Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列
# 我们不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据
# # Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# # Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

