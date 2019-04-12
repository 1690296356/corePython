##items方法将字典所有的项以列表方式返回，列表中的每一项都表示为（键，值）对的形式。
##但是项在返回时并没有遵循特定的次序

d = {'title':'Python Web Site','url':'http://www.python.org','span':0}
print(d.items())

##iteritems方法的作用大致相同，但是会返回一个迭代器对象而不是列表
it = d.__iter__()
print(it)
##Convert the iterator to a list
print(list(it))

