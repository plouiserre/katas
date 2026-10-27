from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class FourOfKindFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 80

    def compare_with_other_four_of_kind_poker_hands(self, other_combination: type[Self]) -> Winner:
        if self.value < other_combination.value : 
            return Winner.SECOND_COMBINATION
        elif other_combination.value < self.value :
            return Winner.FIRST_COMBINATION
        else : 
            if self.high_value_rest_of_cards < other_combination.high_value_rest_of_cards : 
                return Winner.SECOND_COMBINATION
            elif other_combination.high_value_rest_of_cards < self.high_value_rest_of_cards : 
                return Winner.FIRST_COMBINATION
            else : 
                return Winner.EQUALITY