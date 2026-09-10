from PokerHandsV2.card import Card, CardColor, CardValue
from PokerHandsV2.AllFigures.QuinteFlushFigure import QuinteFlushFigure

from typing import Iterator

class QuinteFlushDetector : 
    def __init__(self, manipulating_cards, quinte_detector):
        self.manipulating_cards = manipulating_cards 
        self.quinte_detector = quinte_detector

    def find_quinte_flush(self, hand: Iterator[Card]) -> QuinteFlushFigure:
        quinte_figure = self.quinte_detector.find_quinte(hand)
        card_color = CardColor.UNDEFINED
        is_same_color = True
        if quinte_figure != None : 
            card_color = self.__get_color_from_card_value(hand, quinte_figure.value)
            for card in hand :
                is_same_color = self.__determine_is_same_color_is_ok_for_this_card(quinte_figure.value, card, card_color)
                if is_same_color == False : 
                    break
            if is_same_color : 
                return QuinteFlushFigure(quinte_figure.value, card_color)
            else : 
                return None
        else :
            return None

    def __determine_is_same_color_is_ok_for_this_card(self, quinte_figure_value, card, card_color):
        is_same_color = True
        difference_card_value = quinte_figure_value - card.value
        if difference_card_value < 4 and difference_card_value > 0 and card.color != card_color : 
            is_same_color = False
        return is_same_color
        
    def __get_color_from_card_value(self, hand, card_value):
        card_color = CardColor.UNDEFINED
        for card in hand :
            if card.value == card_value.value : 
                card_color = card.color
                break
        return card_color

    