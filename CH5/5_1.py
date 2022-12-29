#创建并测试一个函数，然后读取它的__doc__属性，再检查它的类型


def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))

print(factorial.__doc__)

print(type(factorial))