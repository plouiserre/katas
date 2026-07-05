from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.detector.flush_detector import FlushDetector
from PokerHands.tests.random_cards import add_cards, get_all_values, get_colors_random, get_high_cards, get_random_card, get_shuffle_hand, remove_cards

def test_find_flush_hearts_by_king():
    hand = [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.HEARTS)]
    assert(__find_flush(hand) == FlushFigure(CardColor.HEARTS, CardValue.KING))

def test_find_flush_clubs_by_queen():
    hand = [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.CLUBS)]
    assert(__find_flush(hand) == FlushFigure(CardColor.CLUBS, CardValue.QUEEN))

def test_find_flush_randomise(): 
    color_choose = get_colors_random()
    all_cards_values = get_all_values()
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE])
    first_card_value = get_high_cards(all_cards_values)
    add_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE ])
    second_card_value = get_random_card(all_cards_values)
    third_card_value = get_random_card(all_cards_values)
    fourth_card_value = get_random_card(all_cards_values)
    fifth_card_value = get_random_card(all_cards_values)
    
    hand = [Card(first_card_value, color_choose), Card(second_card_value, color_choose), 
            Card(third_card_value, color_choose), Card(fourth_card_value, color_choose), 
            Card(fifth_card_value, color_choose)]
    get_shuffle_hand(hand)
    
    assert(__find_flush(hand) == FlushFigure(color_choose, first_card_value))
    
def __find_flush(hand) : 
    flush_detector = FlushDetector()
    return flush_detector.find_flush(hand)