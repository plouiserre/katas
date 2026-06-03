# from PokerHands.card import Card, CardColor, CardValue
# from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure, ThreeOfKindFigure, StraitFigure, FlushFigure, FullFigure, FourOfKindFigure, QuinteFlush
# from PokerHands.hand import Hand, HighCardFigure

# def test_find_three_of_a_two(): 
#     cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.TWO, CardValue.ACE))

# def test_find_three_of_a_three(): 
#     cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.THREE, CardValue.FOUR))

# def test_find_three_of_a_four(): 
#     cards =  [Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.FOUR, CardValue.THREE))

# def test_find_three_of_a_five(): 
#     cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.FIVE, CardValue.FOUR))

# def test_find_three_of_a_six(): 
#     cards =  [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.SIX, CardValue.FOUR))

# def test_find_three_of_a_seven(): 
#     cards =  [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.SEVEN, CardValue.SIX))

# def test_find_three_of_a_eight(): 
#     cards =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.EIGHT, CardValue.SEVEN))

# def test_find_three_of_a_nine(): 
#     cards =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.NINE, CardValue.EIGHT))

# def test_find_three_of_a_ten(): 
#     cards =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.TEN, CardValue.QUEEN))

# def test_find_three_of_a_jack(): 
#     cards =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.JACK, CardValue.QUEEN))

# def test_find_three_of_a_queen(): 
#     cards =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.QUEEN, CardValue.JACK))

# def test_find_three_of_a_king(): 
#     cards =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.KING, CardValue.QUEEN))

# def test_find_three_of_a_ace(): 
#     cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
#     assert(return_high_hands(cards)==ThreeOfKindFigure(CardValue.ACE, CardValue.KING))

# def test_find_straight_finish_six():
#     cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.THREE, CardColor.SPADES)]
#     assert(return_high_hands(cards)==StraitFigure(CardValue.SIX))

# def test_find_straight_finish_jack():
#     cards =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
#     assert(return_high_hands(cards)==StraitFigure(CardValue.JACK))

# def test_find_straight_finish_ace():
#     cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)]
#     assert(return_high_hands(cards)==StraitFigure(CardValue.ACE))

# def test_find_flush_hearts_by_king():
#     hand = [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.HEARTS)]
#     assert(FlushFigure(CardColor.HEARTS, CardValue.KING) == return_high_hands(hand))

# def test_find_flush_clubs_by_queen():
#     hand = [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.CLUBS)]
#     assert(FlushFigure(CardColor.CLUBS, CardValue.QUEEN) == return_high_hands(hand))

# def test_find_flush_spades_by_jack():
#     hand = [Card(CardValue.SEVEN, CardColor.SPADES), Card(CardValue.THREE, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)]
#     assert(FlushFigure(CardColor.SPADES, CardValue.JACK) == return_high_hands(hand))

# def test_find_full_king_two_times_jack_three_times():
#     hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS)]
#     assert(FullFigure(CardValue.KING, CardValue.JACK) == return_high_hands(hand))

# def test_find_full_ten_two_times_nine_three_times():
#     hand = [Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS)]
#     assert(FullFigure(CardValue.TEN, CardValue.NINE) == return_high_hands(hand))

# def test_find_full_eight_two_times_seven_three_times():
#     hand = [Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
#     assert(FullFigure(CardValue.EIGHT, CardValue.SEVEN) == return_high_hands(hand))

# def test_find_full_six_two_times_five_three_times():
#     hand = [Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
#     assert(FullFigure(CardValue.SIX, CardValue.FIVE) == return_high_hands(hand))

# def test_find_full_four_two_times_three_three_times():
#     hand = [Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS)]
#     assert(FullFigure(CardValue.FOUR, CardValue.THREE) == return_high_hands(hand))

# def test_find_full_ace_two_times_SEVEN_three_times():
#     hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
#     assert(FullFigure(CardValue.ACE, CardValue.SEVEN) == return_high_hands(hand))

# def test_find_four_of_king_with_queen_high_cards():
#     hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.KING, CardValue.QUEEN) == return_high_hands(hand))

# def test_find_four_of_ace_with_six_high_cards():
#     hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.ACE, CardValue.SIX) == return_high_hands(hand))

# def test_find_four_of_jack_with_king_high_cards():
#     hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.JACK, CardValue.KING) == return_high_hands(hand))

# def test_find_four_of_ten_with_jack_high_cards():
#     hand = [Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.TEN, CardValue.JACK) == return_high_hands(hand))

# def test_find_four_of_nine_with_eight_high_cards():
#     hand = [Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.NINE, CardValue.EIGHT) == return_high_hands(hand))

# def test_find_four_of_eight_with_seven_high_cards():
#     hand = [Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.EIGHT, CardValue.SEVEN) == return_high_hands(hand))

# def test_find_four_of_seven_with_five_high_cards():
#     hand = [Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.SEVEN, CardValue.FIVE) == return_high_hands(hand))

# def test_find_four_of_six_with_four_high_cards():
#     hand = [Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.SIX, CardValue.FOUR) == return_high_hands(hand))

# def test_find_four_of_five_with_three_high_cards():
#     hand = [Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.FIVE, CardValue.THREE) == return_high_hands(hand))

# def test_find_four_of_four_with_two_high_cards():
#     hand = [Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.FOUR, CardValue.TWO) == return_high_hands(hand))

# def test_find_four_of_two_with_king_high_cards():
#     hand = [Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.DIAMONDS)]
#     assert(FourOfKindFigure(CardValue.TWO, CardValue.KING) == return_high_hands(hand))

# def test_find_quinte_flush_diamonds_with_nine_value():
#     hand = [Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
#     assert(QuinteFlush(CardValue.NINE, CardColor.DIAMONDS) == return_high_hands(hand))

# def test_find_quinte_flush_diamonds_with_six_value():
#     hand = [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.CLUBS)]
#     assert(QuinteFlush(CardValue.SIX, CardColor.CLUBS) == return_high_hands(hand))

# def return_high_hands(cards):
#     hand = Hand()
#     card_most_representative = hand.determinate_high_figure(cards)
#     return card_most_representative