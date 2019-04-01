x = 3
x = x*2
print(x)

print(abs(-10))
print(1/2)
print(1.0/2.0)
print(round(1.0/2.0))

import math
print(math.floor(32.9))

from math import sqrt
print(sqrt(9))

#raw_input("Press <enter>")

#打印圆的周长
import math
radius = 5
print(2*math.pi*radius)

print('Hello world')
print("Hello world")

#使用反斜线（\）对字符串中的引号进行转义
print('Let\'s go!')
print("\"Hello, world!\" she said")

print("Let's say "'"Hello world!"')

x = "Hello. "
y = "world!"
print(x+y)


print(10000)

#一种是通过str函数，它会把值转换为合理形式的字符串
#另一种是通过repr函数，它会创建一个字符串，以合法的Python表达式的形式来表示值

print(repr("Hello. world!"))
print(str("Hello. world!"))
print(repr(10000))
print(str(10000))

#如果希望打印一个包含数字的句子，那么反引号就很有用了
temp = 42
print("The temperature is "+ repr(temp))
print("The temperature is "+ str(temp))


#简而言之，str ，repr和反引号是将python值转换字符串的方法
#str让字符串更容易阅读 repr则把结果字符串转换为合法的python表达式

name = input("what is your name?")
print('hello. '+name+"!")

number = input("enter a number: ")
print("the number is "+number+"!")

rawNumber = input("enter a number: ")
print("the number is "+rawNumber+"!")

#如果需要一个非常长的字符串，他需要跨多行，那么，可以使用三个引号代替引号

print('''This is a very long string. It continuesc if here.And it's' not over yet. "Hello it's not over yet. Still here.''')

print("Hello. \
      world!")



from math import sqrt
#math domain error
#sqrt(-1)

a = 1
b = 2
c = 1
if a == b:
    print("one equals two")
    if a == c:
        print("one equals one")



