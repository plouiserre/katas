from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class QuinteFigure:
    value : CardValue
    points : ClassVar[int] = 50

    def compare_with_other_quinte_poker_hand(self, other_combination: type[Self]) -> Winner:
        if self.value < other_combination.value : 
            return Winner.SECOND_COMBINATION 
        elif other_combination.value < self.value : 
            return Winner.FIRST_COMBINATION
        elif self.value == other_combination.value :
            return Winner.EQUALITY
        else : 
            return Winner.UNDETERMINATED