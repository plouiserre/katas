from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards

def test_count_each_where_different_cards():
    hand = [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS)]        
    cards_counted_excepted = {CardValue.QUEEN : 1, CardValue.JACK : 1, CardValue.SIX : 1, CardValue.ACE : 1, CardValue.FOUR : 1 }
    assert(cards_counted_excepted == __couting_cards(hand))

def test_count_each_where_two_same_cards():
    hand = [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)]
    cards_counted_excepted = {CardValue.QUEEN : 2, CardValue.JACK : 1, CardValue.SIX : 1, CardValue.FOUR : 1 }
    assert(cards_counted_excepted == __couting_cards(hand))

def test_count_each_where_three_same_cards():
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)]
    cards_counted_excepted = {CardValue.ACE : 3, CardValue.TEN : 1, CardValue.SIX : 1}
    assert(cards_counted_excepted == __couting_cards(hand))

def test_count_each_where_fourth_same_cards():
    hand = [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS)]
    cards_counted_excepted = {CardValue.QUEEN : 4, CardValue.ACE : 1}
    assert(cards_counted_excepted == __couting_cards(hand))

def __couting_cards(hand): 
    counting_cards = CountingCards()
    return counting_cards.Count(hand)