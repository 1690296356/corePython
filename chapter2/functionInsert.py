numbers = [1,2,3,4,5,6,7]
numbers.insert(3, 'four')
print(numbers)

numbers[3:3] = ['four']
print(numbers)

#pop方法会移除列表中的一个元素（默认是最后一个），并且返回该元素的值
x = [1,2,3]
print(x.pop())
print(x)

print(x.pop(0))

print(x)
#pop方法是唯一一个既能修改列表又返回元素值（除了None）的列表方法 