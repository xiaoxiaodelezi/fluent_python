# 反汇编示例7-4的f1函数
from dis import dis


def f1(a):
    print(a)
    print(b)


print(dis(f1))