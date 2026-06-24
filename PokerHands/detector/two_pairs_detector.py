from PokerHands.card import CardValue
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure

class TwoPairsDetector: 
    def __init__(self, counting_cards):
        self.counting_cards = counting_cards

    def find_two_pairs(self, hand):
        cards_sorted = self.counting_cards.Count(hand)
        is_two_pairs = False
        first_value_pair = CardValue.TWO
        second_value_pair = CardValue.TWO
        high_value_outside_two_pair = CardValue.TWO
        number_pair = 0
        for card in cards_sorted : 
            number_cards = cards_sorted[card]
            if number_cards == 2 : 
                number_pair = number_pair + 1 
                if number_pair == 1 :
                    first_value_pair = card
                else : 
                    is_two_pairs = True
                    if card > first_value_pair : 
                        second_value_pair = first_value_pair
                        first_value_pair = card
                    else : 
                        second_value_pair = card
            else : 
                if card > high_value_outside_two_pair : 
                    high_value_outside_two_pair = card
        if is_two_pairs : 
            return TwoPairFigure(first_value_pair, second_value_pair, high_value_outside_two_pair)
        else : 
            return None