import copy
import random

from PokerHands.card import CardValue
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_two_four_a_kind():
    all_cards_values = [CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    four_a_kind_high = __get_random_card(all_cards_values)
    four_a_kind_lower = __get_four_a_kind_lower(all_cards_values, four_a_kind_high)
    all_cards_values_other_card = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    lower_card_first_hand = __get_random_card(all_cards_values_other_card)
    lower_card_second_hand = __get_random_card(all_cards_values_other_card)
    first_hand = FourOfKindFigure(four_a_kind_lower, lower_card_first_hand)
    second_hand = FourOfKindFigure(four_a_kind_high, lower_card_second_hand)
    assert(SECOND_HAND == compare_two_four_of_kind_hands(first_hand, second_hand))

def __get_four_a_kind_lower(all_cards_values, four_a_kind_high):
    four_a_kind_lower = CardValue.UNDEFINED
    all_cards_values.append(CardValue.TWO)
    all_cards_values_copy = copy.deepcopy(all_cards_values)
    for card_value in all_cards_values_copy : 
        if four_a_kind_high <= card_value : 
            all_cards_values.remove(card_value)
    four_a_kind_lower = __get_random_card(all_cards_values)
    return four_a_kind_lower

def test_compare_two_four_a_kind_exactly_with_differents_high_cards():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    four_a_kind = __get_random_card(all_cards_values)
    first_hand_high_card = __get_high_card(all_cards_values)
    second_hand_high_card = __get_second_card(all_cards_values, first_hand_high_card)
    first_hand = FourOfKindFigure(four_a_kind, first_hand_high_card)
    second_hand = FourOfKindFigure(four_a_kind, second_hand_high_card)
    assert(FIRST_HAND == compare_two_four_of_kind_hands(first_hand, second_hand))

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

def test_compare_two_four_a_kind_with_same_cards():    
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    four_a_kind = __get_random_card(all_cards_values)
    high_card = __get_random_card(all_cards_values)
    first_hand = FourOfKindFigure(four_a_kind, high_card)
    second_hand = FourOfKindFigure(four_a_kind, high_card)
    assert(EQUALITY == compare_two_four_of_kind_hands(first_hand, second_hand))

def __get_random_card(all_cards_values) : 
    index = random.randint(0, len(all_cards_values) - 1)
    random_card = all_cards_values[index]
    all_cards_values.remove(random_card)
    return random_card

def compare_two_four_of_kind_hands(first_hand, second_hand):
    result = first_hand.compare_with_other_four_of_kind_hands(second_hand)
    return result