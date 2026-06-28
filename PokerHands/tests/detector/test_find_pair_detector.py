import random
import copy

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.detector.pair_detector import PairDetector


# def test_find_one_pair_figure_second(): 
#     hand = [Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)]
#     assert(PairFigure(CardValue.JACK, CardValue.TEN) == _find_pair(hand))

# def test_find_pair_two(): 
#     hand =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.TWO, CardValue.SEVEN))

# def test_find_pair_three(): 
#     hand =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.THREE, CardValue.SEVEN))

# def test_find_pair_four(): 
#     hand =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.FOUR, CardValue.SEVEN))

# def test_find_pair_five(): 
#     hand =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.FIVE, CardValue.SEVEN))

# def test_find_pair_six(): 
#     hand =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.SIX, CardValue.SEVEN))

# def test_find_pair_seven(): 
#     hand =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.SEVEN, CardValue.SIX))

# def test_find_pair_eight(): 
#     hand =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.EIGHT, CardValue.SEVEN))

# def test_find_pair_nine(): 
#     hand =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.NINE, CardValue.SEVEN))

# def test_find_pair_ten(): 
#     hand =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.TEN, CardValue.SEVEN))

# def test_find_pair_jack(): 
#     hand =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.JACK, CardValue.SEVEN))

def test_find_pair_queen(): 
    hand =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.QUEEN, CardValue.SEVEN))

# def test_find_pair_king(): 
#     hand =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(_find_pair(hand)==PairFigure(CardValue.KING, CardValue.SEVEN))

def test_find_pair_ace(): 
    hand =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(_find_pair(hand)==PairFigure(CardValue.ACE, CardValue.SEVEN))

def test_find_pair_random(): 
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    pair_value = __get_pair_value(all_cards_values)
    high_card = __get_high_cards_value(all_cards_values, pair_value)
    print(pair_value)
    print(high_card)
    # other_cards = __get_others_cards(all_cards_values, CardValue.FOUR, CardValue.FIVE)
    other_cards = __get_others_cards(all_cards_values, pair_value, high_card)
    hands = []
    hands.append(pair_value)
    hands.append(pair_value)
    hands.append(high_card)
    hands.extend(other_cards)
    random.shuffle(hands)
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


    # pair_value = __random_creation_pairs(all_cards_values)
    # high_value = __find_high_card_value(all_cards_values, [pair_value])
    # forbidden_value = [pair_value, high_value]
    # first_value = __find_other_cards(all_cards_values, forbidden_value, high_value)
    # second_value = __find_other_cards(all_cards_values, forbidden_value, high_value)
    # all_values_accepted = [pair_value, first_value, second_value, pair_value, high_value]
    # hand = []
    # while len(hand)  < 5 :
    #     index = random.randint(0, len(all_values_accepted) - 1)
    #     value_choose = all_values_accepted[index]
    #     hand.append(value_choose)
    #     all_values_accepted.remove(value_choose)
    assert(_find_pair(hand)==PairFigure(pair_value, high_value))

    

def _find_pair(hand):
    counting_cards = CountingCards()
    pair_detector = PairDetector(counting_cards)
    return pair_detector.find_pair(hand)

# def __random_creation_pairs(all_card_value):
#     index = random.randint(0, len(all_card_value) - 1) 
#     pair_cards = all_card_value[index]
#     return pair_cards

# def __find_high_card_value(all_card_value, card_values_forbidden):
#     all_values_possibles = []
#     for card_value in all_card_value : 
#         if card_value > CardValue.THREE : 
#             all_values_possibles.append(card_value)
#     for value_possible in all_values_possibles : 
#         for card_value_forbidden in card_values_forbidden : 
#             if value_possible == card_value_forbidden : 
#                 all_values_possibles.remove(value_possible)
#     index = random.randint(0, len(all_values_possibles) - 1)
#     value_choose = all_values_possibles[index]
#     return value_choose

# def __find_other_cards(all_card_value, card_values_forbidden, high_card_value) : 
#     all_values_possibles = copy.deepcopy(all_card_value)
#     for value_possible in all_values_possibles : 
#         for card_value_forbidden in card_values_forbidden : 
#             if value_possible == card_value_forbidden or  value_possible > high_card_value  : 
#                 all_values_possibles.remove(value_possible)
#     index = random.randint(0, len(all_values_possibles) - 1)
#     value_choose = all_values_possibles[index]
#     card_values_forbidden.append(value_choose)
#     return value_choose