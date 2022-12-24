#通过改变数组中的一个字节来更新数组里某个元素的值

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
#直接读取了内存位置连续bit
memv = memoryview(numbers)
#长度按照h所占的字节划分
print(len(memv))
#返回内存按照h所占字节划分的第一个值
print([memv[0]])
#将这段内存转为b格式
memv_oct = memv.cast('B')
#以b格式的方式输出这段内存中的值组成的一个list
print(memv_oct.tolist())
#以b格式所占字节数修改内存中的对应位置值
memv_oct[5] = 4
#原始numbers被改变了
print(numbers)
