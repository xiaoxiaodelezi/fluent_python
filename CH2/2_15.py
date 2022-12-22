#没人料到的结果：t[2]被改动，但也有异常

t = (1, 2, [30, 40])
t[2] += [50, 60]
print(t)

'''
编译器中运行有些区别
实际是抛出异常，但t中的列表值确实修改了
>>> t=(1,2,[10,20])
>>> t[2]+=[30,40]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [10, 20, 30, 40])
'''