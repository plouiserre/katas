from PokerHands.card import Card, CardColor, CardValue
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.manipulating_cards import SortedType

from typing import Iterator

class QuinteFlushDetector : 
    def __init__(self, manipulating_cards, quinte_detector):
        self.manipulating_cards = manipulating_cards 
        self.quinte_detector = quinte_detector
        self.card_color = CardColor.UNDEFINED
        self.quinte_figure = None

    def find_quinte_flush(self, hand: Iterator[Card]) -> QuinteFlushFigure:
        is_same_color = True
        self.quinte_figure = self.quinte_detector.find_quinte(hand)
        if self.quinte_figure != None : 
            self.card_color = self.__get_majority_color(hand)
            all_cards_in_quinte = self.__get_all_cards_compatible_with_quinte_flush(hand)
            if all_cards_in_quinte == None : 
                return None
            all_cards_in_quinte_without_doublon = self.manipulating_cards.sorted_card(all_cards_in_quinte, 5, SortedType.NO_DOUBLON)
            is_same_color = self.__determine_if_cards_have_same_color(all_cards_in_quinte_without_doublon)
            if is_same_color == False : 
                return None
            else : 
                if len(all_cards_in_quinte_without_doublon[0]) == 5 : 
                    return QuinteFlushFigure(self.quinte_figure.value, self.card_color)
                else : 
                    return self.__identify_quinte_flush(all_cards_in_quinte_without_doublon, all_cards_in_quinte, card_mini)
        else :
            return None    

    def __get_all_cards_compatible_with_quinte_flush(self, hand):
        all_cards_in_quinte = []
        card_mini = self.quinte_figure.value - 4
        for card in hand : 
            if card.value >= card_mini and card.color == self.card_color : 
                all_cards_in_quinte.append(card)
        if len(all_cards_in_quinte) < 5 : 
            return None
        else : 
            return all_cards_in_quinte

    def __get_majority_color(self, hand):
        all_cards_colors = {}
        for card in hand : 
            if card.color in all_cards_colors : 
                all_cards_colors[card.color] += 1
            else : 
                all_cards_colors[card.color] = 1
        card_color_max = CardColor.UNDEFINED
        count_color = 0
        for color in all_cards_colors :
            count_this_color = all_cards_colors[color]            
            if count_color < count_this_color : 
                count_color = count_this_color
                card_color_max = color
        return card_color_max

    def __determine_if_cards_have_same_color(self, all_cards_in_quinte_without_doublon):
        is_same_color = True
        for card in all_cards_in_quinte_without_doublon[0] : 
            is_same_color = self.__determine_is_same_color_is_ok_for_this_card(self.quinte_figure.value, card, self.card_color)
            if is_same_color == False : 
                break
        return is_same_color
                        
    def __determine_is_same_color_is_ok_for_this_card(self, quinte_figure_value, card, card_color):
        is_same_color = True
        difference_card_value = quinte_figure_value - card.value
        if difference_card_value < 4 and difference_card_value > 0 and card.color != card_color : 
            is_same_color = False
        return is_same_color    

    def __check_if_one_doublon_have_majority_color(self, doublon_cards, card_mini): 
        is_same_color = False
        for card in doublon_cards : 
            if card.value >= card_mini and card.color == self.card_color : 
                is_same_color = True 
                if is_same_color: 
                    break
        return is_same_color

    def __identify_quinte_flush(self, all_cards_in_quinte_without_doublon, all_cards_in_quinte, card_mini):
        if len(all_cards_in_quinte_without_doublon[0]) == 5 : 
            return QuinteFlushFigure(self.quinte_figure.value, self.card_color)
        else : 
            doublon_cards = self.manipulating_cards.sorted_card(all_cards_in_quinte, 5, SortedType.ONLY_DOUBLONS)
            is_same_color = self.__check_if_one_doublon_have_majority_color(doublon_cards, card_mini)
            if is_same_color : 
                return QuinteFlushFigure(self.quinte_figure.value, self.card_color)
            else : 
                return None