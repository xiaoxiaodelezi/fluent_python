# FrenchDeck 类的实现和几个验证

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = 'spades diamonds clubs hearts'.split(' ')

    def __init__(self):
        self._cards = [
            Card(rank, suit) for rank in self.ranks for suit in self.suits
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


from random import choice

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(choice(deck))

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
