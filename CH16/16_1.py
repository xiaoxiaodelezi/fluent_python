#可能是协程最简单的使用演示
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)


my_coro = simple_coroutine()
print(my_coro)
next(my_coro)
my_coro.send(42)