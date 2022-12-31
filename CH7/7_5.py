# b是局部变量，因为函数在定义中给他赋值了

b = 6


def f2(a):
    print(a)
    print(b)
    # 因为b在函数中被赋值了，只是这个赋值晚于调用
    # b = 9 #local variable 'b' referenced before assignment


f2(3)

b = 6


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


f3(3)
print(b)