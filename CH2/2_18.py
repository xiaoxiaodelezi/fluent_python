# 根据一个分数，找到它所对应的成绩
import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
