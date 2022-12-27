# 在haystack里用迭代的方法查找needles的元素，并计算找到的元素的个数

found = 0

for n in needles:
    if n in haystack:
        found += 1
