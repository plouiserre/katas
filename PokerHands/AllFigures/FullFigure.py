from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class FullFigure : 
    two_times : CardValue
    three_times : CardValue
    points : ClassVar[int] = 70

    def compare_with_other_full_figure_poker_hands(self, other_poker_hand: type[Self]) -> Winner:
        if self.three_times < other_poker_hand.three_times : 
            return Winner.SECOND_POKER_HAND
        elif other_poker_hand.three_times < self.three_times : 
            return Winner.FIRST_POKER_HAND
        else : 
            if self.two_times < other_poker_hand.two_times : 
                return Winner.SECOND_POKER_HAND
            elif other_poker_hand.two_times < self.two_times: 
                return Winner.FIRST_POKER_HAND
            else : 
                return Winner.EQUALITY