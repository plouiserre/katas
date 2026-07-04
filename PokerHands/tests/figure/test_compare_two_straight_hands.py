from PokerHands.card import CardValue
from PokerHands.AllFigures.StraitFigure import StraitFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY
from PokerHands.tests.random_cards import get_all_values, get_high_cards, get_lower_card, get_random_card

def test_compare_where_each_hand_have_differents_straights_with_second_hand_win():
    all_cards_values = get_all_values()
    high_card = get_high_cards(all_cards_values)
    low_card = get_lower_card(all_cards_values, high_card)
    first_hand = StraitFigure(low_card)
    second_hand = StraitFigure(high_card)
    assert(SECOND_HAND == compare_two_straights_hands(first_hand, second_hand))
    

def test_compare_where_each_hand_have_differents_straights_with_first_hand_win():
    all_cards_values = get_all_values()
    high_card = get_high_cards(all_cards_values)
    low_card = get_lower_card(all_cards_values, high_card)
    first_hand = StraitFigure(high_card)
    second_hand = StraitFigure(low_card)
    assert(FIRST_HAND == compare_two_straights_hands(first_hand, second_hand))

def test_compare_where_each_hand_have_same_straights():
    all_cards_values = get_all_values()
    random_card = get_random_card(all_cards_values)
    first_hand = StraitFigure(random_card)
    second_hand = StraitFigure(random_card)
    assert(EQUALITY == compare_two_straights_hands(first_hand, second_hand))
    
def compare_two_straights_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_straight_hand(second_hand)
    return result