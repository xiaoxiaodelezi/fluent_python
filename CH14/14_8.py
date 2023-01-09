# 先在列表推导中使用gen_AB生成器函数，然后生成器表达式中使用
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


res1 = [x * 3 for x in gen_AB()]
for i in res1:
    print('-->', i)

res2 = (x * 3 for x in gen_AB())
print(res2)
for i in res2:
    print('-->', i)
