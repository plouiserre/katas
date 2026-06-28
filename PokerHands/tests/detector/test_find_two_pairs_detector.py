import random

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.detector.two_pairs_detector import TwoPairsDetector

def test_find_two_pairs_two_three(): 
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.THREE, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]    
    assert(__find_two_pairs(hand)==TwoPairFigure(CardValue.THREE, CardValue.TWO, CardValue.FOUR))

def test_find_two_pairs_four_five(): 
    hand =  [Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    assert(__find_two_pairs(hand)==TwoPairFigure(CardValue.FIVE, CardValue.FOUR, CardValue.THREE))

def test_find_two_pairs_six_seven(): 
    hand =  [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    assert(__find_two_pairs(hand)==TwoPairFigure(CardValue.SEVEN, CardValue.SIX, CardValue.FIVE))

def test_find_two_pairs_eight_nine(): 
    hand =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)]
    assert(__find_two_pairs(hand)==TwoPairFigure(CardValue.NINE, CardValue.EIGHT, CardValue.SIX))

def test_find_two_pairs_ten_ace(): 
    hand =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.ACE, CardColor.SPADES)]
    assert(__find_two_pairs(hand)==TwoPairFigure(CardValue.ACE, CardValue.TEN, CardValue.NINE))

def test_find_two_pairs_jack_queen(): 
    hand =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(__find_two_pairs(hand)==TwoPairFigure(CardValue.QUEEN, CardValue.JACK, CardValue.NINE))

def test_find_two_pairs_king_six(): 
    hand =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.KING, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(__find_two_pairs(hand)==TwoPairFigure(CardValue.KING, CardValue.SIX, CardValue.QUEEN))

def test_find_two_pairs_randomise(): 
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    first_pair_value = __get_card_value_random(all_cards_values)
    all_cards_values.remove(first_pair_value)
    second_pair_value = __get_card_value_random(all_cards_values)
    all_cards_values.remove(second_pair_value)
    high_card_value = __get_card_value_random(all_cards_values)
    hand = __get_hand_shuffle(first_pair_value, second_pair_value, high_card_value)
    assert(__find_two_pairs(hand)==TwoPairFigure(first_pair_value, second_pair_value, high_card_value) or __find_two_pairs(hand)==TwoPairFigure(second_pair_value, first_pair_value, high_card_value))


def __get_hand_shuffle(first_pair_value, second_pair_value, high_card_value):
    hands = []
    hands.append(first_pair_value)
    hands.append(first_pair_value)
    hands.append(second_pair_value)
    hands.append(second_pair_value)
    hands.append(high_card_value)
    random.shuffle(hands)
    return hands

def __get_card_value_random(all_cards_values):
    index = random.randint(0, len(all_cards_values) - 1)
    pair_value = all_cards_values[index]
    return pair_value

def __find_two_pairs(hand):
    counting_cards = CountingCards()
    two_pairs_detector = TwoPairsDetector(counting_cards)
    return two_pairs_detector.find_two_pairs(hand)
