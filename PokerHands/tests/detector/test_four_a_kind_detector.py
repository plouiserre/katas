from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.detector.four_cards_detector import FourCardsDetector

def test_find_four_of_king_with_queen_high_cards():
    hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.KING, CardValue.QUEEN))

def test_find_four_of_ace_with_six_high_cards():
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.ACE, CardValue.SIX))

def test_find_four_of_jack_with_king_high_cards():
    hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.JACK, CardValue.KING))

def test_find_four_of_ten_with_jack_high_cards():
    hand = [Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.TEN, CardValue.JACK))

def test_find_four_of_nine_with_eight_high_cards():
    hand = [Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.NINE, CardValue.EIGHT))

def test_find_four_of_eight_with_seven_high_cards():
    hand = [Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.EIGHT, CardValue.SEVEN))

def test_find_four_of_seven_with_five_high_cards():
    hand = [Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.SEVEN, CardValue.FIVE))

def test_find_four_of_six_with_four_high_cards():
    hand = [Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.SIX, CardValue.FOUR))

def test_find_four_of_five_with_three_high_cards():
    hand = [Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.FIVE, CardValue.THREE))

def test_find_four_of_four_with_two_high_cards():
    hand = [Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.FOUR, CardValue.TWO))

def test_find_four_of_two_with_king_high_cards():
    hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.TWO, CardValue.KING))

def __find_four_of_kind(hand): 
    counting_cards = CountingCards()
    four_cards_detector = FourCardsDetector(counting_cards)
    return four_cards_detector.find_four_cards(hand)
    