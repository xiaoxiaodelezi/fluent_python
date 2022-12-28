# 编码成字节序列：成功和错误的处理

city = 'São Paulo'

print(city.encode('utf_8'))

print(city.encode('utf_16'))

print(city.encode('iso8859_1'))

# print(city.encode('cp437'))
# Traceback (most recent call last):
#   File "C:\Users\xiaole\Desktop\Fluent Python\CH4\4_6.py", line 10, in <module>
#     print(city.encode('cp437'))
#   File "C:\Users\xiaole\AppData\Local\Programs\Python\Python39\lib\encodings\cp437.py", line 12, in encode
#     return codecs.charmap_encode(input,errors,encoding_map)
# UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>

print(city.encode('cp437', errors='ignore'))

print(city.encode('cp437', errors='replace'))

print(city.encode('cp437', errors='xmlcharrefreplace'))
