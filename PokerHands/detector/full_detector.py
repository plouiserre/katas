from PokerHands.card import Card, CardValue
from PokerHands.AllFigures.FullFigure import FullFigure

from typing import Iterator

class FullDetector : 
    def __init__(self, manipulating_cards):
        self.manipulating_cards = manipulating_cards
        self.card_two_times = CardValue.UNDEFINED
        self.card_three_times = CardValue.UNDEFINED
        self.all_cards_three_times = []
        self.all_cards_two_times = []

    def find_full(self, hand: Iterator[Card]) -> FullFigure: 
        self.__init_count_cards()
        cards_group_by_value = self.manipulating_cards.count_cards(hand)
        for card in cards_group_by_value :
            number_cards = cards_group_by_value[card]
            if number_cards == 3 : 
                self.all_cards_three_times.append(card)
            elif number_cards == 2 : 
                self.all_cards_two_times.append(card)
        if len(self.all_cards_three_times) == 1 and len(self.all_cards_two_times) == 1 : 
            return FullFigure(self.all_cards_two_times[0], self.all_cards_three_times[0])
        elif len(self.all_cards_three_times ) == 2 : 
            first_choice = self.all_cards_three_times[0]
            second_choice = self.all_cards_three_times[1]
            if first_choice < second_choice : 
                return FullFigure(first_choice, second_choice)
            else : 
                return FullFigure(second_choice, first_choice)
        else : 
            return None

    def __init_count_cards(self): 
        self.card_two_times = CardValue.UNDEFINED
        self.card_three_times = CardValue.UNDEFINED
        self.all_cards_three_times = []
        self.all_cards_two_times = []