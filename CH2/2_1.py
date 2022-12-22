#将字符串转为unicode码位的列表

symbols = "$^&*%^*"

codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)