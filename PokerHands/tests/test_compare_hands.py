from PokerHands.card import CardValue
from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure

#two hands with high cards differents values
def test_compare_one_hand_with_jack_and_with_ace(): 
    first_hand = HighCardFigure(CardValue.JACK)
    second_hand = HighCardFigure(CardValue.ACE)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

#two hands with high cards same values
def test_compare_two_hands_with_high_cards_queen():
    first_hand = HighCardFigure(CardValue.QUEEN)
    second_hand = HighCardFigure(CardValue.QUEEN)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

#two hands with high cards and a pair
def test_compare_one_hand_with_high_card_ace_and_one_pair_of_nine() : 
    first_hand = PairFigure(CardValue.NINE, CardValue.KING)
    second_hand = HighCardFigure(CardValue.ACE)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

#two hands with each have one pair different value
def test_compare_one_hand_one_pair_two_second_hand_one_pair_three() :
    first_hand = PairFigure(CardValue.TWO, CardValue.QUEEN)
    second_hand = PairFigure(CardValue.THREE, CardValue.EIGHT)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

#two hands with each have one pair same value but different other cards
def test_compare_two_hands_with_one_same_pair_but_different_high_cards() : 
    first_hand = PairFigure(CardValue.FOUR, CardValue.QUEEN)
    second_hand = PairFigure(CardValue.FOUR, CardValue.EIGHT)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

#two hands with each have one pair same value with same other cards
def test_compare_two_hands_with_same_pair_and_same_high_cards():
    first_hand = PairFigure(CardValue.FOUR, CardValue.QUEEN)
    second_hand = PairFigure(CardValue.FOUR, CardValue.QUEEN)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

#two hands with a pair and a two pairs
def test_compare_one_hand_with_one_pair_and_second_hand_with_two_pairs():
    first_hand = PairFigure(CardValue.ACE, CardValue.QUEEN)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.QUEEN, CardValue.JACK)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

#two hands with each have two pairs different values
def test_compare_two_pairs_with_king_and_two_and_two_pairs_with_queen_and_jack():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.QUEEN, CardValue.JACK, CardValue.ACE)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

#two hands with each have two pairs one is the same the other is different
def test_compare_two_pairs_with_king_pairs_in_each_hand_and_second_pair_highter_in_second_hand():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.JACK, CardValue.ACE)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

#two hands with each have two pairs same values but different other cards

#two hands with each have two pairs same values with same other cards

#two hands with two pairs and one three of kind

#two hands with each have one three of kind different values

#two hands with each have one three of kind same values but different other cards

#two hands with each have one three of kind same values with same other cards

#two hands with one three of kind and one straight

#two hands with each have one straight values

#two hands with each have one straight but different other cards

#two hands with one flush

#two hands with each have one flush differents values

#two hands with one flush and one full

#two hands with two fulls with differents values

#two hands with one full and one a four of kind

#two hands with two fours of kind with differents values

#two hands with one a four of kind and a quinte flush

#two hands with two quinte flush with differents cards

EQUALITY = 0
FIRST_HAND = 1
SECOND_HAND = 2

def compare_two_hands(first_hand, second_hand):
    if type(first_hand) is HighCardFigure and type(second_hand) is HighCardFigure : 
        if first_hand.value < second_hand.value : 
            return SECOND_HAND
        elif second_hand.value < first_hand.value : 
            return FIRST_HAND 
        else :
            return EQUALITY
    elif type(first_hand) is PairFigure and type(second_hand) is HighCardFigure : 
        return FIRST_HAND
    elif type(second_hand) is PairFigure and type(first_hand) is HighCardFigure : 
        return SECOND_HAND
    elif type(first_hand) is PairFigure and type(second_hand) is PairFigure : 
        if first_hand.value < second_hand.value : 
            return SECOND_HAND
        elif second_hand.value < first_hand.value : 
            return FIRST_HAND
        else : 
            if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards : 
                return SECOND_HAND
            elif second_hand.high_value_rest_of_cards < first_hand.high_value_rest_of_cards :
                return FIRST_HAND
            else : 
                return EQUALITY
    elif type(first_hand) is TwoPairFigure and type(second_hand) is PairFigure : 
        return FIRST_HAND 
    elif type(first_hand) is PairFigure and type(second_hand) is TwoPairFigure : 
        return SECOND_HAND
    elif type(first_hand) is TwoPairFigure and type(second_hand) is TwoPairFigure :
        return compare_two_hands_with_two_pairs(first_hand, second_hand)
        
def compare_two_hands_with_two_pairs(first_hand, second_hand):
    first_hand_pairs = []
    first_hand_pairs.append(first_hand.first_pair_value)
    first_hand_pairs.append(first_hand.second_pair_value)
    second_hand_pairs = []
    second_hand_pairs.append(second_hand.first_pair_value)
    second_hand_pairs.append(second_hand.second_pair_value)
    high_pair = CardValue.UNDEFINED
    is_first_hand = False
    is_second_hand = False
    for first_pair_card in first_hand_pairs : 
        for second_pair_card in second_hand_pairs : 
            if high_pair == CardValue.UNDEFINED : 
                if first_pair_card < second_pair_card :
                    high_pair = second_pair_card
                elif second_pair_card < first_pair_card: 
                    high_pair = first_pair_card
            else : 
                if high_pair < first_pair_card : 
                    high_pair = first_pair_card
                elif high_pair < second_pair_card : 
                    high_pair = second_pair_card
    for first_pair_card in first_hand_pairs : 
        if high_pair == first_pair_card : 
            is_first_hand = True
            break
    if is_first_hand : 
        return FIRST_HAND
    for second_pair_card in second_hand_pairs : 
        if high_pair == second_pair_card : 
            is_second_hand = True
            break
    if is_second_hand : 
        return SECOND_HAND
        