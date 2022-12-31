# 测试示例7-9


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))