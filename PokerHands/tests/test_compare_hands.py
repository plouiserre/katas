from PokerHands.card import CardColor, CardValue
from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure 
from PokerHands.AllFigures.FullFigure import FullFigure 
from PokerHands.AllFigures.HighCardFigure import HighCardFigure 
from PokerHands.AllFigures.PairFigure import PairFigure 
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.StraitFigure import StraitFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure 
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.score import Score
from PokerHands.winner import Winner

#TODO faut rajouter des tests combinatoires pour tester deux figures de la même façon 

def test_compare_one_hand_with_high_card_ace_and_one_pair_of_nine() : 
    first_hand = PairFigure(CardValue.NINE, CardValue.KING)
    second_hand = HighCardFigure(CardValue.ACE)
    assert(Winner.FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_with_high_card_ace_and_three_of_kind_of_queen() : 
    first_hand = HighCardFigure(CardValue.ACE)
    second_hand = ThreeOfKindFigure(CardValue.QUEEN, CardValue.TWO)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_with_one_pair_and_second_hand_with_two_pairs():
    first_hand = PairFigure(CardValue.ACE, CardValue.QUEEN)
    second_hand = TwoPairFigure(CardValue.KING, CardValue.QUEEN, CardValue.JACK)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_with_straight_and_second_hand_one_pair():
    first_hand = StraitFigure(CardValue.EIGHT)
    second_hand = PairFigure(CardValue.ACE, CardValue.QUEEN)
    assert(Winner.FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_second_hand_two_pairs_and_first_hand_three_of_kinds(): 
    first_hand = ThreeOfKindFigure(CardValue.QUEEN, CardValue.SIX)
    second_hand = TwoPairFigure(CardValue.ACE, CardValue.KING, CardValue.FOUR)
    assert(Winner.FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_first_hand_two_pairs_and_second_hand_flush(): 
    first_hand = TwoPairFigure(CardValue.ACE, CardValue.KING, CardValue.FOUR)
    second_hand = FlushFigure(CardColor.DIAMONDS, CardValue.ACE)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_first_hand_two_pairs_and_second_hand_three_of_kinds(): 
    first_hand = TwoPairFigure(CardValue.ACE, CardValue.KING, CardValue.FOUR)
    second_hand = ThreeOfKindFigure(CardValue.QUEEN, CardValue.SIX)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_hand_have_straight_and_one_have_three_of_kinds():
    first_hand = StraitFigure(CardValue.QUEEN)
    second_hand = ThreeOfKindFigure(CardValue.ACE, CardValue.KING)
    assert(Winner.FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_hand_have_three_of_kinds_and_one_have_full():
    first_hand = ThreeOfKindFigure(CardValue.ACE, CardValue.KING)
    second_hand = FullFigure(CardValue.THREE, CardValue.TWO)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_flush_and_one_straight():
    first_hand = FlushFigure(CardColor.DIAMONDS, CardValue.NINE)
    second_hand = StraitFigure(CardValue.QUEEN)
    assert(Winner.FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_straight_and_one_four_of_kind():
    first_hand = StraitFigure(CardValue.QUEEN)
    second_hand = FourOfKindFigure(CardValue.TWO, CardValue.THREE)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_hand_have_flush_and_other_have_full():
    first_hand = FlushFigure(CardColor.SPADES, CardValue.ACE)
    second_hand = FullFigure(CardValue.THREE, CardValue.TWO)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_where_one_hand_have_flush_and_other_have_quinte_flush():
    first_hand = QuinteFlushFigure(CardValue.NINE, CardColor.DIAMONDS)
    second_hand = FlushFigure(CardColor.SPADES, CardValue.ACE)
    assert(Winner.FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_have_four_a_kind_and_second_hand_have_fulls():
    first_hand = FourOfKindFigure(CardValue.TWO, CardValue.ACE)
    second_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    assert(Winner.FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_have_fulls_and_one_have_high_card():
    first_hand = HighCardFigure(CardValue.ACE)
    second_hand = FullFigure(CardValue.QUEEN, CardValue.KING)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_have_four_a_kind_and_one_quinte_flush():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    second_hand = QuinteFlushFigure(CardValue.SEVEN, CardColor.CLUBS)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_hand_have_four_a_kind_and_one_pair():
    first_hand = FourOfKindFigure(CardValue.QUEEN, CardValue.JACK)
    second_hand = PairFigure(CardValue.ACE, CardValue.KING)
    assert(Winner.FIRST_HAND == compare_two_hands(first_hand, second_hand))

def test_compare_one_quinte_flush_with_two_pairs():
    first_hand = TwoPairFigure(CardValue.QUEEN, CardValue.KING, CardValue.ACE)
    second_hand = QuinteFlushFigure(CardValue.JACK, CardColor.HEARTS)
    assert(Winner.SECOND_HAND == compare_two_hands(first_hand, second_hand))

def compare_two_hands(first_hand, second_hand):
    score = Score(first_hand, second_hand)
    return score.determinate_winner()

