from PokerHands.card import CardColor, CardValue
from PokerHands.AllFigures.FlushFigure import FlushFigure

class FlushDetector : 
    def __init__(self):
        pass

    def find_flush(self, hand):
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