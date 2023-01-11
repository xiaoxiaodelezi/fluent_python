# 使用16_5中定义的@coroutine装饰器定义并测试计算移动平均值的协程

from functools import wraps


def coroutine(func):

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
