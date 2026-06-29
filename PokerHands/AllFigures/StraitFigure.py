from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY, UNDETERMINATED
from typing import ClassVar, Self

@dataclass(frozen=True)
class StraitFigure:
    value : CardValue
    points : ClassVar[int] = 50

    def compare_with_other_straight_hand(self, other_hand: type[Self]):
        if self.value < other_hand.value : 
            return SECOND_HAND 
        elif other_hand.value < self.value : 
            return FIRST_HAND
        elif self.value == other_hand.value :
            return EQUALITY
        else : 
            return UNDETERMINATED