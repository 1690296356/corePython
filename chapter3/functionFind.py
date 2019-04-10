#find方法可以在一个较长的字符串中查找子串。他返回子串所在位置的最左端索引。如果没有找到则返回-1
print('With a moo-moo here. and a moo-moo there'.find('moo'))

title= "Monty Python's Flying Circus"
print(title.find('Monty'))
print(title.find('Python'))

print(title.find('Flying'))
print(title.find('Zirquss'))


subject = '$$$ Get rich now!!! $$$'
print(subject.find('$$$'))

subject.find('$$$', 1)
subject.find('!!!')
#提供起始点和结束点
subject.find('!!!', 0, 16)


