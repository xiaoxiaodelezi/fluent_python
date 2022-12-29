# 通过函数的别名使用函数，再把函数作为参数传递


def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

print(fact)

print(fact(5))

print(map(factorial, range(11)))

print(list(map(factorial, range(11))))
