#一个简单的二维向量类
#__repr__,__abs__,__add__,__mul__

from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return "Vector_repr(%r, %r)" % (self.x,self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self,other):
        x=self.x + other.x
        y=self.y + other.y
        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x * scalar,self.y * scalar)

    
p=Vector(1,1)
q=Vector(2,2)

#repr调用可以以repr定义的方式来显示Vector的一个实例
print(p)

print(abs(p))

print(bool(p))

#add的调用方法
print(p+q)

#mul的调用方法
print(q*3)