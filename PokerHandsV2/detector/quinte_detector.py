from PokerHandsV2.card import Card, CardValue
from PokerHandsV2.AllFigures.QuinteFigure import QuinteFigure
from PokerHandsV2.manipulating_cards import SortedType
from typing import Iterator

class QuinteDetector : 
    def __init__(self, manipulating_cards):
        self.manipulating_cards = manipulating_cards
        self.high_card_value = CardValue.TWO
        self.is_ace_present = False

    def find_quinte(self, hand: Iterator[Card]) -> QuinteFigure:
        all_quintes_figure = []
        if len(hand) >= 5 :
            all_cards_sorted = self.manipulating_cards.sorted_card(hand, 5, SortedType.KEEP_ONE_DOUBLON)
            all_quintes_figure = self.__find_quinte_from_sorted_cards(all_cards_sorted)    
        else : 
            return None 
        return self.__find_best_quinte(all_quintes_figure)

    def __find_quinte_from_sorted_cards (self, all_cards_sorted):
        all_quintes_figure = []
        for cards_sorted in all_cards_sorted:
            all_possible_quintes = self.__determine_all_possible_quintes(cards_sorted)
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
        is_card_two_present = False
        is_card_king_present = False
        if len(cards_sorted) >= 5 :
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
                return QuinteFigure(self.high_card_value)
            elif self.is_ace_present and is_card_king_present : 
                return QuinteFigure(CardValue.ACE)
            else :
                return None
        else : 
            return None

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