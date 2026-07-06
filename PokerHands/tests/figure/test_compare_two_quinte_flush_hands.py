from PokerHands.card import CardValue, CardColor
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure 
from PokerHands.winner import FIRST_HAND, SECOND_HAND
from PokerHands.tests.random_cards import get_all_values, get_colors_random, get_high_cards, get_lower_card

def test_compare_two_quinte_flush_first_hand_win():
    first_color = get_colors_random()
    second_color = get_colors_random()
    all_cards_values = get_all_values()    
    high_high_card = get_high_cards(all_cards_values)
    lower_high_card = get_lower_card(all_cards_values, high_high_card)
    first_hand = QuinteFlushFigure(high_high_card, first_color)
    second_hand = QuinteFlushFigure(lower_high_card, second_color)
    assert(FIRST_HAND == compare_two_quinte_flushs_hands(first_hand, second_hand))

def test_compare_two_quinte_flush_second_hand_win():
    first_color = get_colors_random()
    second_color = get_colors_random()
    all_cards_values = get_all_values()        
    high_high_card = get_high_cards(all_cards_values)
    lower_high_card = get_lower_card(all_cards_values, high_high_card)
    first_hand = QuinteFlushFigure(lower_high_card, first_color)
    second_hand = QuinteFlushFigure(high_high_card, second_color)
    assert(SECOND_HAND == compare_two_quinte_flushs_hands(first_hand, second_hand))

def compare_two_quinte_flushs_hands(first_hand, second_hand):
    result = first_hand.compare_with_other_quinte_flush_hands(second_hand)
    return result