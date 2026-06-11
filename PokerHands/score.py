from PokerHands.card import CardColor, CardValue
from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure, ThreeOfKindFigure, StraitFigure, FlushFigure, FullFigure, FourOfKindFigure, QuinteFlush

EQUALITY = 0
FIRST_HAND = 1
SECOND_HAND = 2
UNDETERMINATED = -9999

class Score: 
    def __init__(self, first_hand, second_hand):
        self.first_hand = first_hand
        self.second_hand = second_hand

    def determinate_winner(self):
        if self.first_hand.points < self.second_hand.points : 
            return SECOND_HAND
        elif self.second_hand.points < self.first_hand.points : 
            return FIRST_HAND
        elif type(self.first_hand) is HighCardFigure and type(self.second_hand) is HighCardFigure:
            return self.__compare_two_hands_with_high_cards()
        elif type(self.first_hand) is PairFigure and type(self.second_hand) is PairFigure: 
            return self.__compare_two_hands_with_pairs()
        elif type(self.first_hand) is TwoPairFigure and type(self.second_hand) is TwoPairFigure: 
            return self.__compare_two_hands_with_two_pairs()
        elif type(self.first_hand) is ThreeOfKindFigure and type(self.second_hand) is ThreeOfKindFigure:
            return self.__compare_two_hands_with_three_of_kinds()
        elif type(self.first_hand) is StraitFigure and type(self.second_hand) is StraitFigure : 
            return self.__compare_two_hands_with_straight_figure()
        elif type(self.first_hand) is FlushFigure and type(self.second_hand) is FlushFigure : 
            return self.__compare_two_hands_with_flush_figure()
        elif type(self.first_hand) is FullFigure and type(self.second_hand) is FullFigure : 
            return self.__compare_full_hands()
        elif type(self.first_hand) is FourOfKindFigure and type(self.second_hand) is FourOfKindFigure: 
            return self.__compare_four_kind_figure()
        elif type(self.first_hand) is QuinteFlush and type(self.second_hand) is QuinteFlush: 
            return self.__compare_quinte_flush()
        else : 
            return UNDETERMINATED
             
    def __compare_two_hands_with_high_cards(self): 
        if self.first_hand.value < self.second_hand.value : 
            return SECOND_HAND
        elif self.second_hand.value < self.first_hand.value : 
            return FIRST_HAND 
        else :
            return EQUALITY
        
    def __compare_two_hands_with_pairs(self):
        if self.first_hand.value < self.second_hand.value : 
            return SECOND_HAND
        elif self.second_hand.value < self.first_hand.value : 
            return FIRST_HAND
        else : 
            if self.first_hand.high_value_rest_of_cards < self.second_hand.high_value_rest_of_cards : 
                return SECOND_HAND
            elif self.second_hand.high_value_rest_of_cards < self.first_hand.high_value_rest_of_cards :
                return FIRST_HAND
            else : 
                return EQUALITY

    def __compare_two_hands_with_two_pairs(self):
        high_first_pair = self.__get_high_pair(self.first_hand)
        high_second_pair = self.__get_high_pair(self.second_hand)
        if high_first_pair < high_second_pair : 
            return SECOND_HAND
        elif high_second_pair < high_first_pair : 
            return FIRST_HAND
        else : 
            lower_first_pair = self.__get_lower_pair(self.first_hand)
            lower_second_pair = self.__get_lower_pair(self.second_hand)
            if lower_first_pair < lower_second_pair :
                return SECOND_HAND
            elif lower_second_pair < lower_first_pair :
                return FIRST_HAND
            else : 
                if self.first_hand.high_value_rest_of_cards < self.second_hand.high_value_rest_of_cards :
                    return SECOND_HAND
                elif self.second_hand.high_value_rest_of_cards < self.first_hand.high_value_rest_of_cards : 
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
        
    def __compare_two_hands_with_three_of_kinds(self): 
        if self.first_hand.value < self.second_hand.value :
            return SECOND_HAND
        elif self.second_hand.value < self.first_hand.value : 
            return FIRST_HAND
        else : 
            if self.first_hand.high_value_rest_of_cards < self.second_hand.high_value_rest_of_cards : 
                return SECOND_HAND 
            elif self.second_hand.high_value_rest_of_cards < self.first_hand.high_value_rest_of_cards : 
                return FIRST_HAND
            else : 
                return EQUALITY
            
    def __compare_two_hands_with_straight_figure(self):
        if self.first_hand.value < self.second_hand.value : 
            return SECOND_HAND 
        elif self.second_hand.value < self.first_hand.value : 
            return FIRST_HAND
        elif self.first_hand.value == self.second_hand.value :
            return EQUALITY
        else : 
            return UNDETERMINATED
        
    def __compare_two_hands_with_flush_figure(self): 
        if self.first_hand.high_value < self.second_hand.high_value : 
            return SECOND_HAND
        elif self.second_hand.high_value < self.first_hand.high_value :
            return FIRST_HAND
        else : 
            return EQUALITY
            
    def __compare_full_hands(self) :
        if self.first_hand.three_times < self.second_hand.three_times : 
            return SECOND_HAND
        elif self.second_hand.three_times < self.first_hand.three_times : 
            return FIRST_HAND
        else : 
            if self.first_hand.two_times < self.second_hand.two_times : 
                return SECOND_HAND
            elif self.second_hand.two_times < self.first_hand.two_times: 
                return FIRST_HAND
            else : 
                return EQUALITY
            
    def __compare_four_kind_figure(self):
        if self.first_hand.value < self.second_hand.value : 
            return SECOND_HAND
        elif self.second_hand.value < self.first_hand.value :
            return FIRST_HAND
        else : 
            if self.first_hand.high_value_rest_of_cards < self.second_hand.high_value_rest_of_cards : 
                return SECOND_HAND
            elif self.second_hand.high_value_rest_of_cards < self.first_hand.high_value_rest_of_cards : 
                return FIRST_HAND
            else : 
                return EQUALITY
            
    def __compare_quinte_flush(self):
        if self.first_hand.value < self.second_hand.value :
            return SECOND_HAND
        elif self.second_hand.value < self.first_hand.value :
            return FIRST_HAND
        else : 
            return UNDETERMINATED