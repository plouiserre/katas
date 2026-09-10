from PokerHandsV2.card import Card, CardValue
from PokerHandsV2.AllFigures.QuinteFigure import QuinteFigure
from typing import Iterator

class QuinteDetector : 
    def __init__(self, manipulating_cards):
        self.manipulating_cards = manipulating_cards
        self.high_card_value = CardValue.TWO
        self.is_ace_present = False

    def find_quinte(self, hand: Iterator[Card]) -> QuinteFigure:
        if len(hand) >= 5 :
            cards_sorted = self.manipulating_cards.sorted_card(hand)
            all_possible_quintes = self.__determine_all_possible_quintes(cards_sorted)
            for possible_quinte in all_possible_quintes : 
                quinte_figure = self.__determinate_quinte_figure(possible_quinte)
                if quinte_figure != None : 
                    return quinte_figure
                else : 
                    continue
        else : 
            return None 
        
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