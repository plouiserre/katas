from PokerHands.AllFigures.Figure import Figure
from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure 
from PokerHands.AllFigures.FullFigure import FullFigure 
from PokerHands.AllFigures.HighCardFigure import HighCardFigure 
from PokerHands.AllFigures.PairFigure import PairFigure 
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.StraitFigure import StraitFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure 
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.winner import Winner

class Score: 
    def __init__(self, first_hand : Figure, second_hand : Figure):
        self.first_hand = first_hand
        self.second_hand = second_hand

    def determinate_winner(self):
        if self.first_hand.points < self.second_hand.points : 
            return Winner.SECOND_HAND
        elif self.second_hand.points < self.first_hand.points : 
            return Winner.FIRST_HAND
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
        elif type(self.first_hand) is QuinteFlushFigure and type(self.second_hand) is QuinteFlushFigure: 
            return self.__compare_quinte_flush()
        else : 
            return Winner.UNDETERMINATED
              
    def __compare_two_hands_with_high_cards(self): 
        if self.first_hand.value < self.second_hand.value : 
            return Winner.SECOND_HAND
        elif self.second_hand.value < self.first_hand.value : 
            return Winner.FIRST_HAND 
        else :
            return Winner.EQUALITY
        
    def __compare_two_hands_with_pairs(self):
        if self.first_hand.value < self.second_hand.value : 
            return Winner.SECOND_HAND
        elif self.second_hand.value < self.first_hand.value : 
            return Winner.FIRST_HAND
        else : 
            if self.first_hand.high_value_rest_of_cards < self.second_hand.high_value_rest_of_cards : 
                return Winner.SECOND_HAND
            elif self.second_hand.high_value_rest_of_cards < self.first_hand.high_value_rest_of_cards :
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY

    def __compare_two_hands_with_two_pairs(self):
        high_first_pair = self.__get_high_pair(self.first_hand)
        high_second_pair = self.__get_high_pair(self.second_hand)
        if high_first_pair < high_second_pair : 
            return Winner.SECOND_HAND
        elif high_second_pair < high_first_pair : 
            return Winner.FIRST_HAND
        else : 
            lower_first_pair = self.__get_lower_pair(self.first_hand)
            lower_second_pair = self.__get_lower_pair(self.second_hand)
            if lower_first_pair < lower_second_pair :
                return Winner.SECOND_HAND
            elif lower_second_pair < lower_first_pair :
                return Winner.FIRST_HAND
            else : 
                if self.first_hand.high_value_rest_of_cards < self.second_hand.high_value_rest_of_cards :
                    return Winner.SECOND_HAND
                elif self.second_hand.high_value_rest_of_cards < self.first_hand.high_value_rest_of_cards : 
                    return Winner.FIRST_HAND
                else : 
                    return Winner.EQUALITY
                
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
            return Winner.SECOND_HAND
        elif self.second_hand.value < self.first_hand.value : 
            return Winner.FIRST_HAND
        else : 
            if self.first_hand.high_value_rest_of_cards < self.second_hand.high_value_rest_of_cards : 
                return Winner.SECOND_HAND 
            elif self.second_hand.high_value_rest_of_cards < self.first_hand.high_value_rest_of_cards : 
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY
            
    def __compare_two_hands_with_straight_figure(self):
        if self.first_hand.value < self.second_hand.value : 
            return Winner.SECOND_HAND 
        elif self.second_hand.value < self.first_hand.value : 
            return Winner.FIRST_HAND
        elif self.first_hand.value == self.second_hand.value :
            return Winner.EQUALITY
        else : 
            return Winner.UNDETERMINATED
        
    def __compare_two_hands_with_flush_figure(self): 
        if self.first_hand.high_value < self.second_hand.high_value : 
            return Winner.SECOND_HAND
        elif self.second_hand.high_value < self.first_hand.high_value :
            return Winner.FIRST_HAND
        else : 
            return Winner.EQUALITY
            
    def __compare_full_hands(self) :
        if self.first_hand.three_times < self.second_hand.three_times : 
            return Winner.SECOND_HAND
        elif self.second_hand.three_times < self.first_hand.three_times : 
            return Winner.FIRST_HAND
        else : 
            if self.first_hand.two_times < self.second_hand.two_times : 
                return Winner.SECOND_HAND
            elif self.second_hand.two_times < self.first_hand.two_times: 
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY
            
    def __compare_four_kind_figure(self):
        if self.first_hand.value < self.second_hand.value : 
            return Winner.SECOND_HAND
        elif self.second_hand.value < self.first_hand.value :
            return Winner.FIRST_HAND
        else : 
            if self.first_hand.high_value_rest_of_cards < self.second_hand.high_value_rest_of_cards : 
                return Winner.SECOND_HAND
            elif self.second_hand.high_value_rest_of_cards < self.first_hand.high_value_rest_of_cards : 
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY
            
    def __compare_quinte_flush(self):
        if self.first_hand.value < self.second_hand.value :
            return Winner.SECOND_HAND
        elif self.second_hand.value < self.first_hand.value :
            return Winner.FIRST_HAND
        else : 
            return Winner.UNDETERMINATED