import random

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.detector.flush_detector import FlushDetector

def test_find_flush_hearts_by_king():
    hand = [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.HEARTS)]
    assert(__find_flush(hand) == FlushFigure(CardColor.HEARTS, CardValue.KING))

def test_find_flush_clubs_by_queen():
    hand = [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.CLUBS)]
    assert(__find_flush(hand) == FlushFigure(CardColor.CLUBS, CardValue.QUEEN))

def test_find_flush_randomise(): 
    colors = [CardColor.CLUBS, CardColor.DIAMONDS, CardColor.HEARTS, CardColor.SPADES]
    index = random.randint(0, len(colors) - 1)
    color_choose = colors[index]
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    first_card_value = __choose_cards(all_cards_values)
    second_card_value = __choose_cards(all_cards_values)
    third_card_value = __choose_cards(all_cards_values)
    fourth_card_value = __choose_cards(all_cards_values)
    fifth_card_value = __choose_cards(all_cards_values)
    
    hand = [Card(first_card_value, color_choose), Card(second_card_value, color_choose), 
            Card(third_card_value, color_choose), Card(fourth_card_value, color_choose), 
            Card(fifth_card_value, color_choose)]
    max_card = __determine_max_cards(hand)
    assert(__find_flush(hand) == FlushFigure(color_choose, max_card))

def __choose_cards(all_cards_values) :
    index = random.randint(0, len(all_cards_values) - 1)
    card = all_cards_values[index]
    all_cards_values.remove(card)
    return card

def __determine_max_cards(hand): 
    max_card = CardValue.UNDEFINED
    for card in hand : 
        if max_card == CardValue.UNDEFINED or max_card < card.value :
            max_card = card.value
    return max_card


def __find_flush(hand) : 
    flush_detector = FlushDetector()
    return flush_detector.find_flush(hand)