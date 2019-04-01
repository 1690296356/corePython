AList = list('Hello')

print(AList)

#可以用下面的表达式将一个由字符组成的列表转换为字符串
print(''.join(AList))


x = [1,1,1]
x[1] = 2
print(x)

#x[100] = 2
#print(x)

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)
print(len(names))

name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)

name = list('Perl')
name[1: ] = list('ython')
print(name)

numbers = [1,5]
numbers[1:1] = [2,3,4]
print(numbers)

numbers[1:4] = []
print(numbers)