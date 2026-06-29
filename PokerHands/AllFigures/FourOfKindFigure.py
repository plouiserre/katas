from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY
from typing import ClassVar, Self

@dataclass(frozen=True)
class FourOfKindFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 80

    def compare_with_other_four_of_kind_hands(self, other_hand: type[Self]):
        if self.value < other_hand.value : 
            return SECOND_HAND
        elif other_hand.value < self.value :
            return FIRST_HAND
        else : 
            if self.high_value_rest_of_cards < other_hand.high_value_rest_of_cards : 
                return SECOND_HAND
            elif other_hand.high_value_rest_of_cards < self.high_value_rest_of_cards : 
                return FIRST_HAND
            else : 
                return EQUALITY