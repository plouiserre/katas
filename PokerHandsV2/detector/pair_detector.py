from PokerHandsV2.card import Card, CardValue
from PokerHandsV2.AllFigures.PairFigure import PairFigure

from typing import Iterator

class PairDetector : 
    def __init__(self, manipulating_cards):
        self.manipulating_cards = manipulating_cards

    def find_pair(self, hand: Iterator[Card]) -> PairFigure:
        cards_group_by_value = self.manipulating_cards.count_cards(hand)
        is_one_pair = False
        value_pair = CardValue.TWO
        high_value_outside_one_pair = CardValue.TWO
        for card in cards_group_by_value : 
            number_cards = cards_group_by_value[card]
            if number_cards == 2 : 
                is_one_pair = True
                value_pair = card                
            else : 
                if card > high_value_outside_one_pair : 
                    high_value_outside_one_pair = card
        if is_one_pair : 
            return PairFigure(value_pair, high_value_outside_one_pair)