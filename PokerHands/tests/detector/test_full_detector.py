from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.detector.full_detector import FullDetector
from PokerHands.tests.random_cards import get_all_values, get_random_card, get_shuffle_hand

def test_find_full_king_two_times_jack_three_times():
    hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.KING, CardValue.JACK))

def test_find_full_ten_two_times_nine_three_times():
    hand = [Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS)]
    assert(find_full(hand) == FullFigure(CardValue.TEN, CardValue.NINE))

def test_find_full_randomize():
    all_cards_values = get_all_values()
    two_times_cards = get_random_card(all_cards_values)
    three_times_cards = get_random_card(all_cards_values)
    hand = [Card(two_times_cards, CardColor.CLUBS), Card(two_times_cards, CardColor.DIAMONDS),
            Card(three_times_cards, CardColor.HEARTS), Card(three_times_cards, CardColor.SPADES),
            Card(three_times_cards, CardColor.CLUBS)]
    get_shuffle_hand(hand)
    assert(find_full(hand) == FullFigure(two_times_cards, three_times_cards))
    
def find_full(hand):
    counting_cards = CountingCards()
    full_detector = FullDetector(counting_cards)
    return full_detector.find_full(hand)