from PokerHands.card import Card, CardValue
from PokerHands.AllFigures.HighCardFigure import HighCardFigure

from typing import Iterator

class HighCardDetector:
    def __init__(self):
        pass

    def find_high_card(self, hand: Iterator[Card]) -> HighCardFigure:
        high_value = CardValue.TWO
        for card in hand : 
            if high_value < card.value : 
                high_value = card.value
        return HighCardFigure(high_value)