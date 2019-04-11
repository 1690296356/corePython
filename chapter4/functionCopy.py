##copy方法返回一个具有相同键-值对的新字典（这个方法实现的是浅复制（shallow copy），因为值本身就是相同的，而不是副本）
x = {'username':'admin','machines':{'foo','bar','baz'}}

y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')

print(y)

print(x)
##在副本中替换值的时候，原始字典不受影响，但是，如果修改了某个值（原地修改，而不是替换），原始的字典也会修改，因为同样的值也存储在原字典中

##避免这个问题的一种方法就是使用深复制（deep copy），复制其包含的所有值。可以使用copy模块的deepcopy函数来完成操作：
from copy import deepcopy

d={}
d['name'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('Clive')
print(c)
print(dc)

