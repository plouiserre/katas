from PokerHands.card import CardValue
from PokerHands.Figure import FullFigure

class FullDetector : 
    def __init__(self, counting_cards):
        self.counting_cards = counting_cards
        self.card_two_times = CardValue.UNDEFINED
        self.card_three_times = CardValue.UNDEFINED

    def find_full(self, hand): 
        cards_sorted = self.counting_cards.Count(hand)
        for card in cards_sorted :
            number_cards = cards_sorted[card]
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