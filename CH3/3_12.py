# needles的元素在haystack里出现的次数（迭代），两个对象可以是任意迭代对象

needles = set([12, 3, 4, 5])
haystack = set([12, 4, 10, 1])

found = len(set(needles) & set(haystack))
print(found)

#haystack不需要转为set
found = len(set(needles).intersection(haystack))
print(found)