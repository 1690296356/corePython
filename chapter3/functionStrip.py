#strip方法返回去除两侧（不包括内部）空格的字符串

print('         internal whitespace is kept        '.strip( ))

names = ['gumby', 'smith', 'jones']
name = 'gumby'
if name in names: print('Found it !')

#假设用户在输入名字时无意中在名字后面加上空格：
names = ['gumby', 'smith', 'jones']
name = 'gumby'
if name.strip() in names: print('Found it !')

#这个方法只会去除两侧的字符，所以字符串中的星号没有被去除掉
print('*** SPAM * for * everyone!!! ***'.strip(' *!'))


