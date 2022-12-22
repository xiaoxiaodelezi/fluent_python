#一摞Python风格的纸牌
# __getitem__和__len__两个特殊方法的介绍

import collections

from random import choice

# namedtuple的使用
# 返回一个元组的子类，其中包含字段名
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    # 自定义len属性
    def __len__(self):
        return len(self._cards)

    # 自定义getitem方法
    def __getitem__(self, position):
        return self._cards[position]


#初始化一个Card实例
beer_card = Card('7', 'diamonds')
print(beer_card)

#初始化一个FrenchDeck实例
deck = FrenchDeck()
#测试len方法
print(len(deck))
#测试getitem方法
print(deck[0])
print(deck[-1])

#random.choice
#可以随机返回一组数据中的一个值
print(choice(deck))
print(choice(deck))
print(choice(deck))

#getitem支持切片
print(deck[:3])
print(deck[12:13])

#getitem支持迭代
for card in deck:
    print(card)
#也支持反向迭代
for card in reversed(deck):
    print(card)

#如果一个集合没有支持__contains__方法
#对于in的运算会按照顺序迭代搜索
print(Card('Q', 'hearts') in deck)
print(Card('7', 'bearts') in deck)

#排序操作
#设定每个花色的分值
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


#定义排序规则
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# sorted方法，key参数为排序规则，排序deck
for card in sorted(deck, key=spades_high):
    print(card)