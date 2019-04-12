##update可以利用一个字典项更新另外一个字典

d= {
    'title':'Pyhton Web Site',
    'url':'http://www.python.org',
    'changed':'Mar 14 22:09:15 MET 2008'
}

x = {'title':'Python Language WebSite'}
d.update(x)
print(d)
##update方法可以使用与调用dict函数（或者类型构造函数）同样的方式进行调用，这就意味着update可以和映射、拥有（键、值）
##对的队列（或者其他可迭代的对象）以及关键参数一起调用