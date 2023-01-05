# 定义getitem方法，只实现序列协议的一部分，这样足够访问元素，迭代和使用in运算符了


class Foo:

    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


f = Foo()
print(f[1])
for i in f:
    print(i)

print(20 in f)
print(15 in f)