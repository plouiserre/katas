from PokerHands.card import CardValue
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure 
from PokerHands.winner import FIRST_HAND, SECOND_HAND, EQUALITY
from PokerHands.tests.random_cards import add_cards, get_all_values, get_high_cards, get_lower_card, get_random_card, remove_cards

def test_compare_where_two_hands_have_differents_three_of_kinds_with_first_hand_wininng():
    all_cards_values = get_all_values()  
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR])
    high_three_of_cards = get_high_cards(all_cards_values)
    add_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR])
    low_three_of_cards = get_lower_card(all_cards_values, high_three_of_cards)
    random_first_hand = get_random_card(all_cards_values)
    random_second_hand = get_random_card(all_cards_values)
    first_hand = ThreeOfKindFigure(high_three_of_cards, random_first_hand)
    second_hand = ThreeOfKindFigure(low_three_of_cards, random_second_hand)
    assert(FIRST_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_differents_three_of_kinds_with_second_hand_wininng():
    all_cards_values = get_all_values()  
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR])
    high_three_of_cards = get_high_cards(all_cards_values)
    add_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR])
    low_three_of_cards = get_lower_card(all_cards_values, high_three_of_cards)
    random_first_hand = get_random_card(all_cards_values)
    random_second_hand = get_random_card(all_cards_values)
    first_hand = ThreeOfKindFigure(low_three_of_cards, random_first_hand)
    second_hand = ThreeOfKindFigure(high_three_of_cards, random_second_hand)
    assert(SECOND_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_but_differents_high_cards_with_first_hand_winning():
    all_cards_values = get_all_values()  
    random_three_of_card = get_random_card(all_cards_values)
    high_three_of_cards = get_high_cards(all_cards_values)
    low_three_of_cards = get_lower_card(all_cards_values, high_three_of_cards)
    first_hand = ThreeOfKindFigure(random_three_of_card, high_three_of_cards)
    second_hand = ThreeOfKindFigure(random_three_of_card, low_three_of_cards)
    assert(FIRST_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_but_differents_high_cards_with_second_hand_winning():
    all_cards_values = get_all_values()    
    random_three_of_card = get_random_card(all_cards_values)
    high_three_of_cards = get_high_cards(all_cards_values)
    low_three_of_cards = get_lower_card(all_cards_values, high_three_of_cards)
    first_hand = ThreeOfKindFigure(random_three_of_card, low_three_of_cards)
    second_hand = ThreeOfKindFigure(random_three_of_card, high_three_of_cards)
    assert(SECOND_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_and_same_high_cards():
    first_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    second_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    assert(EQUALITY == compare_two_three_of_kind_hands(first_hand, second_hand))

def compare_two_three_of_kind_hands(first_hand, second_hand):
    result = first_hand.compare_with_other_three_of_kinds_hands(second_hand)
    return result