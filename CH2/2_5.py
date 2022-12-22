#用生成器表达初始化元组和数组

symbols = '&$%*HK123'
#返回一个生成器
print(ord(symbol) for symbol in symbols)
#通过转为tuple形式，打印所有的值
print(tuple(ord(symbol) for symbol in symbols))

import array
#ord前面的括号不能省略
print(array.array("I", (ord(symbol) for symbol in symbols)))
