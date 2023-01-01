# 计算移动平均值的高阶函数，不保存所有历史数据，使用nonlocal修正


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager