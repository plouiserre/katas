from PokerHands.card import Card, CardColor, CardValue
from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure, ThreeOfKindFigure, StraitFigure, FlushFigure, FullFigure
from PokerHands.hand import Hand, HighCardFigure

def test_find_high_value_ace():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.ACE, CardColor.SPADES)]
    assert(return_high_hands(cards)==  HighCardFigure(CardValue.ACE))

def test_find_high_value_king():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)== HighCardFigure(CardValue.KING))

def test_find_high_value_queen():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==HighCardFigure(CardValue.QUEEN))

def test_find_high_value_jack():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)]
    assert(return_high_hands(cards)==HighCardFigure(CardValue.JACK))

def test_find_high_value_ten():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==HighCardFigure(CardValue.TEN))

def test_find_high_value_nine():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==HighCardFigure(CardValue.NINE))

def test_find_high_value_eight():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==HighCardFigure(CardValue.EIGHT))

def test_find_high_value_seven():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==HighCardFigure(CardValue.SEVEN))

def test_find_pair_two(): 
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.TWO, CardValue.SEVEN))

def test_find_pair_three(): 
    cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.THREE, CardValue.SEVEN))

def test_find_pair_four(): 
    cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.FOUR, CardValue.SEVEN))

def test_find_pair_five(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.FIVE, CardValue.SEVEN))

def test_find_pair_six(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.SIX, CardValue.SEVEN))

def test_find_pair_seven(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.SEVEN, CardValue.SIX))

def test_find_pair_eight(): 
    cards =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.EIGHT, CardValue.SEVEN))

def test_find_pair_nine(): 
    cards =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.NINE, CardValue.SEVEN))

def test_find_pair_ten(): 
    cards =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.TEN, CardValue.SEVEN))

def test_find_pair_jack(): 
    cards =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.JACK, CardValue.SEVEN))

def test_find_pair_queen(): 
    cards =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.QUEEN, CardValue.SEVEN))

def test_find_pair_king(): 
    cards =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.KING, CardValue.SEVEN))

def test_find_pair_ace(): 
    cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==PairFigure(CardValue.ACE, CardValue.SEVEN))

def test_find_two_pairs_two_three(): 
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.THREE, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==TwoPairFigure(CardValue.THREE, CardValue.TWO, CardValue.FOUR))

def test_find_two_pairs_four_five(): 
    cards =  [Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    assert(return_high_hands(cards)==TwoPairFigure(CardValue.FIVE, CardValue.FOUR, CardValue.THREE))

def test_find_two_pairs_six_seven(): 
    cards =  [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    assert(return_high_hands(cards)==TwoPairFigure(CardValue.SEVEN, CardValue.SIX, CardValue.FIVE))

def test_find_two_pairs_eight_nine(): 
    cards =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)]
    assert(return_high_hands(cards)==TwoPairFigure(CardValue.NINE, CardValue.EIGHT, CardValue.SIX))

def test_find_two_pairs_ten_ace(): 
    cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.ACE, CardColor.SPADES)]
    assert(return_high_hands(cards)==TwoPairFigure(CardValue.ACE, CardValue.TEN, CardValue.NINE))

def test_find_two_pairs_jack_queen(): 
    cards =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==TwoPairFigure(CardValue.QUEEN, CardValue.JACK, CardValue.NINE))

def test_find_two_pairs_king_six(): 
    cards =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.KING, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==TwoPairFigure(CardValue.KING, CardValue.SIX, CardValue.QUEEN))

def test_find_three_of_a_two(): 
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.TWO, CardValue.ACE))

def test_find_three_of_a_three(): 
    cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.THREE, CardValue.FOUR))

def test_find_three_of_a_four(): 
    cards =  [Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.FOUR, CardValue.THREE))

def test_find_three_of_a_five(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.FIVE, CardValue.FOUR))

def test_find_three_of_a_six(): 
    cards =  [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.SIX, CardValue.FOUR))

def test_find_three_of_a_seven(): 
    cards =  [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.SEVEN, CardValue.SIX))

def test_find_three_of_a_eight(): 
    cards =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.EIGHT, CardValue.SEVEN))

def test_find_three_of_a_nine(): 
    cards =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.NINE, CardValue.EIGHT))

def test_find_three_of_a_ten(): 
    cards =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.TEN, CardValue.QUEEN))

def test_find_three_of_a_jack(): 
    cards =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.JACK, CardValue.QUEEN))

def test_find_three_of_a_queen(): 
    cards =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.QUEEN, CardValue.JACK))

def test_find_three_of_a_king(): 
    cards =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.KING, CardValue.QUEEN))

def test_find_three_of_a_ace(): 
    cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.ACE, CardValue.KING))

def test_find_straight_finish_six():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.THREE, CardColor.SPADES)]
    assert(return_high_hands(cards)==StraitFigure(CardValue.SIX))

def test_find_straight_finish_jack():
    cards =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==StraitFigure(CardValue.JACK))

def test_find_straight_finish_ace():
    cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)]
    assert(return_high_hands(cards)==StraitFigure(CardValue.ACE))

def test_find_flush_hearts_by_king():
    hand = [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.HEARTS)]
    assert(FlushFigure(CardColor.HEARTS, CardValue.KING) == return_high_hands(hand))

def test_find_flush_clubs_by_queen():
    hand = [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.CLUBS)]
    assert(FlushFigure(CardColor.CLUBS, CardValue.QUEEN) == return_high_hands(hand))

def test_find_flush_spades_by_jack():
    hand = [Card(CardValue.SEVEN, CardColor.SPADES), Card(CardValue.THREE, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)]
    assert(FlushFigure(CardColor.SPADES, CardValue.JACK) == return_high_hands(hand))

def test_find_full_king_two_times_jack_three_times():
    hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS)]
    assert(FullFigure(CardValue.KING, CardValue.JACK) == return_high_hands(hand))

def test_find_full_ten_two_times_nine_three_times():
    hand = [Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS)]
    assert(FullFigure(CardValue.TEN, CardValue.NINE) == return_high_hands(hand))

def test_find_full_eight_two_times_seven_three_times():
    hand = [Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
    assert(FullFigure(CardValue.EIGHT, CardValue.SEVEN) == return_high_hands(hand))

def test_find_full_six_two_times_five_three_times():
    hand = [Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(FullFigure(CardValue.SIX, CardValue.FIVE) == return_high_hands(hand))

def test_find_full_four_two_times_three_three_times():
    hand = [Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS)]
    assert(FullFigure(CardValue.FOUR, CardValue.THREE) == return_high_hands(hand))

def test_find_full_ace_two_times_SEVEN_three_times():
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
    assert(FullFigure(CardValue.ACE, CardValue.SEVEN) == return_high_hands(hand))


def return_high_hands(cards):
    hand = Hand()
    card_most_representative = hand.determinate_high_figure(cards)
    return card_most_representative