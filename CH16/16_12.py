# 使用try finally块在协程终止时执行操作


class DemoException(Exception):
    pass


def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received : {!r}'.format(x))
    finally:
        print('-> coroutine ending')
