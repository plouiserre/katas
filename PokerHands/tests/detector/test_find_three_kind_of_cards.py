from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.detector.three_cards_detector import ThreeCardsDetector

def test_find_three_of_a_two(): 
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.TWO, CardValue.ACE))

def test_find_three_of_a_three(): 
    hand =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.THREE, CardValue.FOUR))

def test_find_three_of_a_four(): 
    hand =  [Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.FOUR, CardValue.THREE))

def test_find_three_of_a_five(): 
    hand =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.FIVE, CardValue.FOUR))

def test_find_three_of_a_six(): 
    hand =  [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.SIX, CardValue.FOUR))

def test_find_three_of_a_seven(): 
    hand =  [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.SEVEN, CardValue.SIX))

def test_find_three_of_a_eight(): 
    hand =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.EIGHT, CardValue.SEVEN))

def test_find_three_of_a_nine(): 
    hand =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.NINE, CardValue.EIGHT))

def test_find_three_of_a_ten(): 
    hand =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.TEN, CardValue.QUEEN))

def test_find_three_of_a_jack(): 
    hand =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.JACK, CardValue.QUEEN))

def test_find_three_of_a_queen(): 
    hand =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.QUEEN, CardValue.JACK))

def test_find_three_of_a_king(): 
    hand =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.KING, CardValue.QUEEN))

def test_find_three_of_a_ace(): 
    hand =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.ACE, CardValue.KING))

def __find_three_cards_of_kind(hand):
    counting_cards = CountingCards()
    three_cards_detector = ThreeCardsDetector(counting_cards)
    return three_cards_detector.find_three_of_kind(hand)

