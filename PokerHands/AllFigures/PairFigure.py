from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class PairFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 20

    def compare_with_onther_one_pair_hand(self, other_pair: type[Self]): 
        if self.value < other_pair.value : 
            return Winner.SECOND_HAND
        elif other_pair.value < self.value : 
            return Winner.FIRST_HAND
        else : 
            if self.high_value_rest_of_cards < other_pair.high_value_rest_of_cards : 
                return Winner.SECOND_HAND
            elif other_pair.high_value_rest_of_cards < self.high_value_rest_of_cards :
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY