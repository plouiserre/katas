from dataclasses import dataclass
from PokerHands.card import CardValue
from typing import ClassVar, Self
from PokerHands.winner import Winner

@dataclass(frozen=True)
class HighCardFigure : 
    value : CardValue
    points : ClassVar[int] = 10

    def compare_with_other_high_cards_hands(self, other_hand: type[Self]) : 
        if self.value < other_hand.value : 
            return Winner.SECOND_HAND
        elif other_hand.value < self.value : 
            return Winner.FIRST_HAND 
        else :
            return Winner.EQUALITY