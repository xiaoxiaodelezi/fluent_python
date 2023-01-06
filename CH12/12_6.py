# 使用super()函数调用ping方法
class A:

    def ping(self):
        print('ping', self)


class B(A):

    def pong(self):
        print("pong:", self)


class C(A):

    def pong(self):
        print('Pong:', self)


class D(B, C):

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()
d.ping()
