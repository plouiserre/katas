from dataclasses import dataclass
from PokerHands.card import CardValue
from typing import ClassVar, Self
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

@dataclass(frozen=True)
class HighCardFigure : 
    value : CardValue
    points : ClassVar[int] = 10

    def compare_with_other_high_cards_hands(self, other_hand: type[Self]) : 
        if self.value < other_hand.value : 
            return SECOND_HAND
        elif other_hand.value < self.value : 
            return FIRST_HAND 
        else :
            return EQUALITY