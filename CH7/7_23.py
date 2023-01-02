# 为了接受参数，新的register装饰器必须作为函数调用

registry = set()


def register(active=True):

    def decorate(func):
        print('running register(avtive=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')