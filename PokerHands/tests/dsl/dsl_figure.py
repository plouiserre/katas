from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import CardColor, CardValue

def get_figure(initial_figure, other_letters): 
    if initial_figure == "PA":
        return __get_pair_figure(other_letters)
    elif initial_figure == "HI":
        return __get_high_figure(other_letters)
    elif initial_figure == "TK": 
        return __get_three_kind_figure(other_letters)
    elif initial_figure =="QF":
        return __get_quinte_flush_figure(other_letters)
    elif initial_figure == "2P":
        return __get_two_pair_figure(other_letters)
    elif initial_figure == "FU": 
        return __get_full_figure(other_letters)

def __get_pair_figure(pair_letters):
        high_card_pair = CardValue.UNDEFINED
        pair_figure = None
        if len(pair_letters) == 1:
            pair_value = __get_card(pair_letters)
            pair_figure = PairFigure(pair_value, high_card_pair)
        else : 
            pair_value = __get_card(pair_letters[0:1])
            high_card_pair = __get_card(pair_letters[1:2])
            pair_figure = PairFigure(pair_value, high_card_pair)
        return pair_figure

def __get_high_figure(high_card_letters): 
    high_card_value = __get_card(high_card_letters)
    return HighCardFigure(high_card_value)

def __get_three_kind_figure(three_of_kind_letters): 
    three_of_kind_value = __get_card(three_of_kind_letters[0:1])
    high_card_value = __get_card(three_of_kind_letters[1:2])
    return ThreeOfKindFigure(three_of_kind_value, high_card_value)

def __get_two_pair_figure(two_pair_letters): 
    first_pair_value = __get_card(two_pair_letters[0:1])
    second_pair_value = __get_card(two_pair_letters[1:2])
    high_card_value = __get_card(two_pair_letters[2:3])
    return TwoPairFigure(first_pair_value, second_pair_value, high_card_value)

def __get_quinte_flush_figure(quinte_flush_letters): 
    quinte_flush_value = __get_card(quinte_flush_letters[0:1])
    quinte_flush_color = __get_color(quinte_flush_letters[1:2])
    return QuinteFlushFigure(quinte_flush_value, quinte_flush_color)

def __get_full_figure(full_figure_letters): 
    two_times_cards = __get_card(full_figure_letters[0:1])
    three_times_cards = __get_card(full_figure_letters[1:2])
    return FullFigure(two_times_cards, three_times_cards)

def __get_card(card_letters): 
    if card_letters == "A":
        return CardValue.ACE
    elif card_letters == "K":
        return CardValue.KING
    elif card_letters == "Q":
        return CardValue.QUEEN
    elif card_letters == "7":
        return CardValue.SEVEN
    elif card_letters == "6":
        return CardValue.SIX
    elif card_letters == "5":
        return CardValue.FIVE
    else : 
        return CardValue.UNDEFINED

def __get_color(color_letters): 
    if color_letters == "S":
        return CardColor.SPADES

def get_name_figure_from_initial(initial_figure): 
        name_figure = ""
        if initial_figure == "PA": 
            name_figure = PairFigure.__name__
        elif initial_figure == "HI":
            name_figure = HighCardFigure.__name__
        elif initial_figure == "TK":
            name_figure = ThreeOfKindFigure.__name__
        elif initial_figure == "QF":
            name_figure = QuinteFlushFigure.__name__
        elif initial_figure == "FU":
            name_figure = FullFigure.__name__
        elif initial_figure == "2P":
            name_figure = TwoPairFigure.__name__
        return name_figure