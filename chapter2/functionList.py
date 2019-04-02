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

lst = [1,2,3]
lst.append(4)
print(lst)

arrayCount = ['to','be','or','not','to','be']
print(arrayCount.count('to'))

x = [[1,2], 1, 1, [2, 1, [1,2]]]
print(x.count(1))
print(x.count([1,2]))

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a)

a = [1,2,3]
b = [4,5,6]
a[len(a):] =b
print(a)