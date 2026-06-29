from PokerHands.card import Card
from typing import Iterator

class CountingCards :
    def __init__(self):
        pass

    def Count(self, hand : Iterator[Card]):
        counting_cards = {}
        for card in hand : 
            if card.value in counting_cards : 
                counting_cards[card.value] += 1
            else : 
                counting_cards[card.value] = 1
        return counting_cards