# from PokerHands.card import Card, CardColor, CardValue
# from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure, ThreeOfKindFigure, StraitFigure, FlushFigure, FullFigure, FourOfKindFigure, QuinteFlush
# from PokerHands.hand import Hand, HighCardFigure


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