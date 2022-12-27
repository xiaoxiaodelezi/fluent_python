# needles 的元素再haystack里出现的次数，两个变量都是set

needles = set([12, 3, 4, 5])
haystack = set([12, 4, 10, 1])
found = len(needles & haystack)

print(found)