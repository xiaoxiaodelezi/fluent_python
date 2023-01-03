#弱引用是可调用的对象，返回的是被引用的对象；如果所指对象不存在，返回None

import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
wref()
print(wref() is None)
print(wref() is None)
