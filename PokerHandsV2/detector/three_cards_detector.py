from PokerHandsV2.card import Card, CardValue
from PokerHandsV2.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure

from typing import Iterator

class ThreeCardsDetector: 
    def __init__(self, manipulating_cards):
        self.manipulating_cards = manipulating_cards

    def find_three_of_kind(self, hand : Iterator[Card]) -> ThreeOfKindFigure:
        cards_group_by_value = self.manipulating_cards.count_cards(hand)
        is_three_cards = False
        three_of_kind_value = CardValue.TWO
        high_value_outside_three_of_kind = CardValue.TWO
        for card in cards_group_by_value : 
            number_cards = cards_group_by_value[card]
            if number_cards == 3 : 
                is_three_cards = True
                three_of_kind_value = card
            else : 
                if card > high_value_outside_three_of_kind : 
                    high_value_outside_three_of_kind = card
        if is_three_cards : 
            return ThreeOfKindFigure(three_of_kind_value, high_value_outside_three_of_kind)
        else : 
            return None