from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class ThreeOfKindFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 40

    def compare_with_other_three_of_kinds_hands(self, other_hand: type[Self]):
        if self.value < other_hand.value :
            return Winner.SECOND_HAND
        elif other_hand.value < self.value : 
            return Winner.FIRST_HAND
        else : 
            if self.high_value_rest_of_cards < other_hand.high_value_rest_of_cards : 
                return Winner.SECOND_HAND 
            elif other_hand.high_value_rest_of_cards < self.high_value_rest_of_cards : 
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY