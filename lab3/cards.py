#!/usr/bin/env python3

import itertools
from enum import Enum
import random

_ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# or  ranks = list(range(6, 10 + 1)) + list('JQKA')
_suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}


class SuitEnum(Enum):

    def __str__(cls):
        return cls.value


Suit = SuitEnum('Suit', _suits)


class Card:
    __slots__ = 'rank', 'suit'  # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


## ranks = [6, 7, 8, 9, 10]
## suits = ['clubs', 'spades', 'hearts', 'diamonds']
## itertools.product(ranks, suits)
# equivalent to:
##for r in ranks:
##    for s in suits:
##        print(f'{r} : {s}')


class CardDeck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in _ranks for suit in Suit]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n):
        if n <= 0:
            raise ValueError("Number of cards to draw must be positive.")
        if n > len(self.cards):
            raise ValueError("Not enough cards in the deck.")

        drawn_cards = self.cards[:n]
        self.cards = self.cards[n:]

        return drawn_cards

