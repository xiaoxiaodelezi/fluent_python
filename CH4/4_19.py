# 使用locale.strxfrm函数做排序键

import locale

print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8'))

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']

sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)
