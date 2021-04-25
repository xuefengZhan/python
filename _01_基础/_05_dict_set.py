d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

#todo dict就是map，查询速度很快

#todo 添加元素或者更改元素
d['Jack'] = 90
print(d)

d['Jack'] = 88
print(d)


#todo 判断key是否存在于dict中
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas','这个真木有'))

#todo dict的key不能为可变元素



#todo set   就是map的key的集合，不重复，无序
# todo 1.创建一个set，需要提供一个list作为输入集合：
s = set([1, 1, 2, 2, 3, 3])
print(s)   #{1, 2, 3}

#todo set 增删元素
s.add(4)
s.remove(4)
