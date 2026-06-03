# from PokerHands.card import Card, CardColor, CardValue
# from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure, ThreeOfKindFigure, StraitFigure, FlushFigure, FullFigure, FourOfKindFigure, QuinteFlush
# from PokerHands.hand import Hand, HighCardFigure


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