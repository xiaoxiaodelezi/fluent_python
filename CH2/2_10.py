#具名元组的属性和方法

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
#打印City的所有字段
print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
#namedtuple的套用
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

#_make()通过接受一个可迭代对象来生成实例，相当于City(*delhi_data)
delhi = City._make(delhi_data)

#_asdict()把具名元组按照collections.OrderDict的形式返回
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)
