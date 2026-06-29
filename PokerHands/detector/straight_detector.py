from PokerHands.card import Card, CardValue
from PokerHands.AllFigures.StraitFigure import StraitFigure
from typing import Iterator

class StraightDetector : 
    def __init__(self, counting_cards):
        self.counting_cards = counting_cards
        self.high_card_value = CardValue.TWO
        self.is_ace_present = False

    def find_straight(self, hand: Iterator[Card]) -> StraitFigure:
        cards_sorted = self.counting_cards.Count(hand)
        cards_ordered = dict(sorted(cards_sorted.items())) 
        if len(cards_ordered) == 5 :
            last_value = CardValue.UNDEFINED
            for card in cards_ordered :
                if card.value == CardValue.ACE :
                    self.is_ace_present = True
                    continue 
                self.high_card_value = card
                if last_value != CardValue.UNDEFINED : 
                    if card.value - last_value > 1 : 
                        return None
                last_value = card.value
            if self.is_ace_present == False or (self.is_ace_present and CardValue.TWO in cards_ordered): 
                return StraitFigure(self.high_card_value)
            elif self.is_ace_present and CardValue.KING in cards_ordered : 
                return StraitFigure(CardValue.ACE)
            else :
                return None
        else : 
            return None