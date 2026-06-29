from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, UNDETERMINATED
from typing import ClassVar, Self

@dataclass(frozen=True)
class QuinteFlushFigure : 
    value : CardValue
    color : CardColor
    points : ClassVar[int] = 90

    def compare_with_other_quinte_flush_hands(self, other_hand: type[Self]):
        if self.value < other_hand.value :
            return SECOND_HAND
        elif other_hand.value < self.value :
            return FIRST_HAND
        else : 
            return UNDETERMINATED            