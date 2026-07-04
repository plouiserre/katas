import copy
import random

from PokerHands.card import CardValue
from PokerHands.AllFigures.PairFigure import PairFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY
from PokerHands.tests.random_cards import add_cards, get_all_values, get_high_cards, get_lower_card, get_random_card, remove_cards

def test_compare_two_hands_with_different_pair_card_and_different_high_card_second_hand_win() :
    all_cards_values = get_all_values()
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR])    
    best_pair_card = get_high_cards(all_cards_values)
    add_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR])
    lower_pair_card = get_lower_card(all_cards_values, best_pair_card)
    first_random_high_card = get_random_card(all_cards_values)
    second_random_high_card = get_random_card(all_cards_values)
    first_hand = PairFigure(lower_pair_card, first_random_high_card)
    second_hand = PairFigure(best_pair_card, second_random_high_card)
    assert(SECOND_HAND == compare_two_one_pair_hands(first_hand, second_hand))

def test_compare_two_hands_with_same_pair_card_and_different_high_card_first_hand_win() : 
    all_cards_values = get_all_values()    
    pair_card = get_random_card(all_cards_values)
    best_high_card = get_high_cards(all_cards_values)
    lower_high_card = get_lower_card(all_cards_values, best_high_card)
    first_hand = PairFigure(pair_card, best_high_card)
    second_hand = PairFigure(pair_card, lower_high_card)
    assert(FIRST_HAND == compare_two_one_pair_hands(first_hand, second_hand))

def test_compare_two_hands_with_same_pair_and_same_high_cards():
    all_cards_values = get_all_values()    
    pair_card = get_random_card(all_cards_values)
    high_card = get_random_card(all_cards_values)
    first_hand = PairFigure(pair_card, high_card)
    second_hand = PairFigure(pair_card, high_card)
    assert(EQUALITY == compare_two_one_pair_hands(first_hand, second_hand))

def compare_two_one_pair_hands(first_hand, second_hand):
    result = first_hand.compare_with_onther_one_pair_hand(second_hand)
    return result