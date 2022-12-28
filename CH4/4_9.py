# 一个平台上的编码问题（可能发生，也可能不发生）

print(open('cafe.txt', 'w', encoding='utf_8').write('café'))

print(open('cafe.txt').read())