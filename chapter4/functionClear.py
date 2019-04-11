
##clear 方法清除字典中的所有项。这是个原地操作（类似于list.sort）,所以无返回值（或者说返回None）
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)

return_value = d.clear()
print(d)

print(return_value)

##第一种
print("##第一种##")
x={}
y=x
x['key'] = 'value'
print(y)
x = {}
print(y)

##第二种
print("##第二种##")
x = {}
y = x
x['key'] = 'value'
print(y)
x.clear()
print(y)

##x和y最初对应同一个字典，情况1中，我通过将x关联到一个新的空字典来"清空"它，这对y一点影响也没有，它还关联到原先的字典。
##但是如果真的想清空原始字典中的所有元素，必须使用clear方法。正如情况2中看到的，y随后也被清空了
