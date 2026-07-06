from PokerHands.card import CardValue
from PokerHands.AllFigures.FullFigure import FullFigure 
from PokerHands.winner import Winner
from PokerHands.tests.random_cards import add_cards, get_all_values, get_high_cards, get_lower_card, get_random_card, remove_cards

def test_compare_two_hands_with_differents_fulls():
    all_cards_values = get_all_values()
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE])
    first_hand_three_times_card = CardValue.SIX
    add_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE])
    second_hand_three_times_card = get_lower_card(all_cards_values, first_hand_three_times_card)    
    first_two_cards = get_random_card(all_cards_values)
    second_two_cards = get_random_card(all_cards_values)
    first_hand = FullFigure(first_two_cards, first_hand_three_times_card)
    second_hand = FullFigure(second_two_cards, second_hand_three_times_card)
    assert(Winner.FIRST_HAND == compare_two_full_figure_hands(first_hand, second_hand))

def test_compare_two_hands_with_full_and_three_same_cards():
    all_cards_values = get_all_values()    
    three_of_kind = get_random_card(all_cards_values)
    second_hand_two_times_card = get_high_cards(all_cards_values)
    first_hand_two_times_card = get_lower_card(all_cards_values, second_hand_two_times_card)
    first_hand = FullFigure(first_hand_two_times_card, three_of_kind)
    second_hand = FullFigure(second_hand_two_times_card, three_of_kind)
    assert(Winner.SECOND_HAND == compare_two_full_figure_hands(first_hand, second_hand))

def test_compare_two_hands_with_same_fulls():
    all_cards_values = get_all_values()    
    three_of_kind = get_random_card(all_cards_values)
    two_same = get_random_card(all_cards_values)
    first_hand = FullFigure(two_same, three_of_kind)
    second_hand = FullFigure(two_same, three_of_kind)
    assert(Winner.EQUALITY == compare_two_full_figure_hands(first_hand, second_hand))

def compare_two_full_figure_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_full_figure_hands(second_hand)
    return result