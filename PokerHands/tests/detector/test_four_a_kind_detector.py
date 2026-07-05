from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.detector.four_cards_detector import FourCardsDetector
from PokerHands.tests.random_cards import get_all_values, get_random_card, get_shuffle_hand

def test_find_four_of_king_with_queen_high_cards():
    hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.KING, CardValue.QUEEN))

def test_find_four_of_ace_with_six_high_cards():
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS)]
    assert(__find_four_of_kind(hand) == FourOfKindFigure(CardValue.ACE, CardValue.SIX))

def test_find_four_of_kind_randomize():
    all_cards_values = get_all_values()
    four_times = get_random_card(all_cards_values)
    other_card = get_random_card(all_cards_values)
    hand = [Card(four_times, CardColor.CLUBS), Card(four_times, CardColor.DIAMONDS), Card(four_times, CardColor.HEARTS), Card(four_times, CardColor.SPADES), Card(other_card, CardColor.DIAMONDS)]
    get_shuffle_hand(hand)
    assert(__find_four_of_kind(hand) == FourOfKindFigure(four_times, other_card))
    
def __find_four_of_kind(hand): 
    counting_cards = CountingCards()
    four_cards_detector = FourCardsDetector(counting_cards)
    return four_cards_detector.find_four_cards(hand)
    