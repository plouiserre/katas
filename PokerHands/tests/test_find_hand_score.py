from PokerHands.card import Card, CardColor, CardValue
from PokerHands.hand import Hand, HandScore, HandValue

def test_find_high_value_ace():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.ACE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Hand(HandValue.HIGH_VALUE, HandScore.ACE_SCORE))

def test_find_high_value_king():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==Hand(HandValue.HIGH_VALUE, HandScore.KING_SCORE))

def test_find_high_value_queen():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Hand(HandValue.HIGH_VALUE, HandScore.QUEEN_SCORE))

def test_find_high_value_jack():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)]
    assert(return_high_hands(cards)==Hand(HandValue.HIGH_VALUE, HandScore.JACK_SCORE))

def test_find_high_value_ten():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Hand(HandValue.HIGH_VALUE, HandScore.TEN_SCORE))

def test_find_high_value_nine():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Hand(HandValue.HIGH_VALUE, HandScore.NINE_SCORE))

def test_find_high_value_eight():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Hand(HandValue.HIGH_VALUE, HandScore.EIGHT_SCORE))

def test_find_high_value_seven():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Hand(HandValue.HIGH_VALUE, HandScore.SEVEN_SCORE))

def return_high_hands(cards):
    max_value = HandScore.TWO_SCORE
    for card in cards : 
        if card.value == CardValue.ACE : 
            max_value = HandScore.ACE_SCORE
        elif card.value == CardValue.KING and HandScore.KING_SCORE > max_value: 
            max_value = HandScore.KING_SCORE
        elif card.value == CardValue.QUEEN  and HandScore.QUEEN_SCORE > max_value: 
            max_value = HandScore.QUEEN_SCORE
        elif card.value == CardValue.JACK  and HandScore.JACK_SCORE > max_value: 
            max_value = HandScore.JACK_SCORE
        elif card.value == CardValue.TEN  and HandScore.TEN_SCORE > max_value: 
            max_value = HandScore.TEN_SCORE
        elif card.value == CardValue.NINE  and HandScore.NINE_SCORE > max_value: 
            max_value = HandScore.NINE_SCORE
        elif card.value == CardValue.EIGHT  and HandScore.EIGHT_SCORE > max_value: 
            max_value = HandScore.EIGHT_SCORE
        elif card.value == CardValue.SEVEN  and HandScore.SEVEN_SCORE > max_value: 
            max_value = HandScore.SEVEN_SCORE
    return Hand(HandValue.HIGH_VALUE, max_value)