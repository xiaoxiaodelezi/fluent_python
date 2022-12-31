# 审查make_averager创建的函数


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)