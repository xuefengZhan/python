d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

#todo dict就是map，查询速度很快

#todo 1.添加元素或者更改元素
d['Jack'] = 90
print(d)

d['Jack'] = 88
print(d)


#todo 2.判断key是否存在于dict中
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas','这个真木有'))

#todo 3.dict的key不能为可变元素
#todo 4.dict内部存放顺序和key放入顺序没有关系
#todo 5. 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。



#todo set   就是map的key的集合，不重复，无序
# todo 1.创建一个set，需要提供一个list作为输入集合：
# todo 同理  key的显示的顺序也不表示set是有序的。。
s = set([1, 1, 2, 2, 3, 3])
print(s)   #{1, 2, 3}

#todo set 增删元素
s.add(4)
s.remove(4)

#todo set交并差
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2