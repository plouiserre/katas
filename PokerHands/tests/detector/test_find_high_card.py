import random
import copy
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.AllFigures.HighCardFigure import HighCardFigure

def test_find_high_card_king():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    values_already_choose = []
    forbidden_values = [CardValue.KING, CardValue.ACE]
    hand =  [Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.CLUBS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.DIAMONDS),
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.DIAMONDS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.HEARTS), 
             Card(CardValue.KING, CardColor.SPADES)]
    assert(__find_high_card(hand)== HighCardFigure(CardValue.KING))

def test_find_high_card_queen():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    values_already_choose = []
    forbidden_values = [CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    hand =  [Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.CLUBS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.DIAMONDS),
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.SPADES), 
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.HEARTS)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.QUEEN))

def test_find_high_card_jack():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    values_already_choose = []
    forbidden_values = [CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    print(values_already_choose)
    hand =  [Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.CLUBS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.DIAMONDS),
             Card(CardValue.JACK, CardColor.DIAMONDS), 
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.HEARTS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.JACK))

def test_find_high_card_ten():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    values_already_choose = []
    forbidden_values = [CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    hand =  [Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), 
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.HEARTS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.SPADES), 
             Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.TEN))

def test_find_high_card_nine():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    values_already_choose = []
    forbidden_values = [CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    hand =  [Card(CardValue.NINE, CardColor.CLUBS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.DIAMONDS), 
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.HEARTS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.SPADES), 
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.NINE))

def test_find_high_card_eight():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    values_already_choose = []
    forbidden_values = [CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    hand =  [Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.CLUBS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.DIAMONDS), 
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.SPADES), 
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.EIGHT))

def test_find_high_card_seven():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    values_already_choose = []
    forbidden_values = [CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    hand =  [Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.CLUBS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.DIAMONDS), 
             Card(CardValue.SEVEN, CardColor.HEARTS), Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.SPADES), 
             Card(__choose_card_value(all_cards_values, values_already_choose, values_already_choose, forbidden_values), CardColor.SPADES)]
    assert(__find_high_card(hand)==HighCardFigure(CardValue.SEVEN))

def __find_high_card(hand):
    _high_card_detector = HighCardDetector()
    return _high_card_detector.find_high_card(hand)

def __choose_card_value(all_cards_values, values_already_choose, already_choose_values, forbidden_values): 
    not_choose_values = copy.deepcopy(all_cards_values)
    for card_value in all_cards_values : 
        for already_choose_value in already_choose_values : 
            if card_value == already_choose_value : 
                not_choose_values.remove(card_value)
    ok_values = copy.deepcopy(not_choose_values)
    for not_choose_value in not_choose_values : 
        for forbidden_value in forbidden_values : 
            if not_choose_value == forbidden_value : 
                ok_values.remove(forbidden_value)
    index = random.randint(0, len(ok_values) - 1)
    value_choose = ok_values[index]
    values_already_choose.append(value_choose)
    return value_choose