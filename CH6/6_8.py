# 内省单独的promotions模块，构建promos列表

promos = [
    func for name, func in inspect.getmembers(promotions, inspect.isfunction)
]


def best_promo(order):
    """选择最佳折扣
    """
    return (max(promo(order) for promo in promos))