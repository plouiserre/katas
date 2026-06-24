from PokerHands.card import CardValue
from PokerHands.AllFigures.StraitFigure import StraitFigure 
from PokerHands.score_tmp import SECOND_HAND, EQUALITY

def test_compare_where_each_hand_have_differents_straights():
    first_hand = StraitFigure(CardValue.QUEEN)
    second_hand = StraitFigure(CardValue.KING)
    assert(SECOND_HAND == compare_two_straights_hands(first_hand, second_hand))

def test_compare_where_each_hand_have_same_straights():
    first_hand = StraitFigure(CardValue.QUEEN)
    second_hand = StraitFigure(CardValue.QUEEN)
    assert(EQUALITY == compare_two_straights_hands(first_hand, second_hand))

def compare_two_straights_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_straight_hand(second_hand)
    return result