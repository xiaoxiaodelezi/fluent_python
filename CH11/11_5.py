# random.shuffle函数不能打乱FrenchDeck实例

import collections

from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


from random import shuffle

deck = FrenchDeck()
shuffle(deck)
'''
  File "C:\Users\xiaole\Desktop\Fluent Python\CH11\11_5.py", line 29, in <module>
    shuffle(deck)
  File "C:\Users\xiaole\AppData\Local\Programs\Python\Python39\lib\random.py", line 362, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'FrenchDeck' object does not support item assignment
'''