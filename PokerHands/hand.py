from enum import Enum
from PokerHands.card import CardValue

class Hand :
    def __init__(self):
        self.counting_cards = {}

    def count_all_cards(self, content) : 
        self.counting_cards = {}
        for card in content : 
            if card.value in self.counting_cards : 
                self.counting_cards[card.value] += 1
            else : 
                self.counting_cards[card.value] = 1
        return self.counting_cards
    
    def determinate_high_figure(self, cards_sorted):
        high_figure = HighFigure.HIGH_VALUE
        for card in cards_sorted : 
            number_cards = cards_sorted[card]
            if number_cards == 2 : 
                high_figure = HighFigure.PAIR
            elif number_cards == 3 : 
                high_figure = HighFigure.THREE_OF_A_KIND
        return high_figure
    
    def find_more_presents_cards(self, cards_sorted) : 
        card_max_times = 0
        card_most_present = CardValue.ACE
        for card in cards_sorted: 
            if card_max_times < cards_sorted[card] : 
                card_max_times = cards_sorted[card]
                card_most_present = card
        return card_most_present


class HighFigure(Enum) : 
    HIGH_VALUE = 1
    PAIR = 2
    THREE_OF_A_KIND = 3