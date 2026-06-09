from PokerHands.card import Card, CardColor, CardValue
from PokerHands.Figure import QuinteFlush
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector

def test_find_quinte_flush_diamonds_with_nine_value():
    hand = [Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(__find_quinte_flush(hand) == QuinteFlush(CardValue.NINE, CardColor.DIAMONDS))

def test_find_quinte_flush_diamonds_with_six_value():
    hand = [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.CLUBS)]
    assert(__find_quinte_flush(hand) == QuinteFlush(CardValue.SIX, CardColor.CLUBS))

def __find_quinte_flush(hand):
    quinte_flush_detector = QuinteFlushDetector()
    return quinte_flush_detector.find_quinte_flush(hand)