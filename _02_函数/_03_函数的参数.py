#todo 1.默认参数
# 必选参数在前，默认参数在后
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
def power(x,n=2):
    return x*n

#todo 2.默认参数函数调用
print(power(5))
print(power(5, 3))

#todo 3.默认参数的数据类型不能是可变数据类型 比如list
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())  #['END']
print(add_end())  #['END', 'END']
#todo 理解： 函数名+参数相当于一个对象，默认参数相当于该对象的属性值；
# 调用add_end()的时候相当于 该对象的L属性 追加了END,由于是可修改的，所以内容就保存进去了
# 修改：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


#todo 4. 可变参数   python中可变参数未必要放在最后一个，如果可变参数后面还有参数，
# name后面的参数编程命名关键字参数
# 4.1 将零散的参数组装成tuple
# 在调用该函数的时候，可以传入任意个参数，包括0个
# 将实参封装为一个tuple传递给参数numbers
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3, 4, 5))

# todo 4.2 将list或者tuple变为零散的参数再传给可变参数
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
print(calc(*nums))


#todo 5.关键字参数       **函数名
# 如果说可变参数是tuple的话，那么关键字参数就是dict
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

#todo 5.1定义
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

#todo 5.2 调用  传入的是任意多个  key=value形式的实参
print(person('Michael', 30))  #name: Michael age: 30 other: {}
print(person('Bob', 35, city='Beijing')) #name: Bob age: 35 other: {'city': 'Beijing'}

print(person('Adam', 45, gender='M', job='Engineer')) #name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#todo 5.3 参数是dict的时候，先拆开，再传入
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack',17,**extra))



#todo 6.命名关键字参数    将关键字参数的key固定，并且限定了关键字参数key-value对的个数
# todo  6.1 定义
def student(name,age,*,school,address):
    print('name', name, 'age',age,'school',school,'address',address)

#todo 6.2使用  命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错；
# 报错： print(student('jack', 18, school='一中', address='大事上', girl='无'))
print(student('jack', 18, school='一中', address='大事上'))


#todo 7. 可变参数 结合 命名关键字参数
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person1(name, age, *args, city, job):
    print(name, age, args, city, job)