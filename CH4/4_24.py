# 使用surrogateescape 错误处理方式

import os

print(os.listdir('.'))
print(os.listdir(b'.'))

pi_name_bytes = b'digits-of-\xcf\x80.txt'
pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
print(pi_name_str)
print(pi_name_str.encode('ascii', 'surrogateescape'))
