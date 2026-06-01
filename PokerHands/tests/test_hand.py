from PokerHands.card import Card, CardColor, CardValue
from PokerHands.hand import Hand
from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure, ThreeOfKindFigure, StraitFigure, FlushFigure

def test_find_high_figure_ace(): 
    hand = [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS)]
    assert(HighCardFigure(CardValue.ACE) == __find_high_figure(hand))

def test_find_one_pair_figure_first(): 
    hand = [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)]
    assert(PairFigure(CardValue.QUEEN, CardValue.JACK) == __find_high_figure(hand))

def test_find_one_pair_figure_second(): 
    hand = [Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)]
    assert(PairFigure(CardValue.JACK, CardValue.TEN) == __find_high_figure(hand))

def test_find_two_pair_two_three(): 
    hand = [Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS)]
    assert(TwoPairFigure(CardValue.THREE, CardValue.TWO, CardValue.FOUR) == __find_high_figure(hand))

def test_find_one_three_of_kind_figure_first(): 
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)]
    assert(ThreeOfKindFigure(CardValue.ACE, CardValue.TEN) == __find_high_figure(hand))

def test_find_straight_six_finish_by_six(): 
    hand = [Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(StraitFigure(CardValue.SIX) == __find_high_figure(hand))

def test_find_straight_six_finish_by_five(): 
    hand = [Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(StraitFigure(CardValue.SIX) == __find_high_figure(hand))

def test_find_flush_diamonds_by_ace():
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(FlushFigure(CardColor.DIAMONDS, CardValue.ACE) == __find_high_figure(hand))


def __find_high_figure(content) : 
    hand = Hand()
    figure =  hand.determinate_high_figure(content) 
    return figure 