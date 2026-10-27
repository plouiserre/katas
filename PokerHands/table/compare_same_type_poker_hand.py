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

class CompareSameTypePokerHand: 
    def __init__(self):
        pass

    def compare_poker_hands(self, FIRST_COMBINATION, SECOND_COMBINATION) : 
        if type(FIRST_COMBINATION) is HighCardFigure and type(SECOND_COMBINATION) is HighCardFigure:
            return self.__compare_two_poker_hands_with_high_cards(FIRST_COMBINATION, SECOND_COMBINATION)
        elif type(FIRST_COMBINATION) is PairFigure and type(SECOND_COMBINATION) is PairFigure: 
            return self.__compare_two_poker_hands_with_pairs(FIRST_COMBINATION, SECOND_COMBINATION)
        elif type(FIRST_COMBINATION) is TwoPairFigure and type(SECOND_COMBINATION) is TwoPairFigure : 
            return self.__compare_two_poker_hands_with_two_pairs(FIRST_COMBINATION, SECOND_COMBINATION)
        elif type(FIRST_COMBINATION) is ThreeOfKindFigure and type(SECOND_COMBINATION) is ThreeOfKindFigure : 
            return self.__compare_two_poker_hands_with_three_of_kinds(FIRST_COMBINATION, SECOND_COMBINATION)
        elif type(FIRST_COMBINATION) is QuinteFigure and type(SECOND_COMBINATION) is QuinteFigure : 
            return self.__compare_two_poker_hands_with_quinte(FIRST_COMBINATION, SECOND_COMBINATION)
        elif type(FIRST_COMBINATION) is FlushFigure and type(SECOND_COMBINATION) is FlushFigure : 
            return self.__compare_two_poker_hands_with_flush(FIRST_COMBINATION, SECOND_COMBINATION)
        elif type(FIRST_COMBINATION) is FourOfKindFigure and type(SECOND_COMBINATION) is FourOfKindFigure:
            return self.__compare_two_poker_hands_with_four_a_kind(FIRST_COMBINATION, SECOND_COMBINATION)
        elif type(FIRST_COMBINATION) is QuinteFlushFigure and type(SECOND_COMBINATION) is QuinteFlushFigure:
            return self.__compare_two_poker_hands_with_quinte_flush(FIRST_COMBINATION, SECOND_COMBINATION)

    def __compare_two_poker_hands_with_high_cards(self, FIRST_COMBINATION : HighCardFigure, SECOND_COMBINATION : HighCardFigure) -> Winner: 
                if FIRST_COMBINATION.value < SECOND_COMBINATION.value : 
                    return Winner.SECOND_COMBINATION
                elif SECOND_COMBINATION.value < FIRST_COMBINATION.value : 
                    return Winner.FIRST_COMBINATION 
                else :
                    return Winner.EQUALITY
                    
    def __compare_two_poker_hands_with_pairs(self, FIRST_COMBINATION : PairFigure, SECOND_COMBINATION : PairFigure) -> Winner:
        if FIRST_COMBINATION.value < SECOND_COMBINATION.value : 
            return Winner.SECOND_COMBINATION
        elif SECOND_COMBINATION.value < FIRST_COMBINATION.value : 
            return Winner.FIRST_COMBINATION
        else : 
            if FIRST_COMBINATION.high_value_rest_of_cards < SECOND_COMBINATION.high_value_rest_of_cards : 
                return Winner.SECOND_COMBINATION
            elif SECOND_COMBINATION.high_value_rest_of_cards < FIRST_COMBINATION.high_value_rest_of_cards :
                return Winner.FIRST_COMBINATION
            else : 
                return Winner.EQUALITY

    def __compare_two_poker_hands_with_two_pairs(self, FIRST_COMBINATION : TwoPairFigure, SECOND_COMBINATION : TwoPairFigure) -> Winner : 
        if FIRST_COMBINATION.first_pair_value < SECOND_COMBINATION.first_pair_value : 
            return Winner.SECOND_COMBINATION
        elif SECOND_COMBINATION.first_pair_value < FIRST_COMBINATION.first_pair_value : 
            return Winner.FIRST_COMBINATION
        elif FIRST_COMBINATION.first_pair_value == SECOND_COMBINATION.first_pair_value : 
            if FIRST_COMBINATION.second_pair_value < SECOND_COMBINATION.second_pair_value : 
                return Winner.SECOND_COMBINATION
            elif SECOND_COMBINATION.second_pair_value < FIRST_COMBINATION.second_pair_value : 
                return Winner.FIRST_COMBINATION
            elif FIRST_COMBINATION.second_pair_value == SECOND_COMBINATION.second_pair_value : 
                if FIRST_COMBINATION.high_value_rest_of_cards < SECOND_COMBINATION.high_value_rest_of_cards :
                    return Winner.SECOND_COMBINATION
                else :
                    return Winner.FIRST_COMBINATION

    def __compare_two_poker_hands_with_three_of_kinds(self, FIRST_COMBINATION : ThreeOfKindFigure, SECOND_COMBINATION : ThreeOfKindFigure): 
        if FIRST_COMBINATION.value < SECOND_COMBINATION.value :
            return Winner.SECOND_COMBINATION
        elif SECOND_COMBINATION.value < FIRST_COMBINATION.value : 
            return Winner.FIRST_COMBINATION
        elif FIRST_COMBINATION.value == SECOND_COMBINATION.value : 
            if FIRST_COMBINATION.high_value_rest_of_cards < SECOND_COMBINATION.high_value_rest_of_cards :
                return Winner.SECOND_COMBINATION
            elif SECOND_COMBINATION.high_value_rest_of_cards < FIRST_COMBINATION.high_value_rest_of_cards : 
                return Winner.FIRST_COMBINATION

    def __compare_two_poker_hands_with_quinte(self, FIRST_COMBINATION : QuinteFigure, SECOND_COMBINATION : QuinteFigure):
        if FIRST_COMBINATION.value < SECOND_COMBINATION.value : 
            return Winner.SECOND_COMBINATION 
        elif SECOND_COMBINATION.value < FIRST_COMBINATION.value : 
            return Winner.FIRST_COMBINATION

    def __compare_two_poker_hands_with_flush(self, FIRST_COMBINATION : FlushFigure, SECOND_COMBINATION : FlushFigure):
        if FIRST_COMBINATION.high_value < SECOND_COMBINATION.high_value : 
            return Winner.SECOND_COMBINATION 
        elif SECOND_COMBINATION.high_value < FIRST_COMBINATION.high_value : 
            return Winner.FIRST_COMBINATION

    def __compare_two_poker_hands_with_four_a_kind(self, FIRST_COMBINATION : FourOfKindFigure, SECOND_COMBINATION : FourOfKindFigure):
        if FIRST_COMBINATION.value < SECOND_COMBINATION.value : 
            return Winner.SECOND_COMBINATION 
        elif SECOND_COMBINATION.value < FIRST_COMBINATION.value : 
            return Winner.FIRST_COMBINATION
        elif FIRST_COMBINATION.value == SECOND_COMBINATION.value : 
            if FIRST_COMBINATION.high_value_rest_of_cards < SECOND_COMBINATION.high_value_rest_of_cards : 
                return Winner.SECOND_COMBINATION 
            elif SECOND_COMBINATION.high_value_rest_of_cards < FIRST_COMBINATION.high_value_rest_of_cards :
                return Winner.FIRST_COMBINATION

    def __compare_two_poker_hands_with_quinte_flush(self, FIRST_COMBINATION : QuinteFlushFigure, SECOND_COMBINATION : QuinteFlushFigure):
        if FIRST_COMBINATION.value < SECOND_COMBINATION.value : 
            return Winner.SECOND_COMBINATION 
        elif SECOND_COMBINATION.value < FIRST_COMBINATION.value : 
            return Winner.FIRST_COMBINATION