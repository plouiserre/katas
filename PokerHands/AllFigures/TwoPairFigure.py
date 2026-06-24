from dataclasses import dataclass
from PokerHands.card import CardValue
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY
from typing import ClassVar

@dataclass(frozen=True)
class TwoPairFigure: 
    first_pair_value : CardValue
    second_pair_value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 30

    def compare_with_other_two_pairs_hands(self, other_hand): 
        high_first_pair = self.__get_high_pair(self)
        high_second_pair = self.__get_high_pair(other_hand)
        if high_first_pair < high_second_pair : 
            return SECOND_HAND
        elif high_second_pair < high_first_pair : 
            return FIRST_HAND
        else : 
            lower_first_pair = self.__get_lower_pair(self)
            lower_second_pair = self.__get_lower_pair(other_hand)
            if lower_first_pair < lower_second_pair :
                return SECOND_HAND
            elif lower_second_pair < lower_first_pair :
                return FIRST_HAND
            else : 
                if self.high_value_rest_of_cards < other_hand.high_value_rest_of_cards :
                    return SECOND_HAND
                elif other_hand.high_value_rest_of_cards < self.high_value_rest_of_cards : 
                    return FIRST_HAND
                else : 
                    return EQUALITY
                
    def __get_high_pair(self, hand) : 
        if hand.first_pair_value < hand.second_pair_value :
            return hand.second_pair_value
        else : 
            return hand.first_pair_value
        
    def __get_lower_pair(self, hand): 
        if hand.first_pair_value < hand.second_pair_value :
            return hand.first_pair_value
        else : 
            return hand.second_pair_value  