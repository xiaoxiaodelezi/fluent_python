#内置类型dict的init和update方法会忽略我们覆盖的setitem方法
class DoppelDict(dict):

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three=3)
print(dd)