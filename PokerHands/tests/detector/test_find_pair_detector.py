from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.detector.pair_detector import PairDetector
from PokerHands.tests.random_cards import add_cards, get_all_values, get_high_card_complete, get_random_card_complete, get_shuffle_hand, remove_cards

def test_find_pair_queen(): 
    hand =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.QUEEN, CardValue.SEVEN))

def test_find_pair_ace(): 
    hand =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.ACE, CardValue.SEVEN))

def test_find_pair_random(): 
    all_cards_values = get_all_values()
    pair_card = get_random_card_complete(all_cards_values)
    remove_cards(all_cards_values, [CardValue.THREE])
    high_card = get_high_card_complete(all_cards_values)
    add_cards(all_cards_values, [CardValue.THREE])
    fourth_card = get_random_card_complete(all_cards_values)
    fifth_card = get_random_card_complete(all_cards_values)
    hand = [pair_card, pair_card, high_card, fourth_card, fifth_card]
    get_shuffle_hand(hand)
    assert(_find_pair(hand)==PairFigure(pair_card.value, high_card.value))
    
def _find_pair(hand):
    counting_cards = CountingCards()
    pair_detector = PairDetector(counting_cards)
    return pair_detector.find_pair(hand)