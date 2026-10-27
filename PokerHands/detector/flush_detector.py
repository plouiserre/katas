from PokerHands.card import Card, CardColor, CardValue
from PokerHands.AllFigures.FlushFigure import FlushFigure

from typing import Iterator

class FlushDetector : 
    def __init__(self):
        pass

    def find_flush(self, combination : Iterator[Card]) -> FlushFigure:
        if len(combination) == 5 :
            return self.__analyse_poker_hand_when_the_player_have_five_cards(combination)
        else : 
            return None

    def __analyse_poker_hand_when_the_player_have_five_cards(self, combination : Iterator[Card]) -> FlushFigure:
        is_flush = True
        last_color = CardColor.UNDEFINED
        high_card_value = CardValue.TWO
        for card in combination : 
            if last_color == CardColor.UNDEFINED : 
                last_color = card.color 
            elif last_color != card.color : 
                is_flush = False
                break
            if high_card_value < card.value : 
                high_card_value = card.value
        if is_flush:
            return FlushFigure(last_color, high_card_value)
        else : 
            return None