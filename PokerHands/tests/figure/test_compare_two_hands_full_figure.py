from PokerHands.card import CardValue
from PokerHands.AllFigures.FullFigure import FullFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_two_hands_with_differents_fulls():
    first_hand = FullFigure(CardValue.FIVE, CardValue.ACE)
    second_hand = FullFigure(CardValue.THREE, CardValue.TWO)
    assert(FIRST_HAND == compare_two_full_figure_hands(first_hand, second_hand))

def test_compare_two_hands_with_full_and_three_same_cards():
    first_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    second_hand = FullFigure(CardValue.QUEEN, CardValue.ACE)
    assert(SECOND_HAND == compare_two_full_figure_hands(first_hand, second_hand))

def test_compare_two_hands_with_same_fulls():
    first_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    second_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    assert(EQUALITY == compare_two_full_figure_hands(first_hand, second_hand))

def compare_two_full_figure_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_full_figure_hands(second_hand)
    return result