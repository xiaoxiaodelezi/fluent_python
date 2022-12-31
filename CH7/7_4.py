# 一个函数，读取一个局部变量和全局变量


def f1(a):
    print(a)
    #b没有全局变量，也没有局部变量的赋值
    # print(b) #name 'b' is not defined


print(f1(3))