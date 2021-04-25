#todo 1.list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(classmates[0])
print(classmates[-1])


classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)

s=classmates.pop()
print(s)
print(classmates)

l=classmates.pop(1)
print(l)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

#todo list元素可以不痛类型
L = ['Apple', 123, True]
print(L)

#todo 嵌套list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2])
print(s[2][1])


#todo range生成list   range(x)   <x
s= list(range(5))  #[0, 1, 2, 3, 4]






#tuple  不可改，没有append，insert,pop方法
c = ('Michael', 'Bob', 'Tracy')
print(c)

c1=()
print(c1)

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
