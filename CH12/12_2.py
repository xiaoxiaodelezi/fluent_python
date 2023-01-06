#dict.update 方法会忽略AnswerDict.getitem方法
class AnswerDict(dict):

    def __getitem__(self, key):
        return 42


ad = AnswerDict(a='foo')
print(ad['a'])
d = {}
d.update(ad)
print(d['a'])
print(d)