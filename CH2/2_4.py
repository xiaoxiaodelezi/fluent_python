#使用列表推导计算笛卡尔积

colors=['black','white']
sizes=['S','M',"L"]

tshirts=[(color,size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color,size))

#for循环的顺序改变会改变列表中的值的排列顺序
tshirts=[(color,size) for size in sizes for color in colors]
print(tshirts)