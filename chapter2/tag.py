#分片操作的实现需要提供两个索引作为边界，第1个索引的元素是包含在分片内的，第2个则不包含在分片内
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])

print(tag[32:-4])

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[3:6])
print(numbers[0:1])

print(numbers[7:10])
print(numbers[-3:-1])
print(numbers[-3:0])

#如果分片所得部分包括序列结尾的元素，那么，只需置空最后一个索引
print(numbers[-3:])
print(numbers[:3])

print(numbers[:])
print(numbers[0:10:1])

print(numbers[0:10:2])

print(numbers[3:6:3])

print(numbers[::4])

#当然，步长不能为0(那不会执行)，但步长可以是负数，此时分片从右至左提取元素
print(numbers[8:3:-1])


print(numbers[10:0:-2])

print(numbers[::-2])

print(numbers[5::-2])

print(numbers[:5:-2])

array1 = [1,2,3]
array2 = [4,5,6]
print(array1+array2)

print('Hello.'+'  world!')

#print(array1+ ' world!')

#用数字x乘以一个序列会生成新的序列，而在新的序列中，原来的系列将被重复x次
print('python'*5)

array3 = [42]
print(array3*10)

sequence = [None]*10
print(sequence)






