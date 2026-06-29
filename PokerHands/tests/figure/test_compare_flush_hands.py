import copy
import random 

from PokerHands.card import CardValue, CardColor
from PokerHands.AllFigures.FlushFigure import FlushFigure 
from PokerHands.score_tmp import FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_where_each_hand_have_differents_flush(): 
    first_hand = FlushFigure(CardColor.SPADES, CardValue.EIGHT)
    second_hand = FlushFigure(CardColor.CLUBS, CardValue.SEVEN)
    assert(FIRST_HAND == compare_two_flush_hands(first_hand, second_hand))

def test_compare_where_each_hand_have_same_flush(): 
    first_hand = FlushFigure(CardColor.HEARTS, CardValue.ACE)
    second_hand = FlushFigure(CardColor.DIAMONDS, CardValue.ACE)
    assert(EQUALITY == compare_two_flush_hands(first_hand, second_hand))

def test_compare_randomise_flush_with_first_hand_win(): 
    high_card  = __get_high_card_value()
    all_colors = [CardColor.CLUBS, CardColor.DIAMONDS, CardColor.HEARTS, CardColor.SPADES]
    lower_card_value = __get_lower_card_value(high_card)
    high_card_color = __get_colors_random(all_colors)
    lower_card_color = __get_colors_random(all_colors)
    first_hand = FlushFigure(high_card_color, high_card)
    second_hand = FlushFigure(lower_card_color, lower_card_value)
    assert(FIRST_HAND == compare_two_flush_hands(first_hand, second_hand))

def test_compare_randomise_flush_with_second_hand_win(): 
    high_card  = __get_high_card_value()
    print(high_card)
    all_colors = [CardColor.CLUBS, CardColor.DIAMONDS, CardColor.HEARTS, CardColor.SPADES]
    lower_card_value = __get_lower_card_value(high_card)
    print(lower_card_value)
    high_card_color = __get_colors_random(all_colors)
    lower_card_color = __get_colors_random(all_colors)
    first_hand = FlushFigure(lower_card_color, lower_card_value) 
    second_hand = FlushFigure(high_card_color, high_card)
    assert(SECOND_HAND == compare_two_flush_hands(first_hand, second_hand))

def test_compare_randomise_flush_with_equality(): 
    card_value  = __get_high_card_value()
    all_colors = [CardColor.CLUBS, CardColor.DIAMONDS, CardColor.HEARTS, CardColor.SPADES]
    high_card_color = __get_colors_random(all_colors)
    lower_card_color = __get_colors_random(all_colors)
    first_hand = FlushFigure(lower_card_color, card_value) 
    second_hand = FlushFigure(high_card_color, card_value)
    assert(EQUALITY == compare_two_flush_hands(first_hand, second_hand))

def __get_high_card_value():
    all_cards_values = [CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    index = random.randint(0, len(all_cards_values) - 1)
    pair_value = all_cards_values[index]
    return pair_value

def __get_lower_card_value(high_card_value):
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]    
    all_cards_values_copy = copy.deepcopy(all_cards_values)
    for card_value in all_cards_values_copy : 
        if high_card_value <= card_value : 
            all_cards_values.remove(card_value)
    index_lower_card = random.randint(0, len(all_cards_values) - 1)
    lower_card_value = all_cards_values[index_lower_card]
    return lower_card_value

def __get_colors_random(all_colors):
    index_card_color = random.randint(0, len(all_colors) - 1)
    card_color = all_colors[index_card_color]
    all_colors.remove(card_color)
    return card_color

def compare_two_flush_hands(first_hand, second_hand): 
    result = first_hand.compare_with_other_flush_hands(second_hand)
    return result