from PokerHands.card import CardValue
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure 
from PokerHands.winner import FIRST_HAND, SECOND_HAND, EQUALITY
from PokerHands.tests.random_cards import get_all_values, get_high_cards, get_lower_card, get_random_card, remove_cards

def test_compare_two_four_a_kind():
    all_cards_values = get_all_values()
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX])
    four_a_kind_high = get_high_cards(all_cards_values)
    four_a_kind_lower = get_lower_card(all_cards_values, four_a_kind_high)
    all_cards_values_other_card = get_all_values()    
    lower_card_first_hand = get_random_card(all_cards_values_other_card)
    lower_card_second_hand = get_random_card(all_cards_values_other_card)
    first_hand = FourOfKindFigure(four_a_kind_lower, lower_card_first_hand)
    second_hand = FourOfKindFigure(four_a_kind_high, lower_card_second_hand)
    assert(SECOND_HAND == compare_two_four_of_kind_hands(first_hand, second_hand))

def test_compare_two_four_a_kind_exactly_with_differents_high_cards():
    all_cards_values = get_all_values()   
    four_a_kind = get_random_card(all_cards_values)
    first_hand_high_card = get_high_cards(all_cards_values)
    second_hand_high_card = get_lower_card(all_cards_values, first_hand_high_card)
    first_hand = FourOfKindFigure(four_a_kind, first_hand_high_card)
    second_hand = FourOfKindFigure(four_a_kind, second_hand_high_card)
    assert(FIRST_HAND == compare_two_four_of_kind_hands(first_hand, second_hand))

def test_compare_two_four_a_kind_with_same_cards():    
    all_cards_values = get_all_values()    
    four_a_kind = get_random_card(all_cards_values)
    high_card = get_random_card(all_cards_values)
    first_hand = FourOfKindFigure(four_a_kind, high_card)
    second_hand = FourOfKindFigure(four_a_kind, high_card)
    assert(EQUALITY == compare_two_four_of_kind_hands(first_hand, second_hand))

def compare_two_four_of_kind_hands(first_hand, second_hand):
    result = first_hand.compare_with_other_four_of_kind_hands(second_hand)
    return result