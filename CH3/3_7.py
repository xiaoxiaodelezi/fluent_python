# 在查询的时候把非字符串的键转换为字符串


class StrKeyDict(dict):

    #当找不到键时会调用missing
    def __missing__(self, key):
        #如果找不到的键本身就是str，那么久返回键错误
        if isinstance(key, str):
            raise KeyError(key)
        #如果键不是str，那么转为str再查找
        #这里可能会再次调用missing
        return self[str(key)]

    #get方法吧slef[key]的形式委托给getitem，可以通过missing有个补救机会

    def get(self, key, default=None):
        try:
            #这里有个隐式调用__getitem__
            #只有__missing__出问题了，才会有后面的keyerror
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        #整数和对应字符串各查找一次
        return key in self.keys() or str(key) in self.keys()