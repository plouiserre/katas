from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class QuinteFigure:
    value : CardValue
    points : ClassVar[int] = 50

    def compare_with_other_quinte_poker_hand(self, other_poker_hand: type[Self]) -> Winner:
        if self.value < other_poker_hand.value : 
            return Winner.SECOND_POKER_HAND 
        elif other_poker_hand.value < self.value : 
            return Winner.FIRST_POKER_HAND
        elif self.value == other_poker_hand.value :
            return Winner.EQUALITY
        else : 
            return Winner.UNDETERMINATED