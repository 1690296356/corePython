##get方法是个更宽松的访问字典项的方法，一般来说，如果试图访问字典中不存在的项时会出错

d ={}

#print(d['name'])
#使用get访问一个不存在的键时，没有任何异常，而得到了None值。还可以自定义“默认值”，替换None
print(d.get('name'))

#如果键存在，get用起来就像普通的字典查询一样
d['name'] = 'Eric'
print(d.get('name'))