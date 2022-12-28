# 把字节序列解码成字符串：成功和错误处理

octets = b'Montr\xe9al'

print(octets.decode('cp1252'))

print(octets.decode('iso8859_7'))

print(octets.decode('koi8_r'))

# print(octets.decode('utf_8'))
# Traceback (most recent call last):
#   File "C:\Users\xiaole\Desktop\Fluent Python\CH4\4_7.py", line 11, in <module>
#     print(octets.decode('utf_8'))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte

print(octets.decode('utf_8', errors='replace'))
