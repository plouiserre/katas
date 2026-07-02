import random 
import copy

from PokerHands.card import CardValue
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

#le problème vient du fait que ce sont deux pairs donc il faut retravailler le random!!!!

def test_compare_two_pairs_with_first_pair_difference_first_hand_winning():    
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    all_cards_values = [CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_pair_first_hand_high = __get_high_card(all_cards_values)
    all_cards_values.extend([CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,CardValue.SIX])
    first_pair_second_hand_low = __get_second_card(all_cards_values, first_pair_first_hand_high)
    second_pair_first_hand_random = __get_second_card(all_cards_values, first_pair_first_hand_high)
    second_pair_second_hand_random = __get_second_card(all_cards_values, first_pair_first_hand_high)
    high_card_first_hand = __get_random_card(all_cards_values)
    high_card_second_hand = __get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_first_hand_high, second_pair_first_hand_random, high_card_first_hand)
    second_hand = TwoPairFigure(first_pair_second_hand_low, second_pair_second_hand_random, high_card_second_hand)
    assert(FIRST_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_with_first_pair_difference_second_hand_winning():    
    all_cards_values = [CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_pair_first_hand_high = __get_high_card(all_cards_values)
    all_cards_values.extend([CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,CardValue.SIX])
    first_pair_second_hand_low = __get_second_card(all_cards_values, first_pair_first_hand_high)
    second_pair_first_hand_random = __get_second_card(all_cards_values, first_pair_first_hand_high)
    second_pair_second_hand_random = __get_second_card(all_cards_values, first_pair_first_hand_high)
    high_card_first_hand = __get_random_card(all_cards_values)
    high_card_second_hand = __get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_second_hand_low, second_pair_first_hand_random, high_card_first_hand)
    second_hand = TwoPairFigure(first_pair_first_hand_high, second_pair_second_hand_random, high_card_second_hand)
    assert(SECOND_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_with_same_pair_in_first_pair_and_second_pair_highter_in_first_hand():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, 
                        CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_pair_all_hands_random = __get_random_card(all_cards_values)  
    if CardValue.TWO in all_cards_values :
        all_cards_values.remove(CardValue.TWO)      
    if CardValue.THREE in all_cards_values :
        all_cards_values.remove(CardValue.THREE)  
    if CardValue.FOUR in all_cards_values :
        all_cards_values.remove(CardValue.FOUR)  
    if CardValue.FIVE in all_cards_values :
        all_cards_values.remove(CardValue.FIVE)  
    if CardValue.SIX in all_cards_values :
        all_cards_values.remove(CardValue.SIX)  
    second_pair_first_hand_random = __get_high_card(all_cards_values)
    all_cards_values.extend([CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,CardValue.SIX])
    second_pair_second_hand_random = __get_second_card(all_cards_values, second_pair_first_hand_random)
    high_card_first_hand = __get_random_card(all_cards_values)
    high_card_second_hand = __get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_all_hands_random, second_pair_first_hand_random, high_card_first_hand)
    second_hand = TwoPairFigure(first_pair_all_hands_random, second_pair_second_hand_random, high_card_second_hand)
    assert(FIRST_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_with_king_pairs_in_each_hand_and_second_pair_highter_in_second_hand():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, 
                        CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_pair_all_hands_random = __get_random_card(all_cards_values)  
    if CardValue.TWO in all_cards_values :
        all_cards_values.remove(CardValue.TWO)      
    if CardValue.THREE in all_cards_values :
        all_cards_values.remove(CardValue.THREE)  
    if CardValue.FOUR in all_cards_values :
        all_cards_values.remove(CardValue.FOUR)  
    if CardValue.FIVE in all_cards_values :
        all_cards_values.remove(CardValue.FIVE)  
    if CardValue.SIX in all_cards_values :
        all_cards_values.remove(CardValue.SIX)  
    second_pair_first_hand_random = __get_high_card(all_cards_values)
    all_cards_values.extend([CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,CardValue.SIX])
    second_pair_second_hand_random = __get_second_card(all_cards_values, second_pair_first_hand_random)
    high_card_first_hand = __get_random_card(all_cards_values)
    high_card_second_hand = __get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_all_hands_random, second_pair_second_hand_random, high_card_first_hand)
    second_hand = TwoPairFigure(first_pair_all_hands_random, second_pair_first_hand_random, high_card_second_hand)
    assert(SECOND_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_different_high_cards_first_hand_winning():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, 
                        CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_pair_value = __get_random_card(all_cards_values)
    second_pair_value = __get_random_card(all_cards_values)
    if CardValue.TWO in all_cards_values : 
        all_cards_values.remove(CardValue.TWO)
    high_high_card = __get_high_card(all_cards_values)
    low_high_card = __get_second_card(all_cards_values, high_high_card)
    first_hand = TwoPairFigure(first_pair_value, second_pair_value, high_high_card)
    second_hand = TwoPairFigure(first_pair_value, second_pair_value, low_high_card)
    assert(FIRST_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_different_high_cards_second_hand_winning():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, 
                        CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_pair_value = __get_random_card(all_cards_values)
    second_pair_value = __get_random_card(all_cards_values)
    if CardValue.TWO in all_cards_values : 
        all_cards_values.remove(CardValue.TWO)
    high_high_card = __get_high_card(all_cards_values)
    low_high_card = __get_second_card(all_cards_values, high_high_card)
    first_hand = TwoPairFigure(first_pair_value, second_pair_value, low_high_card)
    second_hand = TwoPairFigure(first_pair_value, second_pair_value, high_high_card)
    assert(SECOND_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_same_high_cards_randomly():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, 
                        CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    first_pair_value = __get_random_card(all_cards_values)
    second_pair_value = __get_random_card(all_cards_values)
    high_card = __get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_value, second_pair_value, high_card)
    second_hand = TwoPairFigure(first_pair_value, second_pair_value, high_card)
    assert(EQUALITY == compare_two_pairs_hands(first_hand, second_hand))

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

def compare_two_pairs_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_two_pairs_hands(second_hand)
    return result