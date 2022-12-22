# 用列表推导和map/filter组合来创建同样的表单

symbols = "$^&*%^*"

beyond_ascii = [ord(s) for s in symbols if ord(s) > 50]
print(beyond_ascii)

#map(function, iterable, ...)
#filter(function, iterable)
beyond_ascii = list(filter(lambda c: c > 50, map(ord, symbols)))
print(beyond_ascii)
