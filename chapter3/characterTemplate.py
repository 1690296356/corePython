#string模块提供另外一个格式化值的方法:模块字符串。他的工作方式类似于很多UNIX Shell
#里的变量替换。如下所示，substitute这个模块方法会用传递过来的关键字参数foo替换字符串中的$foo
from string import Template
s = Template('$x. glorious $x!')
print(s.substitute(x='slurm'))

#如果替换字段是单词的一部分，那么参数名就必须用括号括起来，从而准确指明结尾：
s = Template("It's ${x} tastic!")
print(s.substitute(x='slurm'))

#可以使用$$插入美元符号：
s = Template("Make $$ selling $x!")
print(s.substitute(x='slurm'))

#除了关键字参数之外，还可以使用字典变量提供值/名称对
s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print(s.substitute(d))


print('%s plus %s equals %s' % (1,1,2))