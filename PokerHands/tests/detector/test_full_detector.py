import random

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.detector.full_detector import FullDetector

def test_find_full_king_two_times_jack_three_times():
    hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.KING, CardValue.JACK))

def test_find_full_ten_two_times_nine_three_times():
    hand = [Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.TEN, CardValue.NINE))

def test_find_full_randomize():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    two_times_cards = __choose_cards(all_cards_values)
    three_times_cards = __choose_cards(all_cards_values)
    hand = [Card(two_times_cards, CardColor.CLUBS), Card(two_times_cards, CardColor.DIAMONDS),
            Card(three_times_cards, CardColor.HEARTS), Card(three_times_cards, CardColor.SPADES),
            Card(three_times_cards, CardColor.CLUBS)]
    random.shuffle(hand)
    assert(find_full(hand) == FullFigure(two_times_cards, three_times_cards))

def __choose_cards(all_cards_values) :
    index = random.randint(0, len(all_cards_values) - 1)
    card = all_cards_values[index]
    all_cards_values.remove(card)
    return card

def find_full(hand):
    counting_cards = CountingCards()
    full_detector = FullDetector(counting_cards)
    return full_detector.find_full(hand)