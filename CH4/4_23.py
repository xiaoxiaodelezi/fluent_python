#  把字符串和字节序列参数传递给listdir函数得到的结果

import os

print(os.listdir('.'))
print(os.listdir(b'.'))

# 'abc.txt', 'digits-of-π.txt'
#  b'abc.txt', b'digits-of-\xcf\x80.txt'