from math import pi

#字段宽 10
print('%10f' %pi)

#字段宽 10， 精度 2
print('%10.2f' %pi)

#精度 5
print('%.5s' % 'Guido van Rossum')

#可以使用*（星号）作为字段宽度或者精度（或者两者都使用*），此时数值会从元组参数中读出
print('%.*s' % (5,'Guido van Rossum'))