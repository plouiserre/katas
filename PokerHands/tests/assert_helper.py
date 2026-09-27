from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure

def is_this_two_figure_are_equal( first_figure, second_figure): 
        is_good_hand = False
        if isinstance(first_figure, HighCardFigure) and isinstance(second_figure, HighCardFigure) and first_figure.value == second_figure.value : 
            is_good_hand = True
        elif isinstance(first_figure, PairFigure) and isinstance(second_figure,PairFigure) and first_figure.value == second_figure.value and first_figure.high_value_rest_of_cards == second_figure.high_value_rest_of_cards : 
            is_good_hand = True
        elif isinstance(first_figure, TwoPairFigure) and isinstance(second_figure,TwoPairFigure) and first_figure.first_pair_value == second_figure.first_pair_value and first_figure.second_pair_value == second_figure.second_pair_value and first_figure.high_value_rest_of_cards == second_figure.high_value_rest_of_cards :
            is_good_hand = True
        elif first_figure is ThreeOfKindFigure and second_figure is ThreeOfKindFigure and first_figure.value == second_figure.value and first_figure.high_value_rest_of_cards == second_figure.high_value_rest_of_cards: 
            is_good_hand = True
        elif first_figure is QuinteFigure and second_figure is QuinteFigure and first_figure.value == second_figure.value : 
            is_good_hand = True
        elif first_figure is FlushFigure and second_figure is FlushFigure and first_figure.color == second_figure.color and first_figure.high_value == second_figure.high_value :
            is_good_hand = True
        elif first_figure is FullFigure and second_figure is FullFigure and first_figure.two_times == second_figure.two_times and first_figure.three_times == second_figure.three_times : 
            is_good_hand = True
        elif first_figure is FourOfKindFigure and second_figure is FourOfKindFigure and first_figure.value == second_figure.value and first_figure.high_value_rest_of_cards == second_figure.high_value_rest_of_cards :
            is_good_hand = True
        elif first_figure is QuinteFlushFigure and second_figure is QuinteFlushFigure and first_figure.value == second_figure.value and first_figure.color == second_figure.color : 
            is_good_hand = True
        return is_good_hand