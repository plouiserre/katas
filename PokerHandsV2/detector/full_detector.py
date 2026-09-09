from PokerHandsV2.card import Card, CardValue
from PokerHandsV2.AllFigures.FullFigure import FullFigure

from typing import Iterator

class FullDetector : 
    def __init__(self, manipulating_cards):
        self.manipulating_cards = manipulating_cards
        self.card_two_times = CardValue.UNDEFINED
        self.card_three_times = CardValue.UNDEFINED

    def find_full(self, hand: Iterator[Card]) -> FullFigure: 
        self.__init_count_cards()
        cards_group_by_value = self.manipulating_cards.Count(hand)
        for card in cards_group_by_value :
            number_cards = cards_group_by_value[card]
            if number_cards == 3 : 
                self.card_three_times = card
            elif number_cards == 2 : 
                self.card_two_times = card
            else : 
                break
        if self.card_two_times != CardValue.UNDEFINED and self.card_three_times != CardValue.UNDEFINED : 
            return FullFigure(self.card_two_times, self.card_three_times)
        else : 
            return None

    def __init_count_cards(self): 
        self.card_two_times = CardValue.UNDEFINED
        self.card_three_times = CardValue.UNDEFINED