import copy
import random

from PokerHands.card import CardValue
from PokerHands.AllFigures.HighCardFigure import HighCardFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_one_hand_with_random_values_but_second_hand_better(): 
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    high_card = __get_high_card(all_cards_values)
    lower_card = __get_second_card(all_cards_values, high_card)
    first_hand = HighCardFigure(lower_card)
    second_hand = HighCardFigure(high_card)
    assert(SECOND_HAND == compare_two_high_cards_hands(first_hand, second_hand))

def test_compare_one_hand_with_random_values_but_first_hand_better(): 
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    high_card = __get_high_card(all_cards_values)
    lower_card = __get_second_card(all_cards_values, high_card)
    first_hand =  HighCardFigure(high_card)
    second_hand = HighCardFigure(lower_card)
    assert(FIRST_HAND == compare_two_high_cards_hands(first_hand, second_hand))

def test_compare_two_hands_with_high_cards_random_equality():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    high_card = __get_random_card(all_cards_values)
    first_hand = HighCardFigure(high_card)
    second_hand = HighCardFigure(high_card)
    assert(EQUALITY == compare_two_high_cards_hands(first_hand, second_hand))

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

def compare_two_high_cards_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_high_cards_hands(second_hand)
    return result