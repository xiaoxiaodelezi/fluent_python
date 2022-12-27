# 当有非字符串的键被查找的时候
# 如果在该键不存在的情况下，把它转换为字符串的
# 没有导入Raspberry Pi的库，所以无法使用例子中的StrKeyDict0类
# StrKeyDict 这个类的实例接受字符串和整数，自动比对key
# 但没有的key会报错

# Test for item retrieval using `d[key]` notation:
d = {
    '2': 'two',
    '4': 'four',
}

print(d['2'])
# print(d[4])   报错
# print(d[1])   报错

#Tests for item retrieval using `d.get(key)` notation:
print(d.get('2'))
# print(d.get(4))   报错
# print(d.get(1,'N/A')) 报错

# Tests for the `in` operator:
print('2' in d)
print(2 in d)