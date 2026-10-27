from dataclasses import dataclass
from typing import ClassVar, Self
from PokerHands.card import CardValue, CardColor
from PokerHands.winner import Winner

@dataclass(frozen=True)
class FlushFigure : 
    color : CardColor
    high_value : CardValue
    points : ClassVar[int] = 60

    def compare_with_other_flush_poker_hands(self, other_combination: type[Self]) -> Winner: 
        if self.high_value < other_combination.high_value : 
            return Winner.SECOND_COMBINATION
        elif other_combination.high_value < self.high_value :
            return Winner.FIRST_COMBINATION
        else : 
            return Winner.EQUALITY