# 使用鸭子类型处理单个字符串或由字符串组成的可迭代对象

try:
    field_names = field_name.replace(',', ' ').split()
except AttributeError:
    pass
field_name = tuple(field_names)
