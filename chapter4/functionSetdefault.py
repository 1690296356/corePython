##setdefault方法在某种程度上类似于get方法能够获得与给定键相关联的值，除此之外，setdefault还能在字典
##中不含有给定键的情况下设定相应的键值
d = {}
print(d.setdefault('name'))

print(d)