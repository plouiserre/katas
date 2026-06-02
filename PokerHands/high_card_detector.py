from PokerHands.card import CardValue
from PokerHands.Figure import HighCardFigure

class HighCardDetector:
    def __init__(self):
        pass

    def find_high_card(self, cards_sorted):
        high_value = CardValue.TWO
        for card in cards_sorted : 
            if high_value < card.value : 
                high_value = card.value
        return HighCardFigure(high_value)