# 把DemoException异常传入demo_exc_handling不会导致协程终止


class DemoException(Exception):
    pass


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received : {!r}'.format(x))
    raise RuntimeError('This line should never run.')


exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException)
from inspect import getgeneratorstate

print(getgeneratorstate(exc_coro))
