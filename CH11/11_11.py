# 不符合Tombola要求的子类无法蒙混过关
import abc


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        pass

    @abc.abstractmethod
    def pick(self):
        pass

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class Fake(Tombola):

    def pick(self):
        return 13


print(Fake)
f = Fake()
#TypeError: Can't instantiate abstract class Fake with abstract method load
