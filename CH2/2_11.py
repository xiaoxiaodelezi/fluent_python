#纯文本文件形式的收据以一行字符串的形式被解析

invoice = '''
0.....6.................................40.........52...55.......
1909  Pimoroni Pibrella                 $17.50      3    $52.50
'''

SKU = slice(0, 6)
DESCRIPITION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split('\n')[2:]
for item in line_items:
    #注意UNIT_PRICE作为切片位置参数时的定义slice(起始位置，终止位置)
    print(item[UNIT_PRICE], item[DESCRIPITION])
