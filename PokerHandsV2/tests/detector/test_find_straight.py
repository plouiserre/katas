from PokerHandsV2.card import Card, CardColor, CardValue
from PokerHandsV2.manipulating_cards import ManipulatingCards
from PokerHandsV2.AllFigures.QuinteFigure import QuinteFigure
from PokerHandsV2.detector.quinte_detector import QuinteDetector

def test_find_quinte_finish_six():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.THREE, CardColor.SPADES)]
    assert(__find_quinte_cards(hand)==QuinteFigure(CardValue.SIX))

def test_find_quinte_finish_jack():
    hand =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(__find_quinte_cards(hand)==QuinteFigure(CardValue.JACK))

def test_find_quinte_finish_ace():
    hand =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)]
    assert(__find_quinte_cards(hand)==QuinteFigure(CardValue.ACE))

def __find_quinte_cards(hand):
    manipulating_cards = ManipulatingCards()
    quinte_detector = QuinteDetector(manipulating_cards)
    return quinte_detector.find_quinte(hand)
    
