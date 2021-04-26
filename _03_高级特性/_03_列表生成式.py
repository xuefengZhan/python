#todo 列表生成式即List Comprehensions
# Python内置的非常简单却强大的可以用来创建list的生成式。

list(range(1, 11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#todo 1.加表达式
l = [x * x for x in range(1, 11)]  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l)

#todo 2.加过滤
l1 = [x * x for x in range(1, 11) if x % 2 == 0] #[4, 16, 36, 64, 100]
print(l1)

#todo 3.多个变量
l2 = [m + n for m in 'ABC' for n in 'XYZ']
print(l2) #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#todo 4.迭代dict生成列表
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

l3 = [k + '=' + v for k, v in d.items()]
print(l3)

l4=[i for i in range(5) if(i > 0 and i < 4)]
l4[0] = 0
#l4[4]=1
print(l4)
