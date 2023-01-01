# 计算移动平均值的高阶函数，不保存所有历史数据，但是有缺陷


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager

    # 会报错，因为count+=1 实质是count=count+1，等于在averager中又定义了count
