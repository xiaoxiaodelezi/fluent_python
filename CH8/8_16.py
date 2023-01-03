# 没有指向对象的引用时，监视对象生命结束时的情形

import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'  #'Gone with the wind...'
print(ender.alive)