age = 20
if age >= 18:
    print('your age is', age)
    print('adult')


age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#todo if后面是非零数值、非空字符串、非空list等，就判断为True，否则为False
if not []:
    print('True')