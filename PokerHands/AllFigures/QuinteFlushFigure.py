from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class QuinteFlushFigure : 
    value : CardValue
    color : CardColor
    points : ClassVar[int] = 90

    def compare_with_other_quinte_flush_poker_hands(self, other_combination: type[Self]) -> Winner:
        if self.value < other_combination.value :
            return Winner.SECOND_COMBINATION
        elif other_combination.value < self.value :
            return Winner.FIRST_COMBINATION
        else : 
            return Winner.UNDETERMINATED            