import random
import copy
from typing import List
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.AllFigures.HighCardFigure import HighCardFigure

def test_find_high_card_queen():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.QUEEN))

def test_find_high_card_jack():
    hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.JACK))


def test_find_high_card_random(): 
    hand : List[Card]= []
    high_card_random = __get_high_card_value()
    hand.append(Card(high_card_random, CardColor.CLUBS))
    all_colors = [CardColor.CLUBS, CardColor.DIAMONDS, CardColor.HEARTS, CardColor.SPADES]
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    all_cards_values.remove(high_card_random)
    all_cards_values_copy = copy.deepcopy(all_cards_values)
    for card_value in all_cards_values_copy : 
        if high_card_random <= card_value :
            all_cards_values.remove(card_value)
    while len(hand) < 5 : 
        index_value = random.randint(0, len(all_cards_values) - 1)
        index_color = random.randint(0, len(all_colors) - 1)
        value = all_cards_values[index_value]
        color = all_colors[index_color]
        hand.append(Card(value, color))
        all_cards_values.remove(value)
    assert(__find_high_card(hand)==HighCardFigure(high_card_random))
    

def __get_high_card_value():
    all_cards_values = [CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    index = random.randint(0, len(all_cards_values) - 1)
    pair_value = all_cards_values[index]
    return pair_value

def __find_high_card(hand):
    _high_card_detector = HighCardDetector()
    return _high_card_detector.find_high_card(hand)