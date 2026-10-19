from dataclasses import dataclass
from typing import ClassVar, Self
from PokerHands.card import CardValue, CardColor
from PokerHands.winner import Winner

@dataclass(frozen=True)
class FlushFigure : 
    color : CardColor
    high_value : CardValue
    points : ClassVar[int] = 60

    def compare_with_other_flush_poker_hands(self, other_poker_hand: type[Self]) -> Winner: 
        if self.high_value < other_poker_hand.high_value : 
            return Winner.SECOND_POKER_HAND
        elif other_poker_hand.high_value < self.high_value :
            return Winner.FIRST_POKER_HAND
        else : 
            return Winner.EQUALITY