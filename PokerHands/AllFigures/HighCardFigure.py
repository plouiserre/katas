from dataclasses import dataclass
from PokerHands.card import CardValue
from typing import ClassVar, Self
from PokerHands.winner import Winner

@dataclass(frozen=True)
class HighCardFigure : 
    value : CardValue
    points : ClassVar[int] = 10

    def compare_with_other_high_cards_poker_hands(self, other_poker_hand: type[Self]) -> Winner: 
        if self.value < other_poker_hand.value : 
            return Winner.SECOND_POKER_HAND
        elif other_poker_hand.value < self.value : 
            return Winner.FIRST_POKER_HAND 
        else :
            return Winner.EQUALITY