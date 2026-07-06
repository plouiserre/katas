from PokerHands.card import CardValue
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure 
from PokerHands.winner import Winner
from PokerHands.tests.random_cards import add_cards, get_all_values, get_high_cards, get_lower_card, get_random_card, remove_cards

def test_compare_two_pairs_with_first_pair_difference_first_hand_winning():    
    all_cards_values = get_all_values()    
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX])
    first_pair_first_hand_high = get_high_cards(all_cards_values)
    add_cards(all_cards_values, [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX])
    first_pair_second_hand_low = get_lower_card(all_cards_values, first_pair_first_hand_high)
    second_pair_first_hand_random = get_lower_card(all_cards_values, first_pair_first_hand_high)
    second_pair_second_hand_random = get_lower_card(all_cards_values, first_pair_first_hand_high)
    high_card_first_hand = get_random_card(all_cards_values)
    high_card_second_hand = get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_first_hand_high, second_pair_first_hand_random, high_card_first_hand)
    second_hand = TwoPairFigure(first_pair_second_hand_low, second_pair_second_hand_random, high_card_second_hand)
    assert(Winner.FIRST_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_with_first_pair_difference_second_hand_winning():    
    all_cards_values = get_all_values()    
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX])
    first_pair_first_hand_high = get_high_cards(all_cards_values)
    add_cards(all_cards_values, [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX])
    first_pair_second_hand_low = get_lower_card(all_cards_values, first_pair_first_hand_high)
    second_pair_first_hand_random = get_lower_card(all_cards_values, first_pair_first_hand_high)
    second_pair_second_hand_random = get_lower_card(all_cards_values, first_pair_first_hand_high)
    high_card_first_hand = get_random_card(all_cards_values)
    high_card_second_hand = get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_second_hand_low, second_pair_first_hand_random, high_card_first_hand)
    second_hand = TwoPairFigure(first_pair_first_hand_high, second_pair_second_hand_random, high_card_second_hand)
    assert(Winner.SECOND_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_with_same_pair_in_first_pair_and_second_pair_highter_in_first_hand():
    all_cards_values = get_all_values()
    first_pair_all_hands_random = get_random_card(all_cards_values)  
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX])
    second_pair_first_hand_random = get_high_cards(all_cards_values)
    add_cards(all_cards_values, [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX])
    second_pair_second_hand_random = get_lower_card(all_cards_values, second_pair_first_hand_random)
    high_card_first_hand = get_random_card(all_cards_values)
    high_card_second_hand = get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_all_hands_random, second_pair_first_hand_random, high_card_first_hand)
    second_hand = TwoPairFigure(first_pair_all_hands_random, second_pair_second_hand_random, high_card_second_hand)
    assert(Winner.FIRST_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_with_king_pairs_in_each_hand_and_second_pair_highter_in_second_hand():
    all_cards_values = get_all_values()    
    first_pair_all_hands_random = get_random_card(all_cards_values)  
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX])     
    second_pair_first_hand_random = get_high_cards(all_cards_values)
    add_cards(all_cards_values, [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX])
    second_pair_second_hand_random = get_lower_card(all_cards_values, second_pair_first_hand_random)
    high_card_first_hand = get_random_card(all_cards_values)
    high_card_second_hand = get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_all_hands_random, second_pair_second_hand_random, high_card_first_hand)
    second_hand = TwoPairFigure(first_pair_all_hands_random, second_pair_first_hand_random, high_card_second_hand)
    assert(Winner.SECOND_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_different_high_cards_first_hand_winning():
    all_cards_values = get_all_values()    
    first_pair_value = get_random_card(all_cards_values)
    second_pair_value = get_random_card(all_cards_values)
    high_high_card = get_high_cards(all_cards_values)
    low_high_card = get_lower_card(all_cards_values, high_high_card)
    first_hand = TwoPairFigure(first_pair_value, second_pair_value, high_high_card)
    second_hand = TwoPairFigure(first_pair_value, second_pair_value, low_high_card)
    assert(Winner.FIRST_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_different_high_cards_second_hand_winning():
    all_cards_values = get_all_values()    
    first_pair_value = get_random_card(all_cards_values)
    second_pair_value = get_random_card(all_cards_values)
    high_high_card = get_high_cards(all_cards_values)
    low_high_card = get_lower_card(all_cards_values, high_high_card)
    first_hand = TwoPairFigure(first_pair_value, second_pair_value, low_high_card)
    second_hand = TwoPairFigure(first_pair_value, second_pair_value, high_high_card)
    assert(Winner.SECOND_HAND == compare_two_pairs_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_same_high_cards_randomly():
    all_cards_values = get_all_values()        
    first_pair_value = get_random_card(all_cards_values)
    second_pair_value = get_random_card(all_cards_values)
    high_card = get_random_card(all_cards_values)
    first_hand = TwoPairFigure(first_pair_value, second_pair_value, high_card)
    second_hand = TwoPairFigure(first_pair_value, second_pair_value, high_card)
    assert(Winner.EQUALITY == compare_two_pairs_hands(first_hand, second_hand))

def compare_two_pairs_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_two_pairs_hands(second_hand)
    return result