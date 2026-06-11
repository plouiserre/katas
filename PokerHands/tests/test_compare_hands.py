from PokerHands.card import CardColor, CardValue
from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure, ThreeOfKindFigure, StraitFigure, FlushFigure, FullFigure, FourOfKindFigure, QuinteFlush
from PokerHands.score import Score, FIRST_HAND, SECOND_HAND, EQUALITY

def test_compare_one_hand_with_jack_and_with_ace(): 
    first_hand = HighCardFigure(CardValue.JACK)
    second_hand = HighCardFigure(CardValue.ACE)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_hands_with_high_cards_queen():
    first_hand = HighCardFigure(CardValue.QUEEN)
    second_hand = HighCardFigure(CardValue.QUEEN)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_with_high_card_ace_and_one_pair_of_nine() : 
    first_hand = PairFigure(CardValue.NINE, CardValue.KING)
    second_hand = HighCardFigure(CardValue.ACE)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_with_high_card_ace_and_three_of_kind_of_queen() : 
    first_hand = HighCardFigure(CardValue.ACE)
    second_hand = ThreeOfKindFigure(CardValue.QUEEN, CardValue.TWO)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_one_pair_two_second_hand_one_pair_three() :
    first_hand = PairFigure(CardValue.TWO, CardValue.QUEEN)
    second_hand = PairFigure(CardValue.THREE, CardValue.EIGHT)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_hands_with_one_same_pair_but_different_high_cards() : 
    first_hand = PairFigure(CardValue.FOUR, CardValue.QUEEN)
    second_hand = PairFigure(CardValue.FOUR, CardValue.EIGHT)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_hands_with_same_pair_and_same_high_cards():
    first_hand = PairFigure(CardValue.FOUR, CardValue.QUEEN)
    second_hand = PairFigure(CardValue.FOUR, CardValue.QUEEN)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_with_one_pair_and_second_hand_with_two_pairs():
    first_hand = PairFigure(CardValue.ACE, CardValue.QUEEN)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.QUEEN, CardValue.JACK)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_with_straight_and_second_hand_one_pair():
    first_hand = StraitFigure(CardValue.EIGHT)
    second_hand = PairFigure(CardValue.ACE, CardValue.QUEEN)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_pairs_with_king_and_two_and_two_pairs_with_queen_and_jack():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.QUEEN, CardValue.JACK, CardValue.ACE)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_pairs_with_king_pairs_in_each_hand_and_second_pair_highter_in_second_hand():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.JACK, CardValue.ACE)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_different_high_cards():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.ACE)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_pairs_exactly_with_same_high_cards():
    first_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.TWO, CardValue.THREE)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

def test_compare_second_hand_two_pairs_and_first_hand_three_of_kinds(): 
    first_hand = ThreeOfKindFigure(CardValue.QUEEN, CardValue.SIX)
    second_hand = TwoPairFigure(CardValue.ACE, CardValue.KING, CardValue.FOUR)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_first_hand_two_pairs_and_second_hand_flush(): 
    first_hand = TwoPairFigure(CardValue.ACE, CardValue.KING, CardValue.FOUR)
    second_hand = FlushFigure(CardColor.DIAMONDS, CardValue.ACE)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_first_hand_two_pairs_and_second_hand_three_of_kinds(): 
    first_hand = TwoPairFigure(CardValue.ACE, CardValue.KING, CardValue.FOUR)
    second_hand = ThreeOfKindFigure(CardValue.QUEEN, CardValue.SIX)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_differents_three_of_kinds():
    first_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.FIVE)
    second_hand = ThreeOfKindFigure(CardValue.TEN, CardValue.ACE)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_but_differents_high_cards():
    first_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.FIVE)
    second_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_two_hands_have_same_three_of_kinds_and_same_high_cards():
    first_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    second_hand = ThreeOfKindFigure(CardValue.JACK, CardValue.ACE)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_hand_have_straight_and_one_have_three_of_kinds():
    first_hand = StraitFigure(CardValue.QUEEN)
    second_hand = ThreeOfKindFigure(CardValue.ACE, CardValue.KING)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_hand_have_three_of_kinds_and_one_have_full():
    first_hand = ThreeOfKindFigure(CardValue.ACE, CardValue.KING)
    second_hand = FullFigure(CardValue.THREE, CardValue.TWO)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_each_hand_have_differents_straights():
    first_hand = StraitFigure(CardValue.QUEEN)
    second_hand = StraitFigure(CardValue.KING)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_each_hand_have_same_straights():
    first_hand = StraitFigure(CardValue.QUEEN)
    second_hand = StraitFigure(CardValue.QUEEN)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_flush_and_one_straight():
    first_hand = FlushFigure(CardColor.DIAMONDS, CardValue.NINE)
    second_hand = StraitFigure(CardValue.QUEEN)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_straight_and_one_four_of_kind():
    first_hand = StraitFigure(CardValue.QUEEN)
    second_hand = FourOfKindFigure(CardValue.TWO, CardValue.THREE)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_each_hand_have_differents_flush(): 
    first_hand = FlushFigure(CardColor.SPADES, CardValue.EIGHT)
    second_hand = FlushFigure(CardColor.CLUBS, CardValue.SEVEN)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_each_hand_have_same_flush(): 
    first_hand = FlushFigure(CardColor.HEARTS, CardValue.ACE)
    second_hand = FlushFigure(CardColor.DIAMONDS, CardValue.ACE)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_hand_have_flush_and_other_have_full():
    first_hand = FlushFigure(CardColor.SPADES, CardValue.ACE)
    second_hand = FullFigure(CardValue.THREE, CardValue.TWO)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_hand_have_flush_and_other_have_quinte_flush():
    first_hand = QuinteFlush(CardValue.NINE, CardColor.DIAMONDS)
    second_hand = FlushFigure(CardColor.SPADES, CardValue.ACE)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_hands_with_differents_fulls():
    first_hand = FullFigure(CardValue.FIVE, CardValue.ACE)
    second_hand = FullFigure(CardValue.THREE, CardValue.TWO)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_hands_with_full_and_three_same_cards():
    first_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    second_hand = FullFigure(CardValue.QUEEN, CardValue.ACE)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_hands_with_same_fulls():
    first_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    second_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_have_four_a_kind_and_second_hand_have_fulls():
    first_hand = FourOfKindFigure(CardValue.TWO, CardValue.ACE)
    second_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_have_fulls_and_one_have_high_card():
    first_hand = HighCardFigure(CardValue.ACE)
    second_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_four_a_kind():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    second_hand = FourOfKindFigure(CardValue.ACE, CardValue.KING)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_four_a_kind_exactly_with_differents_high_cards():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.ACE)
    second_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.KING)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_four_a_kind_with_same_cards():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    second_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    assert(EQUALITY == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_have_four_a_kind_and_one_quinte_flush():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    second_hand = QuinteFlush(CardValue.SEVEN, CardColor.CLUBS)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_have_four_a_kind_and_one_pair():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    second_hand = PairFigure(CardValue.ACE, CardValue.KING)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_two_quinte_flush():
    first_hand = QuinteFlush(CardValue.QUEEN, CardColor.DIAMONDS)
    second_hand = QuinteFlush(CardValue.JACK, CardColor.HEARTS)
    assert(FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_quinte_flush_with_two_pairs():
    first_hand = TwoPairFigure(CardValue.QUEEN, CardValue.KING, CardValue.ACE)
    second_hand = QuinteFlush(CardValue.JACK, CardColor.HEARTS)
    assert(SECOND_HAND == compare_two_hands(first_hand, second_hand))

def compare_two_hands(first_hand, second_hand):
    score = Score(first_hand, second_hand)
    return score.determinate_winner()

