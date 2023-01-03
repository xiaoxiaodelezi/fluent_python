# 字符串字面量可能会创建共享的对象

t1 = (1, 2, 3)
t3 = (1, 2, 3)
print(t3 is t1)

s1 = 'ABC'
s2 = 'ABC'
print(s2 is s1)
