from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.score_tmp import EQUALITY, FIRST_HAND, SECOND_HAND
from typing import ClassVar

@dataclass(frozen=True)
class PairFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 20

    def compare_with_onther_one_pair_hand(self, other_pair): 
        if self.value < other_pair.value : 
            return SECOND_HAND
        elif other_pair.value < self.value : 
            return FIRST_HAND
        else : 
            if self.high_value_rest_of_cards < other_pair.high_value_rest_of_cards : 
                return SECOND_HAND
            elif other_pair.high_value_rest_of_cards < self.high_value_rest_of_cards :
                return FIRST_HAND
            else : 
                return EQUALITY