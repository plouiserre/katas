from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class FullFigure : 
    two_times : CardValue
    three_times : CardValue
    points : ClassVar[int] = 70

    def compare_with_other_full_figure_hands(self, other_hand: type[Self]):
        if self.three_times < other_hand.three_times : 
            return Winner.SECOND_HAND
        elif other_hand.three_times < self.three_times : 
            return Winner.FIRST_HAND
        else : 
            if self.two_times < other_hand.two_times : 
                return Winner.SECOND_HAND
            elif other_hand.two_times < self.two_times: 
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY