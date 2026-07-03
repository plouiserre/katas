import copy
import random 

from PokerHands.AllFigures.FlushFigure import FlushFigure 
from PokerHands.card import CardValue, CardColor
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY
from PokerHands.tests.random_cards import get_all_colors, get_all_high_cards, get_all_values, get_colors_random, get_lower_card

def test_compare_where_each_hand_have_differents_flush(): 
    first_hand = FlushFigure(CardColor.SPADES, CardValue.EIGHT)
    second_hand = FlushFigure(CardColor.CLUBS, CardValue.SEVEN)
    assert(FIRST_HAND == compare_two_flush_hands(first_hand, second_hand))

def test_compare_where_each_hand_have_same_flush(): 
    first_hand = FlushFigure(CardColor.HEARTS, CardValue.ACE)
    second_hand = FlushFigure(CardColor.DIAMONDS, CardValue.ACE)
    assert(EQUALITY == compare_two_flush_hands(first_hand, second_hand))

def test_compare_randomise_flush_with_first_hand_win(): 
    all_cards_values = get_all_values()
    high_card  = get_all_high_cards(all_cards_values)
    lower_card_value = get_lower_card(all_cards_values, high_card)
    high_card_color = get_colors_random()
    lower_card_color = get_colors_random()
    first_hand = FlushFigure(high_card_color, high_card)
    second_hand = FlushFigure(lower_card_color, lower_card_value)
    assert(FIRST_HAND == compare_two_flush_hands(first_hand, second_hand))

def test_compare_randomise_flush_with_second_hand_win(): 
    all_cards_values = get_all_values()
    high_card  = get_all_high_cards(all_cards_values)
    lower_card_value = get_lower_card(all_cards_values, high_card)
    high_card_color = get_colors_random()
    lower_card_color = get_colors_random()
    first_hand = FlushFigure(lower_card_color, lower_card_value) 
    second_hand = FlushFigure(high_card_color, high_card)
    assert(SECOND_HAND == compare_two_flush_hands(first_hand, second_hand))

def test_compare_randomise_flush_with_equality(): 
    all_cards_values = get_all_values()
    high_card  = get_all_high_cards(all_cards_values)
    high_card_color = get_colors_random()
    lower_card_color = get_colors_random()
    first_hand = FlushFigure(lower_card_color, high_card) 
    second_hand = FlushFigure(high_card_color, high_card)
    assert(EQUALITY == compare_two_flush_hands(first_hand, second_hand))

def compare_two_flush_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_flush_hands(second_hand)
    return result