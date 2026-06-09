from PokerHands.card import Card, CardColor, CardValue
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.Figure import HighCardFigure

def test_find_high_card_king():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.KING, CardColor.SPADES)]
    assert(__find_high_card(hand)== HighCardFigure(CardValue.KING))

def test_find_high_card_queen():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.QUEEN))

def test_find_high_card_jack():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.JACK))

def test_find_high_card_ten():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.TEN))

def test_find_high_card_nine():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.NINE))

def test_find_high_card_eight():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.EIGHT))

def test_find_high_card_seven():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.SEVEN))

def __find_high_card(hand):
    _high_card_detector = HighCardDetector()
    return _high_card_detector.find_high_card(hand)