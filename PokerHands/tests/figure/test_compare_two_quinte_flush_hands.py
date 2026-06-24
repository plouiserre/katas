from PokerHands.card import CardValue, CardColor
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure 
from PokerHands.score_tmp import FIRST_HAND, EQUALITY


def test_compare_two_quinte_flush():
    first_hand = QuinteFlushFigure(CardValue.QUEEN, CardColor.DIAMONDS)
    second_hand = QuinteFlushFigure(CardValue.JACK, CardColor.HEARTS)
    assert(FIRST_HAND == compare_two_quinte_flushs_hands(first_hand, second_hand))

def compare_two_quinte_flushs_hands(first_hand, second_hand):
    result = first_hand.compare_with_other_quinte_flush_hands(second_hand)
    return result