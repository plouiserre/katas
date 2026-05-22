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
        number_pair = 0
        number_three_of_kind = 0
        is_straight = self.__detect_straight(cards_sorted)
        if is_straight == False : 
            for card in cards_sorted : 
                number_cards = cards_sorted[card]
                if number_cards == 2 : 
                    number_pair += 1
                elif number_cards == 3 : 
                    number_three_of_kind += 1
            if number_pair == 1 : 
                high_figure = HighFigure.PAIR
            elif number_pair == 2 :
                high_figure = HighFigure.TWO_PAIRS
            elif number_three_of_kind == 1: 
                high_figure = HighFigure.THREE_OF_A_KIND
        else : 
            high_figure = HighFigure.STRAIGHT
        return high_figure
    
    def __detect_straight(self, cards_sorted) : 
        cards_ordered = dict(sorted(cards_sorted.items()))
        if len(cards_ordered) == 5 :
            #mettre les clés par ordre 
            is_straight = True
            last_value = 0
            for card in cards_ordered : 
                if last_value != 0 : 
                    if card.value - last_value > 1 : 
                        is_straight = False
                        break
                last_value = card.value
            return is_straight
        else : 
            return False
    
    def find_more_presents_cards(self, cards_sorted) : 
        card_max_times = 0
        card_most_present = CardValue.ACE
        for card in cards_sorted: 
            if card_max_times < cards_sorted[card] : 
                card_max_times = cards_sorted[card]
                card_most_present = card
            elif card_max_times == cards_sorted[card] and card_most_present.value < card.value : 
                card_max_times = cards_sorted[card]
                card_most_present = card
        return card_most_present


class HighFigure(Enum) : 
    HIGH_VALUE = 1
    PAIR = 2
    TWO_PAIRS = 3    
    THREE_OF_A_KIND = 4
    STRAIGHT = 5