def test_1():
    cards =  [Card(TWO, CLUBS), Card(THREE, DIAMONDS), Card(NINE, DIAMONDS), Card(TEN, HEARTS), Card(ACE, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, ACE_SCORE))

def test_2():
    cards =  [Card(TWO, CLUBS), Card(THREE, DIAMONDS),Card(NINE, DIAMONDS), Card(TEN, HEARTS), Card(KING, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, KING_SCORE))

def test_3():
    cards =  [Card(TWO, CLUBS), Card(THREE, DIAMONDS),Card(NINE, DIAMONDS), Card(TEN, HEARTS), Card(QUEEN, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, QUEEN_SCORE))

def test_4():
    cards =  [Card(TWO, CLUBS), Card(THREE, DIAMONDS),Card(NINE, DIAMONDS), Card(TEN, HEARTS), Card(JACK, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, JACK_SCORE))

def test_5():
    cards =  [Card(TWO, CLUBS), Card(NINE, DIAMONDS), Card(EIGHT, HEARTS), Card(TEN, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, TEN_SCORE))

def test_6():
    cards =  [Card(TWO, CLUBS), Card(NINE, DIAMONDS), Card(EIGHT, HEARTS), Card(SIX, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, NINE_SCORE))

def test_7():
    cards =  [Card(TWO, CLUBS), Card(FIVE, DIAMONDS), Card(EIGHT, HEARTS), Card(SIX, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, EIGHT_SCORE))

def test_8():
    cards =  [Card(TWO, CLUBS), Card(FIVE, DIAMONDS), Card(SEVEN, HEARTS), Card(SIX, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, SEVEN_SCORE))

def test_9():
    cards =  [Card(TWO, CLUBS), Card(FIVE, DIAMONDS), Card(FOUR, HEARTS), Card(SIX, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, SIX_SCORE))

def test_10():
    cards =  [Card(TWO, CLUBS), Card(FIVE, DIAMONDS), Card(FOUR, HEARTS), Card(THREE, SPADES)]
    assert(return_high_hands(cards)==Hands(HIGH_VALUE, FIVE_SCORE))


def return_high_hands(cards):
    max_value = TWO_SCORE
    for card in cards : 
        if card.value == ACE : 
            max_value = ACE_SCORE
        elif card.value == KING and KING_SCORE > max_value: 
            max_value = KING_SCORE
        elif card.value == QUEEN  and QUEEN_SCORE > max_value: 
            max_value = QUEEN_SCORE
        elif card.value == JACK  and JACK_SCORE > max_value: 
            max_value = JACK_SCORE
        elif card.value == TEN  and TEN_SCORE > max_value: 
            max_value = TEN_SCORE
        elif card.value == NINE  and NINE_SCORE > max_value: 
            max_value = NINE_SCORE
        elif card.value == EIGHT  and EIGHT_SCORE > max_value: 
            max_value = EIGHT_SCORE
        elif card.value == SEVEN  and SEVEN_SCORE > max_value: 
            max_value = SEVEN_SCORE
        elif card.value == SIX  and SIX_SCORE > max_value: 
            max_value = SIX_SCORE
        elif card.value == FIVE  and FIVE_SCORE > max_value: 
            max_value = FIVE_SCORE
    return Hands(HIGH_VALUE, max_value)


class Card: 
    def __init__(self, value, color):
        self.value = value
        self.color = color

class Hands :
    def __init__(self, hand_name, score_name):
        self.hand_name = hand_name
        self.score_name = score_name
        
    def __eq__(self, other):
        return other.hand_name == self.hand_name and self.score_name == other.score_name 


TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
JACK = 11
QUEEN = 12
KING = 13
ACE = 14

CLUBS = 15
DIAMONDS = 16
HEARTS = 17
SPADES = 18

HIGH_VALUE = 19

TWO_SCORE = 38
THREE_SCORE = 39
FOUR_SCORE = 40
FIVE_SCORE = 41
SIX_SCORE = 42
SEVEN_SCORE = 43
EIGHT_SCORE = 44
NINE_SCORE = 45
TEN_SCORE = 46
JACK_SCORE = 47
QUEEN_SCORE = 48
KING_SCORE = 49
ACE_SCORE = 50