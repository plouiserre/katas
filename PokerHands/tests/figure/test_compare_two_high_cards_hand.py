from PokerHands.AllFigures.HighCardFigure import HighCardFigure 
from PokerHands.winner import Winner
from PokerHands.tests.random_cards import get_all_values, get_high_cards, get_lower_card

def test_compare_one_hand_with_random_values_but_second_hand_better(): 
    all_cards_values = get_all_values()    
    high_card = get_high_cards(all_cards_values)
    lower_card = get_lower_card(all_cards_values, high_card)
    first_hand = HighCardFigure(lower_card)
    second_hand = HighCardFigure(high_card)
    assert(Winner.SECOND_HAND == compare_two_high_cards_hands(first_hand, second_hand))

def test_compare_one_hand_with_random_values_but_first_hand_better(): 
    all_cards_values = get_all_values()    
    high_card = get_high_cards(all_cards_values)
    lower_card = get_lower_card(all_cards_values, high_card)
    first_hand =  HighCardFigure(high_card)
    second_hand = HighCardFigure(lower_card)
    assert(Winner.FIRST_HAND == compare_two_high_cards_hands(first_hand, second_hand))

def test_compare_two_hands_with_high_cards_random_equality():
    all_cards_values = get_all_values()    
    high_card = get_high_cards(all_cards_values)
    first_hand = HighCardFigure(high_card)
    second_hand = HighCardFigure(high_card)
    assert(Winner.EQUALITY == compare_two_high_cards_hands(first_hand, second_hand))

def compare_two_high_cards_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_high_cards_hands(second_hand)
    return result