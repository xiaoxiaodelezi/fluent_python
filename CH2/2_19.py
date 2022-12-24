# insort可以保持有序序列的顺序

import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    #insort(原列表，添加的新元素) 将元素插入原列表，并使得列表有序
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
