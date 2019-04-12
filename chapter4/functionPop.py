 ##pop方法用来获取对应给定键的值，然后将这个键-值对从字典中移除
d = {'x':1,'y':2}
print(d.pop('x'))
print(d)

##popitem方法类似于list.pop,后者会弹出列表的最后一个元素。但不同的是，popitem弹出随机的项，因为字典并没有“最后的元素”
##或者其他有关顺序的概念，若想一个接一个地移除并处理项，这个方法非常有效（因为不用首先获取键的列表）。

d = {'title':'Python Web Site','url':'http://www.python.org','span':0}
print(d)
d.popitem()
print(d)