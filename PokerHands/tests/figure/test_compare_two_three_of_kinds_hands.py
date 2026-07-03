import copy
import random

from PokerHands.card import CardValue
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_where_two_hands_have_differents_three_of_kinds_with_first_hand_wininng():
    all_cards_values = [CardValue.TWO,  CardValue.SIX,  CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    high_three_of_cards = __get_high_card(all_cards_values)
    all_cards_values.extend([CardValue.THREE, CardValue.FOUR, CardValue.FIVE])
    low_three_of_cards = __get_second_card(all_cards_values, high_three_of_cards)
    random_first_hand = __get_random_card(all_cards_values)
    random_second_hand = __get_random_card(all_cards_values)
    first_hand = ThreeOfKindFigure(high_three_of_cards, random_first_hand)
    second_hand = ThreeOfKindFigure(low_three_of_cards, random_second_hand)
    assert(FIRST_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_differents_three_of_kinds_with_second_hand_wininng():
    all_cards_values = [CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    high_three_of_cards = __get_high_card(all_cards_values)
    low_three_of_cards = __get_second_card(all_cards_values, high_three_of_cards)
    all_cards_values.extend([CardValue.TWO, CardValue.THREE])
    random_first_hand = __get_random_card(all_cards_values)
    random_second_hand = __get_random_card(all_cards_values)
    first_hand = ThreeOfKindFigure(low_three_of_cards, random_first_hand)
    second_hand = ThreeOfKindFigure(high_three_of_cards, random_second_hand)
    assert(SECOND_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_but_differents_high_cards_with_first_hand_winning():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    random_three_of_card = __get_random_card(all_cards_values)
    high_three_of_cards = __get_high_card(all_cards_values)
    low_three_of_cards = __get_second_card(all_cards_values, high_three_of_cards)
    first_hand = ThreeOfKindFigure(random_three_of_card, high_three_of_cards)
    second_hand = ThreeOfKindFigure(random_three_of_card, low_three_of_cards)
    assert(FIRST_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_but_differents_high_cards_with_second_hand_winning():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    random_three_of_card = __get_random_card(all_cards_values)
    high_three_of_cards = __get_high_card(all_cards_values)
    low_three_of_cards = __get_second_card(all_cards_values, high_three_of_cards)
    first_hand = ThreeOfKindFigure(random_three_of_card, low_three_of_cards)
    second_hand = ThreeOfKindFigure(random_three_of_card, high_three_of_cards)
    assert(SECOND_HAND == compare_two_three_of_kind_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_and_same_high_cards():
    first_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    second_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    assert(EQUALITY == compare_two_three_of_kind_hands(first_hand, second_hand))

def __get_random_card(all_cards_values) : 
    index = random.randint(0, len(all_cards_values) - 1)
    random_card = all_cards_values[index]
    all_cards_values.remove(random_card)
    return random_card


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

def compare_two_three_of_kind_hands(first_hand, second_hand):
    result = first_hand.compare_with_other_three_of_kinds_hands(second_hand)
    return result