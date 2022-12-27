# needles的元素在haystack里出现的次数（迭代）

found = 0

needles = set([12, 3, 4, 5])
haystack = set([12, 4, 10, 1])

#迭代不一定需要set
for n in needles:
    if n in haystack:
        found += 1

print(found)