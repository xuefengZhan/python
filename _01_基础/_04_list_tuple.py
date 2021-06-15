#todo 1.list  list是一种有序的集合，可以随时添加和删除其中的元素。

#todo 1.1 list-根据索引查询元素
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(classmates[0])
print(classmates[-1])

#todo 1.2 list-增加元素
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)

#todo 1.3 list-删除元素
s=classmates.pop()#删除list末尾元素
print(s)
print(classmates)

l=classmates.pop(1)
print(l)
print(classmates)

#todo 1.4 list-修改索引位置的元素
classmates[1] = 'Sarah'
print(classmates)

#todo 1.5 list元素可以是不同类型   py没有泛型
L = ['Apple', 123, True]
print(L)

#嵌套list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2])
print(s[2][1])

#todo 1.6 list长度
len(s)

#todo range生成list   range(x)   <x
s= list(range(5))  #[0, 1, 2, 3, 4]






#todo tuple 初始化后不可改变，因此没有append，insert,pop方法
#不可变指的是元素的值不可变；如果是引用地址，地址不变，地址中存的
#内容变了，还是可以的。
c = ('Michael', 'Bob', 'Tracy')
print(c)

c1=()
print(c1)

#todo 只有一个元素的tuple的定义
c2=(1)
print(c2)

c3=(1,)
print(c3)   #(1,)

c4=(1,)
print(c4) #(1,)

#todo tuple中的元素为可变对象时，可以变
t = ('a', 'b', ['A', 'B'])
t[2][0]='x'
t[2][1]='f'
print(t) #('a', 'b', ['x', 'f'])
