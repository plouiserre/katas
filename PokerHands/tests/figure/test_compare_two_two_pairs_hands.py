from PokerHands.card import CardValue
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_two_pairs_with_king_and_two_and_two_pairs_with_queen_and_jack():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.QUEEN, CardValue.JACK, CardValue.ACE)
    assert(FIRST_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_with_king_pairs_in_each_hand_and_second_pair_highter_in_second_hand():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.JACK, CardValue.ACE)
    assert(SECOND_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_different_high_cards():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.ACE)
    assert(SECOND_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_same_high_cards():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    assert(EQUALITY == compare_two_pairs_hands(first_hand, second_hand))

def compare_two_pairs_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_two_pairs_hands(second_hand)
    return result