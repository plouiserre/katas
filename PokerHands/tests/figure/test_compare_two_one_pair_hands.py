from PokerHands.card import CardValue
from PokerHands.AllFigures.PairFigure import PairFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_one_hand_one_pair_two_second_hand_one_pair_three() :
    first_hand = PairFigure(CardValue.TWO, CardValue.QUEEN)
    second_hand = PairFigure(CardValue.THREE, CardValue.EIGHT)
    assert(SECOND_HAND == compare_two_one_pair_hands(first_hand, second_hand))

def test_compare_two_hands_with_one_same_pair_but_different_high_cards() : 
    first_hand = PairFigure(CardValue.FOUR, CardValue.QUEEN)
    second_hand = PairFigure(CardValue.FOUR, CardValue.EIGHT)
    assert(FIRST_HAND == compare_two_one_pair_hands(first_hand, second_hand))

def test_compare_two_hands_with_same_pair_and_same_high_cards():
    first_hand = PairFigure(CardValue.FOUR, CardValue.QUEEN)
    second_hand = PairFigure(CardValue.FOUR, CardValue.QUEEN)
    assert(EQUALITY == compare_two_one_pair_hands(first_hand, second_hand))

def compare_two_one_pair_hands(first_hand, second_hand):
    result = first_hand.compare_with_onther_one_pair_hand(second_hand)
    return result