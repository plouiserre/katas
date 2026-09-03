from PokerHandsV2.card import Card, CardColor, CardValue
from PokerHandsV2.AllFigures.FlushFigure import FlushFigure

from typing import Iterator

class FlushDetector : 
    def __init__(self):
        pass

    def find_flush(self, hand : Iterator[Card]) -> FlushFigure:
        if len(hand) == 5 :
            return self.__analyse_hand_when_the_player_have_five_cards(hand)
        else : 
            return None

    def __analyse_hand_when_the_player_have_five_cards(self, hand : Iterator[Card]) -> FlushFigure:
        is_flush = True
        last_color = CardColor.UNDEFINED
        high_card_value = CardValue.TWO
        for card in hand : 
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