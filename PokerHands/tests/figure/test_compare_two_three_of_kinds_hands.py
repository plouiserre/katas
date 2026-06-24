from PokerHands.card import CardValue
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_where_two_hands_have_differents_three_of_kinds():
    first_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.FIVE)
    second_hand = ThreeOfKindFigure(CardValue.TEN, CardValue.ACE)
    assert(FIRST_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_but_differents_high_cards():
    first_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.FIVE)
    second_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    assert(SECOND_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_and_same_high_cards():
    first_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    second_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    assert(EQUALITY == compare_two_three_of_kind_hands(first_hand, second_hand))

def compare_two_three_of_kind_hands(first_hand, second_hand):
    result = first_hand.compare_with_other_three_of_kinds_hands(second_hand)
    return result