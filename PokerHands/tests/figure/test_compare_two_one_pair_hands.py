import copy
import random

from PokerHands.card import CardValue
from PokerHands.AllFigures.PairFigure import PairFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_two_hands_with_different_pair_card_and_different_high_card_second_hand_win() :
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    best_pair_card = __get_high_card(all_cards_values)
    lower_pair_card = __get_second_card(all_cards_values, best_pair_card)
    all_cards_values_high_card = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_random_high_card = __get_random_card(all_cards_values_high_card)
    second_random_high_card = __get_random_card(all_cards_values_high_card)
    first_hand = PairFigure(lower_pair_card, first_random_high_card)
    second_hand = PairFigure(best_pair_card, second_random_high_card)
    assert(SECOND_HAND == compare_two_one_pair_hands(first_hand, second_hand))

def test_compare_two_hands_with_same_pair_card_and_different_high_card_first_hand_win() : 
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    pair_card = __get_random_card(all_cards_values)
    best_high_card = __get_high_card(all_cards_values)
    lower_high_card = __get_second_card(all_cards_values, best_high_card)
    first_hand = PairFigure(pair_card, best_high_card)
    second_hand = PairFigure(pair_card, lower_high_card)
    assert(FIRST_HAND == compare_two_one_pair_hands(first_hand, second_hand))

def test_compare_two_hands_with_same_pair_and_same_high_cards():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    pair_card = __get_random_card(all_cards_values)
    high_card = __get_random_card(all_cards_values)
    first_hand = PairFigure(pair_card, high_card)
    second_hand = PairFigure(pair_card, high_card)
    assert(EQUALITY == compare_two_one_pair_hands(first_hand, second_hand))

def __get_high_card(all_cards_values):
    high_card = CardValue.UNDEFINED
    if CardValue.TWO in all_cards_values :
        all_cards_values.remove(CardValue.TWO)
    high_card = __get_random_card(all_cards_values)
    if CardValue.TWO not in all_cards_values :
        all_cards_values.append(CardValue.TWO)
    return high_card

def __get_second_card(all_cards_values, high_card):
    second_card = CardValue.UNDEFINED
    all_cards_values_copy = copy.deepcopy(all_cards_values)
    for card_value in all_cards_values_copy : 
        if high_card <= card_value : 
            all_cards_values.remove(card_value)
    second_card = __get_random_card(all_cards_values)
    return second_card

def __get_random_card(all_cards_values) : 
    index = random.randint(0, len(all_cards_values) - 1)
    random_card = all_cards_values[index]
    all_cards_values.remove(random_card)
    return random_card

def compare_two_one_pair_hands(first_hand, second_hand):
    result = first_hand.compare_with_onther_one_pair_hand(second_hand)
    return result