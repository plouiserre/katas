import random

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector

def test_find_quinte_flush_diamonds_with_nine_value():
    hand = [Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(__find_quinte_flush(hand) == QuinteFlushFigure(CardValue.NINE, CardColor.DIAMONDS))

def test_find_quinte_flush_random_colors__with_six_value():
    colors = [CardColor.CLUBS, CardColor.DIAMONDS, CardColor.HEARTS, CardColor.SPADES]
    index = random.randint(0, len(colors) - 1)
    color_value = colors[index]
    hand = [Card(CardValue.TWO, color_value), Card(CardValue.FOUR, color_value), Card(CardValue.SIX, color_value), Card(CardValue.FIVE, color_value), Card(CardValue.THREE, color_value)]
    assert(__find_quinte_flush(hand) == QuinteFlushFigure(CardValue.SIX, color_value))

def __find_quinte_flush(hand):
    quinte_flush_detector = QuinteFlushDetector()
    return quinte_flush_detector.find_quinte_flush(hand)