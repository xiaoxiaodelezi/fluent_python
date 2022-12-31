# 装饰器通常把函数替换成另一个函数


def deco(func):

    def inner():
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


target()
print(target)