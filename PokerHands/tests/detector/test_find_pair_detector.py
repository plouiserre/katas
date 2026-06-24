from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.detector.pair_detector import PairDetector

def test_find_one_pair_figure_second(): 
    hand = [Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)]
    assert(PairFigure(CardValue.JACK, CardValue.TEN) == _find_pair(hand))

def test_find_pair_two(): 
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.TWO, CardValue.SEVEN))

def test_find_pair_three(): 
    hand =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.THREE, CardValue.SEVEN))

def test_find_pair_four(): 
    hand =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.FOUR, CardValue.SEVEN))

def test_find_pair_five(): 
    hand =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.FIVE, CardValue.SEVEN))

def test_find_pair_six(): 
    hand =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.SIX, CardValue.SEVEN))

def test_find_pair_seven(): 
    hand =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.SEVEN, CardValue.SIX))

def test_find_pair_eight(): 
    hand =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.EIGHT, CardValue.SEVEN))

def test_find_pair_nine(): 
    hand =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.NINE, CardValue.SEVEN))

def test_find_pair_ten(): 
    hand =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.TEN, CardValue.SEVEN))

def test_find_pair_jack(): 
    hand =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.JACK, CardValue.SEVEN))

def test_find_pair_queen(): 
    hand =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.QUEEN, CardValue.SEVEN))

def test_find_pair_king(): 
    hand =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.KING, CardValue.SEVEN))

def test_find_pair_ace(): 
    hand =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.ACE, CardValue.SEVEN))

def _find_pair(hand):
    counting_cards = CountingCards()
    pair_detector = PairDetector(counting_cards)
    return pair_detector.find_pair(hand)