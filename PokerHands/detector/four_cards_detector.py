from PokerHands.card import CardValue
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure

class FourCardsDetector: 
    def __init__(self, counting_cards):
        self.counting_cards = counting_cards
        self.card_four_times = CardValue.UNDEFINED
        self.high_card_value = CardValue.UNDEFINED    

    def find_four_cards(self, hand):
        cards_sorted = self.counting_cards.Count(hand)
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