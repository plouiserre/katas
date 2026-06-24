from PokerHands.card import CardValue
from PokerHands.AllFigures.PairFigure import PairFigure

class PairDetector : 
    def __init__(self, counting_cards):
        self.counting_cards = counting_cards

    def find_pair(self, hand):
        cards_sorted = self.counting_cards.Count(hand)
        is_one_pair = False
        value_pair = CardValue.TWO
        high_value_outside_one_pair = CardValue.TWO
        for card in cards_sorted : 
            number_cards = cards_sorted[card]
            if number_cards == 2 : 
                is_one_pair = True
                value_pair = card                
            else : 
                if card > high_value_outside_one_pair : 
                    high_value_outside_one_pair = card
        if is_one_pair : 
            return PairFigure(value_pair, high_value_outside_one_pair)