from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.detector.three_cards_detector import ThreeCardsDetector
from PokerHands.tests.random_cards import add_cards, get_all_values, get_high_card_complete, get_lower_card_complete, get_random_card_complete, get_shuffle_hand, remove_cards

def test_find_three_of_a_six(): 
    hand =  [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.SIX, CardValue.FOUR))

def test_find_three_of_a_king(): 
    hand =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(CardValue.KING, CardValue.QUEEN))

def test_find_three_of_kind_randomized(): 
    all_cards_values = get_all_values()
    three_of_kinds = get_random_card_complete(all_cards_values)
    if three_of_kinds.value is CardValue.TWO : 
        remove_cards(all_cards_values, [CardValue.THREE])
    high_card = get_high_card_complete(all_cards_values)
    if three_of_kinds.value is CardValue.TWO : 
        add_cards(all_cards_values, [CardValue.THREE])
        remove_cards(all_cards_values, [CardValue.TWO])
    print("three of cards "+str(three_of_kinds.value)+ " high_card "+str(high_card.value))
    other_card = get_lower_card_complete(all_cards_values, high_card)
    hand = [three_of_kinds, three_of_kinds, three_of_kinds, high_card,  other_card] 
    get_shuffle_hand(hand)
    assert(__find_three_cards_of_kind(hand)==ThreeOfKindFigure(three_of_kinds.value, high_card.value))        

def __find_three_cards_of_kind(hand):
    counting_cards = CountingCards()
    three_cards_detector = ThreeCardsDetector(counting_cards)
    return three_cards_detector.find_three_of_kind(hand)