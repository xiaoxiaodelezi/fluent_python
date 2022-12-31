# 反汇编示例7-5中的f2函数
from dis import dis


def f2(a):
    print(a)
    print(b)
    b = 9


print(dis(f2))