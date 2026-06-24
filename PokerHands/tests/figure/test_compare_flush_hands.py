from PokerHands.card import CardValue, CardColor
from PokerHands.AllFigures.FlushFigure import FlushFigure 
from PokerHands.score_tmp import FIRST_HAND, EQUALITY

def test_compare_where_each_hand_have_differents_flush(): 
    first_hand = FlushFigure(CardColor.SPADES, CardValue.EIGHT)
    second_hand = FlushFigure(CardColor.CLUBS, CardValue.SEVEN)
    assert(FIRST_HAND == compare_two_flush_hands(first_hand, second_hand))

def test_compare_where_each_hand_have_same_flush(): 
    first_hand = FlushFigure(CardColor.HEARTS, CardValue.ACE)
    second_hand = FlushFigure(CardColor.DIAMONDS, CardValue.ACE)
    assert(EQUALITY == compare_two_flush_hands(first_hand, second_hand))

def compare_two_flush_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_flush_hands(second_hand)
    return result