# 创建对象以后才会把变量分配给对象


class Gizmo:

    def __init__(self):
        print('Gizmo id:%d' % id(self))


x = Gizmo()
# y = Gizmo() * 10
print(dir())
