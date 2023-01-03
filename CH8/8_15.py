# 一个简单的类，说明接受可变参数的风险


class TwilightBus:
    '''让乘客销声匿迹的校车'''

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)