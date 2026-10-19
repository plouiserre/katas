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

#TODO rename this
class CompareSameTypeHand: 
    def __init__(self):
        pass

    def compare_poker_hands(self, FIRST_POKER_HAND, SECOND_POKER_HAND) : 
        if type(FIRST_POKER_HAND) is HighCardFigure and type(SECOND_POKER_HAND) is HighCardFigure:
            return self.__compare_two_poker_hands_with_high_cards(FIRST_POKER_HAND, SECOND_POKER_HAND)
        elif type(FIRST_POKER_HAND) is PairFigure and type(SECOND_POKER_HAND) is PairFigure: 
            return self.__compare_two_poker_hands_with_pairs(FIRST_POKER_HAND, SECOND_POKER_HAND)
        elif type(FIRST_POKER_HAND) is TwoPairFigure and type(SECOND_POKER_HAND) is TwoPairFigure : 
            return self.__compare_two_poker_hands_with_two_pairs(FIRST_POKER_HAND, SECOND_POKER_HAND)
        elif type(FIRST_POKER_HAND) is ThreeOfKindFigure and type(SECOND_POKER_HAND) is ThreeOfKindFigure : 
            return self.__compare_two_poker_hands_with_three_of_kinds(FIRST_POKER_HAND, SECOND_POKER_HAND)
        elif type(FIRST_POKER_HAND) is QuinteFigure and type(SECOND_POKER_HAND) is QuinteFigure : 
            return self.__compare_two_poker_hands_with_quinte(FIRST_POKER_HAND, SECOND_POKER_HAND)
        elif type(FIRST_POKER_HAND) is FlushFigure and type(SECOND_POKER_HAND) is FlushFigure : 
            return self.__compare_two_poker_hands_with_flush(FIRST_POKER_HAND, SECOND_POKER_HAND)
        elif type(FIRST_POKER_HAND) is FourOfKindFigure and type(SECOND_POKER_HAND) is FourOfKindFigure:
            return self.__compare_two_poker_hands_with_four_a_kind(FIRST_POKER_HAND, SECOND_POKER_HAND)
        elif type(FIRST_POKER_HAND) is QuinteFlushFigure and type(SECOND_POKER_HAND) is QuinteFlushFigure:
            return self.__compare_two_poker_hands_with_quinte_flush(FIRST_POKER_HAND, SECOND_POKER_HAND)

    def __compare_two_poker_hands_with_high_cards(self, FIRST_POKER_HAND : HighCardFigure, SECOND_POKER_HAND : HighCardFigure) -> Winner: 
                if FIRST_POKER_HAND.value < SECOND_POKER_HAND.value : 
                    return Winner.SECOND_POKER_HAND
                elif SECOND_POKER_HAND.value < FIRST_POKER_HAND.value : 
                    return Winner.FIRST_POKER_HAND 
                else :
                    return Winner.EQUALITY
                    
    def __compare_two_poker_hands_with_pairs(self, FIRST_POKER_HAND : PairFigure, SECOND_POKER_HAND : PairFigure) -> Winner:
        if FIRST_POKER_HAND.value < SECOND_POKER_HAND.value : 
            return Winner.SECOND_POKER_HAND
        elif SECOND_POKER_HAND.value < FIRST_POKER_HAND.value : 
            return Winner.FIRST_POKER_HAND
        else : 
            if FIRST_POKER_HAND.high_value_rest_of_cards < SECOND_POKER_HAND.high_value_rest_of_cards : 
                return Winner.SECOND_POKER_HAND
            elif SECOND_POKER_HAND.high_value_rest_of_cards < FIRST_POKER_HAND.high_value_rest_of_cards :
                return Winner.FIRST_POKER_HAND
            else : 
                return Winner.EQUALITY

    def __compare_two_poker_hands_with_two_pairs(self, FIRST_POKER_HAND : TwoPairFigure, SECOND_POKER_HAND : TwoPairFigure) -> Winner : 
        if FIRST_POKER_HAND.first_pair_value < SECOND_POKER_HAND.first_pair_value : 
            return Winner.SECOND_POKER_HAND
        elif SECOND_POKER_HAND.first_pair_value < FIRST_POKER_HAND.first_pair_value : 
            return Winner.FIRST_POKER_HAND
        elif FIRST_POKER_HAND.first_pair_value == SECOND_POKER_HAND.first_pair_value : 
            if FIRST_POKER_HAND.second_pair_value < SECOND_POKER_HAND.second_pair_value : 
                return Winner.SECOND_POKER_HAND
            elif SECOND_POKER_HAND.second_pair_value < FIRST_POKER_HAND.second_pair_value : 
                return Winner.FIRST_POKER_HAND
            elif FIRST_POKER_HAND.second_pair_value == SECOND_POKER_HAND.second_pair_value : 
                if FIRST_POKER_HAND.high_value_rest_of_cards < SECOND_POKER_HAND.high_value_rest_of_cards :
                    return Winner.SECOND_POKER_HAND
                else :
                    return Winner.FIRST_POKER_HAND

    def __compare_two_poker_hands_with_three_of_kinds(self, FIRST_POKER_HAND : ThreeOfKindFigure, SECOND_POKER_HAND : ThreeOfKindFigure): 
        if FIRST_POKER_HAND.value < SECOND_POKER_HAND.value :
            return Winner.SECOND_POKER_HAND
        elif SECOND_POKER_HAND.value < FIRST_POKER_HAND.value : 
            return Winner.FIRST_POKER_HAND
        elif FIRST_POKER_HAND.value == SECOND_POKER_HAND.value : 
            if FIRST_POKER_HAND.high_value_rest_of_cards < SECOND_POKER_HAND.high_value_rest_of_cards :
                return Winner.SECOND_POKER_HAND
            elif SECOND_POKER_HAND.high_value_rest_of_cards < FIRST_POKER_HAND.high_value_rest_of_cards : 
                return Winner.FIRST_POKER_HAND

    def __compare_two_poker_hands_with_quinte(self, FIRST_POKER_HAND : QuinteFigure, SECOND_POKER_HAND : QuinteFigure):
        if FIRST_POKER_HAND.value < SECOND_POKER_HAND.value : 
            return Winner.SECOND_POKER_HAND 
        elif SECOND_POKER_HAND.value < FIRST_POKER_HAND.value : 
            return Winner.FIRST_POKER_HAND

    def __compare_two_poker_hands_with_flush(self, FIRST_POKER_HAND : FlushFigure, SECOND_POKER_HAND : FlushFigure):
        if FIRST_POKER_HAND.high_value < SECOND_POKER_HAND.high_value : 
            return Winner.SECOND_POKER_HAND 
        elif SECOND_POKER_HAND.high_value < FIRST_POKER_HAND.high_value : 
            return Winner.FIRST_POKER_HAND

    def __compare_two_poker_hands_with_four_a_kind(self, FIRST_POKER_HAND : FourOfKindFigure, SECOND_POKER_HAND : FourOfKindFigure):
        if FIRST_POKER_HAND.value < SECOND_POKER_HAND.value : 
            return Winner.SECOND_POKER_HAND 
        elif SECOND_POKER_HAND.value < FIRST_POKER_HAND.value : 
            return Winner.FIRST_POKER_HAND
        elif FIRST_POKER_HAND.value == SECOND_POKER_HAND.value : 
            if FIRST_POKER_HAND.high_value_rest_of_cards < SECOND_POKER_HAND.high_value_rest_of_cards : 
                return Winner.SECOND_POKER_HAND 
            elif SECOND_POKER_HAND.high_value_rest_of_cards < FIRST_POKER_HAND.high_value_rest_of_cards :
                return Winner.FIRST_POKER_HAND

    def __compare_two_poker_hands_with_quinte_flush(self, FIRST_POKER_HAND : QuinteFlushFigure, SECOND_POKER_HAND : QuinteFlushFigure):
        if FIRST_POKER_HAND.value < SECOND_POKER_HAND.value : 
            return Winner.SECOND_POKER_HAND 
        elif SECOND_POKER_HAND.value < FIRST_POKER_HAND.value : 
            return Winner.FIRST_POKER_HAND