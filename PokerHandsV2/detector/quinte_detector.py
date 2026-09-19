from PokerHandsV2.card import Card, CardValue
from PokerHandsV2.AllFigures.QuinteFigure import QuinteFigure
from PokerHandsV2.manipulating_cards import SortedType
from typing import Iterator

class QuinteDetector : 
    def __init__(self, manipulating_cards):
        self.manipulating_cards = manipulating_cards
        self.high_card_value = CardValue.TWO
        self.is_ace_present = False
        self.is_card_two_present = False
        self.is_card_king_present = False

    def find_quinte(self, hand: Iterator[Card]) -> QuinteFigure:
        all_quintes_figure = []
        if len(hand) >= 5 :
            all_cards_sorted = self.manipulating_cards.sorted_card(hand, 5, SortedType.KEEP_ONE_DOUBLON)            
            all_quintes_figure = self.__find_quinte_from_sorted_cards(all_cards_sorted)
            return self.__find_best_quinte(all_quintes_figure)            
        else : 
            return None         

    def __find_quinte_from_sorted_cards (self, all_cards_sorted):
        all_quintes_figure = []
        for cards_sorted in all_cards_sorted:
            all_possible_quintes = self.__determine_all_possible_quintes(cards_sorted)
            if all_possible_quintes == None : 
                continue
            for possible_quinte in all_possible_quintes : 
                quinte_figure = self.__determinate_quinte_figure(possible_quinte)
                if quinte_figure != None : 
                    all_quintes_figure.append(quinte_figure)
                else : 
                    continue
        return all_quintes_figure
        
    def __determine_all_possible_quintes(self, cards_sorted):
        if len(cards_sorted) == 5 :
            return [cards_sorted]
        elif len(cards_sorted) == 6 : 
            return [cards_sorted[1 :6], cards_sorted]
        elif len(cards_sorted) == 7 : 
            return [cards_sorted[2 :], cards_sorted[1 :6], cards_sorted[0 :5]]            

    def __determinate_quinte_figure(self, cards_sorted):        
        if len(cards_sorted) >= 5 :
            is_sorted_cards_is_ok = self.__analyse_sorted_cards(cards_sorted)
            if is_sorted_cards_is_ok == False : 
                return None
            elif self.is_ace_present == False or (self.is_ace_present and self.is_card_two_present): 
                return QuinteFigure(self.high_card_value)
            elif self.is_ace_present and self.is_card_king_present : 
                return QuinteFigure(CardValue.ACE)
            else :
                return None
        else : 
            return None

    def __analyse_sorted_cards(self, cards_sorted):
        is_sorted_cards_is_ok = True
        last_value = CardValue.UNDEFINED
        self.__init_all_identification_cards()
        for card in cards_sorted :
            if card.value == CardValue.ACE :
                self.is_ace_present = True
                continue 
            elif card.value == CardValue.KING : 
                self.is_card_king_present = True
            elif card.value == CardValue.TWO : 
                self.is_card_two_present = True
            self.high_card_value = card.value
            if last_value != CardValue.UNDEFINED : 
                if card.value - last_value > 1 : 
                    is_sorted_cards_is_ok = False
            last_value = card.value
        return is_sorted_cards_is_ok

    def __init_all_identification_cards(self):
        self.is_ace_present = False
        self.is_card_two_present = False
        self.is_card_king_present = False

    def __find_best_quinte(self, all_quintes_figure):
        if len(all_quintes_figure) == 1 :
            return all_quintes_figure[0]
        else : 
            best_quinte = None 
            high_card = None 
            for quinte_figure in all_quintes_figure:
                if high_card == None or high_card < quinte_figure.high_card : 
                    best_quinte = quinte_figure
            return best_quinte