from PokerHandsV2.card import Card, CardValue
from PokerHandsV2.AllFigures.StraitFigure import StraitFigure
from typing import Iterator

class QuinteDetector : 
    def __init__(self, manipulating_cards):
        self.manipulating_cards = manipulating_cards
        self.high_card_value = CardValue.TWO
        self.is_ace_present = False

    def find_quinte(self, hand: Iterator[Card]) -> StraitFigure:
        cards_sorted = self.manipulating_cards.sorted_card(hand)
        is_card_two_present = False
        is_card_king_present = False
        if len(cards_sorted) == 5 :
            last_value = CardValue.UNDEFINED
            for card in cards_sorted :
                if card.value == CardValue.ACE :
                    self.is_ace_present = True
                    continue 
                elif card.value == CardValue.KING : 
                    is_card_king_present = True
                elif card.value == CardValue.TWO : 
                    is_card_two_present = True
                self.high_card_value = card.value
                if last_value != CardValue.UNDEFINED : 
                    if card.value - last_value > 1 : 
                        return None
                last_value = card.value
            if self.is_ace_present == False or (self.is_ace_present and is_card_two_present): 
                return StraitFigure(self.high_card_value)
            elif self.is_ace_present and is_card_king_present : 
                return StraitFigure(CardValue.ACE)
            else :
                return None
        else : 
            return None