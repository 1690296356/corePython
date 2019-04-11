phonebook = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
print(phonebook['Cecil'])

##可以用dict函数，通过其他映射（比如其他字典）或者（键，值）对的序列建立字典
items = [('name','Gumby'),('age', 42)]
d = dict(items)
print(d)

##dict函数也可以通过关键字参数来创建字典
d=dict(name='Gumby', age=42)
print(d)

##x = []
##x[42] = 'Foobar'
##print(x)

x = {}
x[42] = 'Foobar'
print(x)