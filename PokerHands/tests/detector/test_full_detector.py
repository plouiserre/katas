from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.Figure import FullFigure
from PokerHands.detector.full_detector import FullDetector

def test_find_full_king_two_times_jack_three_times():
    hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.KING, CardValue.JACK))

def test_find_full_ten_two_times_nine_three_times():
    hand = [Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.TEN, CardValue.NINE))

def test_find_full_eight_two_times_seven_three_times():
    hand = [Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.EIGHT, CardValue.SEVEN))

def test_find_full_six_two_times_five_three_times():
    hand = [Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.SIX, CardValue.FIVE))

def test_find_full_four_two_times_three_three_times():
    hand = [Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.FOUR, CardValue.THREE))

def test_find_full_ace_two_times_SEVEN_three_times():
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.ACE, CardValue.SEVEN))

def find_full(hand):
    counting_cards = CountingCards()
    full_detector = FullDetector(counting_cards)
    return full_detector.find_full(hand)