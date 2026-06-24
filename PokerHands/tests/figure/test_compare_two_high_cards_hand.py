from PokerHands.card import CardValue
from PokerHands.AllFigures.HighCardFigure import HighCardFigure 
from PokerHands.score_tmp import SECOND_HAND, EQUALITY

def test_compare_one_hand_with_jack_and_with_ace(): 
    first_hand = HighCardFigure(CardValue.JACK)
    second_hand = HighCardFigure(CardValue.ACE)
    assert(SECOND_HAND == compare_two_high_cards_hands(first_hand, second_hand))

def test_compare_two_hands_with_high_cards_queen():
    first_hand = HighCardFigure(CardValue.QUEEN)
    second_hand = HighCardFigure(CardValue.QUEEN)
    assert(EQUALITY == compare_two_high_cards_hands(first_hand, second_hand))

def compare_two_high_cards_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_high_cards_hands(second_hand)
    return result