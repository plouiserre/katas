from dataclasses import dataclass
from typing import ClassVar, Self
from PokerHands.card import CardValue, CardColor
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

@dataclass(frozen=True)
class FlushFigure : 
    color : CardColor
    high_value : CardValue
    points : ClassVar[int] = 60

    def compare_with_other_flush_hands(self, other_hand: type[Self]): 
        if self.high_value < other_hand.high_value : 
            return SECOND_HAND
        elif other_hand.high_value < self.high_value :
            return FIRST_HAND
        else : 
            return EQUALITY