# 用MappingProxyType 来获取字典的只读实例mappingproxy

from types import MappingProxyType

d = {1: 'A'}

d_proxy = MappingProxyType(d)

print(d_proxy)

print(d_proxy[1])

# 返回错误
# print(d_proxy[2])

d[2] = 'B'

print(d_proxy)

print(d_proxy[2])