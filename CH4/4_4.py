# 使用memoryview和struct查看一个GIF图像的首部

import struct

#结构体的格式:<代表小字节序，3s3s是两个3字节的序列，HH是两个16位2进制整数
fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    #读取内存成为要给memoryview对象
    img = memoryview(fp.read())

#memoryview对象的切片header，不会复制，只是切片，也是一个memoryview对象
header = img[:10]
print(bytes(header))

#拆包memoryview对象，得到一个元组，包含类型、版本、宽度、高度
print(struct.unpack(fmt, header))

#删除引用，释放memoryview占据的内存
del header
del img
