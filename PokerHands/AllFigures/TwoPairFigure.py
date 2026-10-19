from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.winner import Winner
from typing import ClassVar, Self

@dataclass(frozen=True)
class TwoPairFigure: 
    first_pair_value : CardValue
    second_pair_value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 30

    def compare_with_other_two_pairs_poker_hands(self, other_poker_hand: type[Self]) -> Winner: 
        high_first_pair = self.__get_high_pair(self)
        high_second_pair = self.__get_high_pair(other_poker_hand)
        if high_first_pair < high_second_pair : 
            return Winner.SECOND_POKER_HAND
        elif high_second_pair < high_first_pair : 
            return Winner.FIRST_POKER_HAND
        else : 
            lower_first_pair = self.__get_lower_pair(self)
            lower_second_pair = self.__get_lower_pair(other_poker_hand)
            if lower_first_pair < lower_second_pair :
                return Winner.SECOND_POKER_HAND
            elif lower_second_pair < lower_first_pair :
                return Winner.FIRST_POKER_HAND
            else : 
                if self.high_value_rest_of_cards < other_poker_hand.high_value_rest_of_cards :
                    return Winner.SECOND_POKER_HAND
                elif other_poker_hand.high_value_rest_of_cards < self.high_value_rest_of_cards : 
                    return Winner.FIRST_POKER_HAND
                else : 
                    return Winner.EQUALITY
                
    def __get_high_pair(self, poker_hand) -> Winner: 
        if poker_hand.first_pair_value < poker_hand.second_pair_value :
            return poker_hand.second_pair_value
        else : 
            return poker_hand.first_pair_value
        
    def __get_lower_pair(self, poker_hand) -> Winner: 
        if poker_hand.first_pair_value < poker_hand.second_pair_value :
            return poker_hand.first_pair_value
        else : 
            return poker_hand.second_pair_value  