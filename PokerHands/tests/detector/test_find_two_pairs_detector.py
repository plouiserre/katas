from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.detector.two_pairs_detector import TwoPairsDetector
from PokerHands.tests.random_cards import get_all_values, get_random_card_complete, get_shuffle_hand

def test_find_two_pairs_ten_ace(): 
    hand =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.ACE, CardColor.SPADES)]
    assert(__find_two_pairs(hand)==TwoPairFigure(CardValue.ACE, CardValue.TEN, CardValue.NINE))

def test_find_two_pairs_jack_queen(): 
    hand =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(__find_two_pairs(hand)==TwoPairFigure(CardValue.QUEEN, CardValue.JACK, CardValue.NINE))

def test_find_two_pairs_randomise(): 
    all_cards_values = get_all_values()
    first_pair_card = get_random_card_complete(all_cards_values)
    second_pair_card = get_random_card_complete(all_cards_values)
    high_card = get_random_card_complete(all_cards_values)
    hand = [first_pair_card, first_pair_card, second_pair_card, second_pair_card, high_card]
    get_shuffle_hand(hand)
    assert(__find_two_pairs(hand)==TwoPairFigure(first_pair_card.value, second_pair_card.value, high_card.value) or __find_two_pairs(hand)==TwoPairFigure(second_pair_card.value, first_pair_card.value, high_card.value))


def __find_two_pairs(hand):
    counting_cards = CountingCards()
    two_pairs_detector = TwoPairsDetector(counting_cards)
    return two_pairs_detector.find_two_pairs(hand)
