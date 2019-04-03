#sort方法用于在原位置对列表进行排序。在“原位置排序”意味着改变原来的列表，从而让其中的元素能按一定的顺序排列，而不是简单地返回一个已排序的列表副本
x = [4,6,2,1,7,9]
x.sort()
print(x)


#再次调用x1[:]得到的是包含了x所有元素的分片，这是一种很有效率的复制整个列表的方法。只是简单地把x赋值给y是没用的，因为这样做就让x和y都指向同一个列表了
x1 = [4,6,2,1,7,9]
y =x1[:]
y.sort()
print(x1)
print(y)

#另一种获取已排序的列表副本的方法是，使用sorted函数：
x = [4,6,2,1,7,9]
y = sorted(x)
print(y)

character = 'Python'

print(sorted(character))

#cmp(42, 32)
numbers = [5,2,9,7]

numbers.sort()

print(numbers)


x = ['aardvark','abalone','acme','add','aerate']
x.sort()
print(x)


x = [4,6,2,1,7,9]
x.sort()
print(x)


x = (1,2,3)
print(x)
s = 1,2,3
print(s)
t=()
print(t)

z=42
print(z)
u=42.
print(u)

#实现包括一个值的元组。实现方法有些奇特--必须加个逗号，即使只有一个值：
h1 =3*(40+2)
print(h1)

h2 =3*(40+2.)
print(h2)

k = tuple([1,2,3])
print(k)

#tuple函数的功能与list函数基本上一样的以一个序列作为参数并把它转换为元组。如果参数就是元组，那么参数就会被原样返回
l =tuple('abc')
print(l)
s = tuple((1,2,3))
print(s)

#元组其实并不复杂--出了创建元组和访问元素之外，也没有太多其他操作，可以参照其他类型的序列来实现
#元组的分片还是元组，就像列表的分片还是列表一样
x = 1,2,3
print(x[1])
print(x[0:2])







