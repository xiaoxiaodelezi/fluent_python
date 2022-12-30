# 内省模块的全局命名空间，构建promos列表

promos = [
    globals()[name] for name in globals()
    if name.endswith('_promo') and name != 'best_promo'
]


def best_promo(order):
    """选择最佳折扣
    """
    return (max(promo(order) for promo in promos))
