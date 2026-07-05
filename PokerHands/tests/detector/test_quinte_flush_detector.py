from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHands.tests.random_cards import get_all_values, get_random_card, get_colors_random, get_shuffle_hand, remove_cards

def test_find_quinte_flush_diamonds_with_nine_value():
    hand = [Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(__find_quinte_flush(hand) == QuinteFlushFigure(CardValue.NINE, CardColor.DIAMONDS))

def test_find_quinte_flush_random_colors__with_six_value():
    color_value = get_colors_random()
    all_cards_values = get_all_values()
    remove_cards(all_cards_values, [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE])
    top_quinte_flush = get_random_card(all_cards_values)
    second_card = top_quinte_flush - 1
    third_card = top_quinte_flush - 2
    fourth_card = top_quinte_flush - 3
    fifth_card = top_quinte_flush - 4
    hand = [Card(top_quinte_flush, color_value), Card(second_card, color_value), Card(third_card, color_value), Card(fourth_card, color_value), Card(fifth_card, color_value)]
    get_shuffle_hand(hand)
    assert(__find_quinte_flush(hand) == QuinteFlushFigure(top_quinte_flush, color_value))

def __find_quinte_flush(hand):
    quinte_flush_detector = QuinteFlushDetector()
    return quinte_flush_detector.find_quinte_flush(hand)