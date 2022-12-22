#定义和使用具名元组

from collections import namedtuple
#namedtuple('类名','字段名')
#字段名可以是由数个字符串组成的可迭代对象，或者是由空格分开的字段名组成的字符串
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])