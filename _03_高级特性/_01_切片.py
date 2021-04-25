#todo 1.切片就是获取list或者tuple的子序列
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#todo 1.1 正着 索引从0开始   倒着索引从-1开始

#todo 左闭右开 放在右边就等价于lenth-x
print(L[0:3]) #['Michael', 'Sarah', 'Tracy']
print(L[:3]) #['Michael', 'Sarah', 'Tracy']
print(L[:]) #['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[1:-2]) #['Sarah', 'Tracy']
print(L[1:-1]) #['Sarah', 'Tracy', 'Bob']
print(L[-2:]) #['Bob', 'Jack']
print(L[2:0])  #[]

#todo 1.2 步进
L = list(range(100))
print(L[:10:2])

#todo 注意： 切片只能取子序列，且不能改变顺序
#  tuple,list,str都可以使用切片

#todo 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if(s==''):
        return s
    # i 和 j 定义为正序和反序 第一个非' '的元素的索引
    i = 0
    j = -1
    while( i  <= len(s) + j):
        if(s[i] == ' '):
            i = i + 1
        if(s[j] == ' '):
            j = j - 1
        if(s[i] !=' ' and s[j] != ' '):
            s=s[i:len(s)+j+1]
            return s
    return ''


print(trim('  hello'))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')