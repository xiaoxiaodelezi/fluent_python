# 运行时打印消息的生成器函数


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


for c in gen_AB():
    print('-->', c)
