from PokerHands.card import Card, CardColor, CardValue
from PokerHands.Figure import FlushFigure
from PokerHands.detector.flush_detector import FlushDetector

def test_find_flush_hearts_by_king():
    hand = [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.HEARTS)]
    assert(__find_flush(hand) == FlushFigure(CardColor.HEARTS, CardValue.KING))

def test_find_flush_clubs_by_queen():
    hand = [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.CLUBS)]
    assert(__find_flush(hand) == FlushFigure(CardColor.CLUBS, CardValue.QUEEN))

def test_find_flush_spades_by_jack():
    hand = [Card(CardValue.SEVEN, CardColor.SPADES), Card(CardValue.THREE, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)]
    assert(__find_flush(hand) == FlushFigure(CardColor.SPADES, CardValue.JACK))

def __find_flush(hand) : 
    flush_detector = FlushDetector()
    return flush_detector.find_flush(hand)