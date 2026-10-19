from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class QuinteFlushFigure : 
    value : CardValue
    color : CardColor
    points : ClassVar[int] = 90

    def compare_with_other_quinte_flush_poker_hands(self, other_poker_hand: type[Self]) -> Winner:
        if self.value < other_poker_hand.value :
            return Winner.SECOND_POKER_HAND
        elif other_poker_hand.value < self.value :
            return Winner.FIRST_POKER_HAND
        else : 
            return Winner.UNDETERMINATED            