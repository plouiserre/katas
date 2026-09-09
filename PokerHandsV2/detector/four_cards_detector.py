from PokerHandsV2.card import Card, CardValue
from PokerHandsV2.AllFigures.FourOfKindFigure import FourOfKindFigure

from typing import Iterator

class FourCardsDetector: 
    def __init__(self, manipulating_cards):
        self.manipulating_cards = manipulating_cards
        self.card_four_times = CardValue.UNDEFINED
        self.high_card_value = CardValue.UNDEFINED    

    def find_four_cards(self,  hand: Iterator[Card]) -> FourOfKindFigure:
        cards_sorted = self.manipulating_cards.Count(hand)
        for card in cards_sorted : 
            number_cards = cards_sorted[card]
            if number_cards == 4 :
                self.card_four_times = card
            else :
                self.high_card_value = card
        if self.card_four_times != CardValue.UNDEFINED :
            return FourOfKindFigure(self.card_four_times, self.high_card_value)
        else : 
            return None