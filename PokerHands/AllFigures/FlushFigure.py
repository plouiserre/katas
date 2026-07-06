from dataclasses import dataclass
from typing import ClassVar, Self
from PokerHands.card import CardValue, CardColor
from PokerHands.winner import Winner

@dataclass(frozen=True)
class FlushFigure : 
    color : CardColor
    high_value : CardValue
    points : ClassVar[int] = 60

    def compare_with_other_flush_hands(self, other_hand: type[Self]): 
        if self.high_value < other_hand.high_value : 
            return Winner.SECOND_HAND
        elif other_hand.high_value < self.high_value :
            return Winner.FIRST_HAND
        else : 
            return Winner.EQUALITY