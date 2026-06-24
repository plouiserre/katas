from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.AllFigures.StraitFigure import StraitFigure
from PokerHands.detector.straight_detector import StraightDetector

def test_find_straight_finish_six():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.THREE, CardColor.SPADES)]
    assert(__find_straight_cards(hand)==StraitFigure(CardValue.SIX))

def test_find_straight_finish_jack():
    hand =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(__find_straight_cards(hand)==StraitFigure(CardValue.JACK))

def test_find_straight_finish_ace():
    hand =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)]
    assert(__find_straight_cards(hand)==StraitFigure(CardValue.ACE))

def __find_straight_cards(hand):
    counting_cards = CountingCards()
    straight_detector = StraightDetector(counting_cards)
    return straight_detector.find_straight(hand)
    
