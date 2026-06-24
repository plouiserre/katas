from PokerHands.card import CardValue
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_two_four_a_kind():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    second_hand = FourOfKindFigure(CardValue.ACE, CardValue.KING)
    assert(SECOND_HAND == compare_two_four_of_kind_hands(first_hand, second_hand))

def test_compare_two_four_a_kind_exactly_with_differents_high_cards():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.ACE)
    second_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.KING)
    assert(FIRST_HAND == compare_two_four_of_kind_hands(first_hand, second_hand))

def test_compare_two_four_a_kind_with_same_cards():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    second_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    assert(EQUALITY == compare_two_four_of_kind_hands(first_hand, second_hand))

def compare_two_four_of_kind_hands(first_hand, second_hand):
    result = first_hand.compare_with_other_four_of_kind_hands(second_hand)
    return result