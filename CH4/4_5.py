#使用3个编译器编码字符串"El Niño"，得到的字节序列差异很大

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')
