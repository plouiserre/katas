from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.tests.random_cards import add_cards, get_all_values, get_high_card_complete, get_random_card_complete, get_shuffle_poker_hand, remove_cards
from typing import List

def test_find_high_card_queen():
    combination =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(__find_high_card(combination)==HighCardFigure(CardValue.QUEEN))

def test_find_high_card_jack():
    combination =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)]
    assert(__find_high_card(combination)==HighCardFigure(CardValue.JACK))

def test_find_high_card_random(): 
    combination : List[Card]= []
    all_cards_values = get_all_values()
    remove_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE])
    high_card_random = get_high_card_complete(all_cards_values)
    add_cards(all_cards_values, [CardValue.THREE, CardValue.FOUR, CardValue.FIVE])
    combination.append(high_card_random)
    while len(combination) < 5 : 
        new_card = get_random_card_complete(all_cards_values)
        combination.append(new_card)
    get_shuffle_poker_hand(combination)
    assert(__find_high_card(combination)==HighCardFigure(high_card_random.value))

def __find_high_card(combination):
    _high_card_detector = HighCardDetector()
    return _high_card_detector.find_high_card(combination)