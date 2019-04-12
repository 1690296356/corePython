#字典使用人名作为减，每个人用另一个字典表示，其键‘phone’和‘addr'分别表示他们的电话号码和地址
people = {
    'Alice':{
        'phone':'2341',
        'addr':'Foo drive 23'
    },
    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
    },
    'Cecil':{
        'phone':'3158',
        'addr':'Baz avenue 90'
    }

}

##get方法是个更宽松的访问字典项的方法，一般来说，如果试图访问字典中不存在的项时会出错

d ={}

#print(d['name'])
#使用get访问一个不存在的键时，没有任何异常，而得到了None值。还可以自定义“默认值”，替换None
print(d.get('name'))

#如果键存在，get用起来就像普通的字典查询一样
d['name'] = 'Eric'
print(d.get('name'))

#使用get()的简单数据库

labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')

#查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')

#使用正确的键：
#如果请求既不是‘p’也是不‘a’
key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

#使用get()提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("%s's %s is %s." % (name, label, result))

#has_key方法可以检查字典中是否含有特定的键。表达式d.has_key(k)相当于表达式k in d.使用哪个方式很大程度上取决于个人的喜好
#Python 3.0中不包括这个函数
d = {}
if 'Eric' in d.keys():print('true')
d['name'] = 'Eric'
if 'Eric' in d.keys():print('true')



