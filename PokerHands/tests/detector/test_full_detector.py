from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.manipulating_cards import ManipulatingCards
from PokerHands.detector.full_detector import FullDetector
from PokerHands.tests.random_cards import get_all_values, get_random_card, get_shuffle_poker_hand

def test_find_full_king_two_times_jack_three_times():
    combination = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS)]
    assert(find_full(combination) == FullFigure(CardValue.KING, CardValue.JACK))

def test_find_full_ten_two_times_nine_three_times():
    combination = [Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS)]
    assert(find_full(combination) == FullFigure(CardValue.TEN, CardValue.NINE))

def test_find_full_with_seven_cards_with_queen_two_times_ace_three_times_and_six():
    combination = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.HEARTS)]
    assert(find_full(combination) == FullFigure(CardValue.QUEEN, CardValue.ACE))

def test_find_full_randomize():
    all_cards_values = get_all_values()
    two_times_cards = get_random_card(all_cards_values)
    three_times_cards = get_random_card(all_cards_values)
    combination = [Card(two_times_cards, CardColor.CLUBS), Card(two_times_cards, CardColor.DIAMONDS),
            Card(three_times_cards, CardColor.HEARTS), Card(three_times_cards, CardColor.SPADES),
            Card(three_times_cards, CardColor.CLUBS)]
    get_shuffle_poker_hand(combination)
    assert(find_full(combination) == FullFigure(two_times_cards, three_times_cards))
    
def find_full(combination):
    manipulating_cards = ManipulatingCards()
    full_detector = FullDetector(manipulating_cards)
    return full_detector.find_full(combination)