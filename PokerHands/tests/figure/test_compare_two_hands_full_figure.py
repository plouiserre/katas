import copy
import random

from PokerHands.card import CardValue
from PokerHands.AllFigures.FullFigure import FullFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_two_hands_with_differents_fulls():
    all_cards_values = [CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_hand_three_times_card = __get_high_cards(all_cards_values, CardValue.UNDEFINED)
    second_hand_three_times_card = __get_lower_cards(all_cards_values, first_hand_three_times_card)    
    all_cards_values_two_cards = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_two_cards = __get_random_card(all_cards_values_two_cards)
    second_two_cards = __get_random_card(all_cards_values_two_cards)
    first_hand = FullFigure(first_two_cards, first_hand_three_times_card)
    second_hand = FullFigure(second_two_cards, second_hand_three_times_card)
    assert(FIRST_HAND == compare_two_full_figure_hands(first_hand, second_hand))

def test_compare_two_hands_with_full_and_three_same_cards():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    three_of_kind = __get_random_card(all_cards_values)
    second_hand_two_times_card = __get_high_cards(all_cards_values, three_of_kind)
    first_hand_two_times_card = __get_lower_cards(all_cards_values, second_hand_two_times_card)
    first_hand = FullFigure(first_hand_two_times_card, three_of_kind)
    second_hand = FullFigure(second_hand_two_times_card, three_of_kind)
    assert(SECOND_HAND == compare_two_full_figure_hands(first_hand, second_hand))

def __get_high_cards(all_cards_values, three_of_kind):
    higher_two_times_cards = CardValue.UNDEFINED
    if CardValue.TWO in all_cards_values : 
        all_cards_values.remove(CardValue.TWO)
    if three_of_kind == CardValue.TWO :
        all_cards_values.remove(CardValue.THREE)
    higher_two_times_cards = __get_random_card(all_cards_values)
    if CardValue.TWO not in all_cards_values and three_of_kind != CardValue.TWO : 
        all_cards_values.append(CardValue.TWO)    
    if three_of_kind == CardValue.TWO :
        all_cards_values.append(CardValue.THREE)
    return higher_two_times_cards

def __get_lower_cards(all_cards_values, high_card):
    lower_two_times_cards = CardValue.UNDEFINED
    all_cards_values_copy = copy.deepcopy(all_cards_values)
    for card_value in all_cards_values_copy : 
        if high_card <= card_value : 
            all_cards_values.remove(card_value)
    lower_two_times_cards = __get_random_card(all_cards_values)
    return lower_two_times_cards

def test_compare_two_hands_with_same_fulls():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    three_of_kind = __get_random_card(all_cards_values)
    two_same = __get_random_card(all_cards_values)
    first_hand = FullFigure(two_same, three_of_kind)
    second_hand = FullFigure(two_same, three_of_kind)
    assert(EQUALITY == compare_two_full_figure_hands(first_hand, second_hand))

def __get_random_card(all_cards_values) : 
    index = random.randint(0, len(all_cards_values) - 1)
    random_card = all_cards_values[index]
    all_cards_values.remove(random_card)
    return random_card

def compare_two_full_figure_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_full_figure_hands(second_hand)
    return result