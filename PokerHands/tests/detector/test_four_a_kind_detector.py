import random

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

def test_find_four_of_kind_randomize():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    four_times = __choose_cards(all_cards_values)
    other_card = __choose_cards(all_cards_values)
    hand = [Card(four_times, CardColor.CLUBS), Card(four_times, CardColor.DIAMONDS), Card(four_times, CardColor.HEARTS), Card(four_times, CardColor.SPADES), Card(other_card, CardColor.DIAMONDS)]
    random.shuffle(hand)
    assert(__find_four_of_kind(hand) == FourOfKindFigure(four_times, other_card))

    

def __choose_cards(all_cards_values) :
    index = random.randint(0, len(all_cards_values) - 1)
    card = all_cards_values[index]
    all_cards_values.remove(card)
    return card

def __find_four_of_kind(hand): 
    counting_cards = CountingCards()
    four_cards_detector = FourCardsDetector(counting_cards)
    return four_cards_detector.find_four_cards(hand)
    