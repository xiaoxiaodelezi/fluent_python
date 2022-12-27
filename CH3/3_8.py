# 无论是添加、更新还是查询操作，StrKeyDict都会把非字符串的键转换为字符串

import collections


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        #不能写 in self，一定要有data
        return str(key) in self.data

    def __setitem__(self, key, item):
        #不能写self[str(key)]
        self.data[str(key)] = item


skd = StrKeyDict()
skd[1] = 20
print(1 in skd)
print('1' in skd)
print(2 in skd)
print(skd)
print(skd.data)
print(skd == skd.data)
