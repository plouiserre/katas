from PokerHands.AllFigures.Figure import Figure
from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.winner import Winner

class CompareSameTypeHand: 
    def __init__(self):
        pass

    def compare_hands(self, first_hand, second_hand) : 
        if type(first_hand) is HighCardFigure and type(second_hand) is HighCardFigure:
            return self.__compare_two_hands_with_high_cards(first_hand, second_hand)
        elif type(first_hand) is PairFigure and type(second_hand) is PairFigure: 
            return self.__compare_two_hands_with_pairs(first_hand, second_hand)
        elif type(first_hand) is TwoPairFigure and type(second_hand) is TwoPairFigure : 
            return self.__compare_two_hands_with_two_pairs(first_hand, second_hand)
        elif type(first_hand) is ThreeOfKindFigure and type(second_hand) is ThreeOfKindFigure : 
            return self.__compare_two_hands_with_three_of_kinds(first_hand, second_hand)
        elif type(first_hand) is QuinteFigure and type(second_hand) is QuinteFigure : 
            return self.__compare_two_hands_with_quinte(first_hand, second_hand)
        elif type(first_hand) is FlushFigure and type(second_hand) is FlushFigure : 
            return self.__compare_two_hands_with_flush(first_hand, second_hand)
        elif type(first_hand) is FourOfKindFigure and type(second_hand) is FourOfKindFigure:
            return self.__compare_two_hands_with_four_a_kind(first_hand, second_hand)
        elif type(first_hand) is QuinteFlushFigure and type(second_hand) is QuinteFlushFigure:
            return self.__compare_two_hands_with_quinte_flush(first_hand, second_hand)

    def __compare_two_hands_with_high_cards(self, first_hand : HighCardFigure, second_hand : HighCardFigure) -> Winner: 
                if first_hand.value < second_hand.value : 
                    return Winner.SECOND_HAND
                elif second_hand.value < first_hand.value : 
                    return Winner.FIRST_HAND 
                else :
                    return Winner.EQUALITY
                    
    def __compare_two_hands_with_pairs(self, first_hand : PairFigure, second_hand : PairFigure) -> Winner:
        if first_hand.value < second_hand.value : 
            return Winner.SECOND_HAND
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND
        else : 
            if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards : 
                return Winner.SECOND_HAND
            elif second_hand.high_value_rest_of_cards < first_hand.high_value_rest_of_cards :
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY

    def __compare_two_hands_with_two_pairs(self, first_hand : TwoPairFigure, second_hand : TwoPairFigure) -> Winner : 
        if first_hand.first_pair_value < second_hand.first_pair_value : 
            return Winner.SECOND_HAND
        elif second_hand.first_pair_value < first_hand.first_pair_value : 
            return Winner.FIRST_HAND
        elif first_hand.first_pair_value == second_hand.first_pair_value : 
            if first_hand.second_pair_value < second_hand.second_pair_value : 
                return Winner.SECOND_HAND
            elif second_hand.second_pair_value < first_hand.second_pair_value : 
                return Winner.FIRST_HAND
            elif first_hand.second_pair_value == second_hand.second_pair_value : 
                if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards :
                    return Winner.SECOND_HAND
                else :
                    return Winner.FIRST_HAND

    def __compare_two_hands_with_three_of_kinds(self, first_hand : ThreeOfKindFigure, second_hand : ThreeOfKindFigure): 
        if first_hand.value < second_hand.value :
            return Winner.SECOND_HAND
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND
        elif first_hand.value == second_hand.value : 
            if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards :
                return Winner.SECOND_HAND
            elif second_hand.high_value_rest_of_cards < first_hand.high_value_rest_of_cards : 
                return Winner.FIRST_HAND

    def __compare_two_hands_with_quinte(self, first_hand : QuinteFigure, second_hand : QuinteFigure):
        if first_hand.value < second_hand.value : 
            return Winner.SECOND_HAND 
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND

    def __compare_two_hands_with_flush(self, first_hand : FlushFigure, second_hand : FlushFigure):
        if first_hand.high_value < second_hand.high_value : 
            return Winner.SECOND_HAND 
        elif second_hand.high_value < first_hand.high_value : 
            return Winner.FIRST_HAND

    def __compare_two_hands_with_four_a_kind(self, first_hand : FourOfKindFigure, second_hand : FourOfKindFigure):
        if first_hand.value < second_hand.value : 
            return Winner.SECOND_HAND 
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND
        elif first_hand.value == second_hand.value : 
            if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards : 
                return Winner.SECOND_HAND 
            elif second_hand.high_value_rest_of_cards < first_hand.high_value_rest_of_cards :
                return Winner.FIRST_HAND

    def __compare_two_hands_with_quinte_flush(self, first_hand : QuinteFlushFigure, second_hand : QuinteFlushFigure):
        if first_hand.value < second_hand.value : 
            return Winner.SECOND_HAND 
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND