import random
import copy

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.detector.pair_detector import PairDetector

def test_find_pair_queen(): 
    hand =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.QUEEN, CardValue.SEVEN))

def test_find_pair_ace(): 
    hand =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.ACE, CardValue.SEVEN))

def test_find_pair_random(): 
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    pair_value = __get_pair_value(all_cards_values)
    high_card = __get_high_cards_value(all_cards_values, pair_value)
    other_cards = __get_others_cards(all_cards_values, pair_value, high_card)
    hands = __get_hand_shuffle(pair_value, high_card, other_cards)
    assert(_find_pair(hands)==PairFigure(pair_value, high_card))
    
def __get_pair_value(all_cards_values):
    index = random.randint(0, len(all_cards_values) - 1)
    pair_value = all_cards_values[index]
    return pair_value

def __get_high_cards_value(all_cards_values, pair_value): 
    all_cards_values_for_high_cards = copy.deepcopy(all_cards_values)
    all_cards_values_for_high_cards.remove(pair_value)
    if CardValue.TWO in all_cards_values_for_high_cards :
        all_cards_values_for_high_cards.remove(CardValue.TWO)
    if CardValue.THREE in all_cards_values_for_high_cards : 
        all_cards_values_for_high_cards.remove(CardValue.THREE)    
    if CardValue.FOUR in all_cards_values_for_high_cards :
        all_cards_values_for_high_cards.remove(CardValue.FOUR)
    if pair_value == CardValue.TWO or pair_value == CardValue.THREE or pair_value == CardValue.FOUR : 
        all_cards_values_for_high_cards.remove(CardValue.FIVE)
    index = random.randint(0, len(all_cards_values_for_high_cards) - 1)
    high_cards_value = all_cards_values_for_high_cards[index]
    return high_cards_value

def __get_others_cards(all_cards_values, pair_value, high_card) : 
    copy_all_cards_values = copy.deepcopy(all_cards_values)
    for card_value in copy_all_cards_values : 
        if high_card <= card_value : 
            all_cards_values.remove(card_value)
    if pair_value in all_cards_values : 
        all_cards_values.remove(pair_value)
    others_cards = []
    while len(others_cards) < 3 :
        index = random.randint(0, len(all_cards_values) - 1)
        other_card_value = all_cards_values[index]
        others_cards.append(other_card_value)
        all_cards_values.remove(other_card_value)
    return others_cards    

def __get_hand_shuffle(pair_value, high_card, other_cards):
    hands = []
    hands.append(pair_value)
    hands.append(pair_value)
    hands.append(high_card)
    hands.extend(other_cards)
    random.shuffle(hands)
    return hands

def _find_pair(hand):
    counting_cards = CountingCards()
    pair_detector = PairDetector(counting_cards)
    return pair_detector.find_pair(hand)