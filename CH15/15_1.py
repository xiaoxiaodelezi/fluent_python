# 演示把文件对象当成上下文管理器使用

with open('mirror.py') as fp:
    src = fp.read

print(len(src))
print(fp)
print(fp.closed, fp.encoding)
#fp.read(60)