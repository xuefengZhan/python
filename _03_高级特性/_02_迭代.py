#todo 可以通过for in 来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

#todo 可迭代对象 Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print('%s : %i' % (key,d[key]))