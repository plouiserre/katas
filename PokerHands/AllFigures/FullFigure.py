from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class FullFigure : 
    two_times : CardValue
    three_times : CardValue
    points : ClassVar[int] = 70

    def compare_with_other_full_figure_poker_hands(self, other_combination: type[Self]) -> Winner:
        if self.three_times < other_combination.three_times : 
            return Winner.SECOND_COMBINATION
        elif other_combination.three_times < self.three_times : 
            return Winner.FIRST_COMBINATION
        else : 
            if self.two_times < other_combination.two_times : 
                return Winner.SECOND_COMBINATION
            elif other_combination.two_times < self.two_times: 
                return Winner.FIRST_COMBINATION
            else : 
                return Winner.EQUALITY