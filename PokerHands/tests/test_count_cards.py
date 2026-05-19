from PokerHands.card import Card, CardColor, CardValue
from PokerHands.hand import Hand

def test_count_cards_with_each_cards_different() : 
    hand = [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.TWO : 1, CardValue.THREE : 1, CardValue.FOUR : 1, CardValue.FIVE : 1, CardValue.SIX : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_two_cards() : 
    hand = [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.TWO : 2, CardValue.FOUR : 1, CardValue.FIVE : 1, CardValue.SIX : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_three_cards() : 
    hand = [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.THREE : 2, CardValue.FOUR : 1, CardValue.FIVE : 1, CardValue.SIX : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_four_cards() : 
    hand = [Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.FOUR : 3, CardValue.FIVE : 1, CardValue.SIX : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_five_cards() : 
    hand = [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.FOUR : 1, CardValue.FIVE : 3, CardValue.SIX : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_six_cards() : 
    hand = [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.SIX : 2, CardValue.FIVE : 2, CardValue.FOUR : 1  }
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_seven_cards() : 
    hand = [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.SEVEN : 2, CardValue.FOUR : 1, CardValue.SIX : 1, CardValue.FIVE : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_eight_cards() : 
    hand = [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.EIGHT : 2, CardValue.FOUR : 1, CardValue.SIX : 1, CardValue.FIVE : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_nine_cards() : 
    hand = [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.NINE : 2, CardValue.FOUR : 1, CardValue.SIX : 1, CardValue.FIVE : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_ten_cards() : 
    hand = [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.TEN : 2, CardValue.FOUR : 1, CardValue.SIX : 1, CardValue.FIVE : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_jacks_cards() : 
    hand = [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES)]
    count_expected =  {CardValue.JACK : 2, CardValue.FOUR : 1, CardValue.SIX : 1, CardValue.FIVE : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_queens_cards() : 
    hand = [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES)]
    count_expected =  {CardValue.QUEEN : 2, CardValue.JACK : 1, CardValue.FOUR : 1, CardValue.SIX : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_kings_cards() : 
    hand = [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.KING, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES)]
    count_expected =  {CardValue.KING : 2, CardValue.JACK : 1, CardValue.FOUR : 1, CardValue.QUEEN : 1}
    assert(__count_cards(hand) == count_expected)

def test_count_cards_with_two_ace_cards() : 
    hand = [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.HEARTS), Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES)]
    count_expected =  {CardValue.ACE : 2, CardValue.JACK : 1, CardValue.FOUR : 1, CardValue.QUEEN : 1}
    assert(__count_cards(hand) == count_expected)

def __count_cards(content_hand) :
    hand = Hand(content_hand)
    return hand.count_hand()