import random
import copy

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.detector.three_cards_detector import ThreeCardsDetector

def test_find_three_of_a_six(): 
    hand =  [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.SIX, CardValue.FOUR))

def test_find_three_of_a_king(): 
    hand =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.KING, CardValue.QUEEN))

def test_find_three_of_kind_randomized(): 
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    three_of_kinds_value = __get_card_value_random(all_cards_values)
    high_cards_value = __get_high_cards(all_cards_values, three_of_kinds_value)
    other_card_value = __get_other_cards(all_cards_values, three_of_kinds_value, high_cards_value)
    hand = __get_hand_shuffle(three_of_kinds_value, high_cards_value, other_card_value)
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(three_of_kinds_value, high_cards_value))


def __get_card_value_random(all_cards_values):
    index = random.randint(0, len(all_cards_values) - 1)
    pair_value = all_cards_values[index]
    return pair_value    

def __get_high_cards(all_cards_values, three_of_kind_value):
    copy_all_cards_values = copy.deepcopy(all_cards_values)
    copy_all_cards_values.remove(three_of_kind_value)
    if CardValue.TWO in copy_all_cards_values : 
        copy_all_cards_values.remove(CardValue.TWO)
    if three_of_kind_value == CardValue.TWO and CardValue.THREE in copy_all_cards_values : 
        copy_all_cards_values.remove(CardValue.THREE)
    index = random.randint(0, len(copy_all_cards_values) - 1)
    high_card_value = copy_all_cards_values[index]
    return high_card_value

def __get_other_cards(all_cards_values, three_of_kind_value, high_card_value):
    copy_all_cards_values = copy.deepcopy(all_cards_values)
    for card_value in copy_all_cards_values : 
        if high_card_value <= card_value : 
            all_cards_values.remove(card_value)
    if three_of_kind_value in all_cards_values : 
        all_cards_values.remove(three_of_kind_value)
    index = random.randint(0, len(all_cards_values) - 1)
    other_card_value = all_cards_values[index]
    return other_card_value

def __get_hand_shuffle(three_of_kind_value, high_card_value, other_card_value):
    hands = []
    hands.append(three_of_kind_value)
    hands.append(three_of_kind_value)
    hands.append(three_of_kind_value)
    hands.append(high_card_value)
    hands.append(other_card_value)
    random.shuffle(hands)
    return hands

def __find_three_cards_of_kind(hand):
    counting_cards = CountingCards()
    three_cards_detector = ThreeCardsDetector(counting_cards)
    return three_cards_detector.find_three_of_kind(hand)