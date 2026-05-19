from PokerHands.card import Card, CardColor, CardValue
from PokerHands.score import Score, HighFigure, FigureValue

def test_find_high_value_ace():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.ACE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, FigureValue.ACE_SCORE))

def test_find_high_value_king():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, FigureValue.KING_SCORE))

def test_find_high_value_queen():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, FigureValue.QUEEN_SCORE))

def test_find_high_value_jack():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, FigureValue.JACK_SCORE))

def test_find_high_value_ten():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, FigureValue.TEN_SCORE))

def test_find_high_value_nine():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, FigureValue.NINE_SCORE))

def test_find_high_value_eight():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, FigureValue.EIGHT_SCORE))

def test_find_high_value_seven():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, FigureValue.SEVEN_SCORE))

def test_find_pair_two(): 
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.TWO_SCORE))

def test_find_pair_three(): 
    cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.THREE_SCORE))

def test_find_pair_four(): 
    cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.FOUR_SCORE))

def test_find_pair_five(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.FIVE_SCORE))

def test_find_pair_six(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.SIX_SCORE))

def test_find_pair_seven(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.SEVEN_SCORE))

def test_find_pair_eight(): 
    cards =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.EIGHT_SCORE))

def test_find_pair_nine(): 
    cards =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.NINE_SCORE))

def test_find_pair_ten(): 
    cards =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.TEN_SCORE))

def test_find_pair_jack(): 
    cards =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.JACK_SCORE))

def test_find_pair_queen(): 
    cards =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.QUEEN_SCORE))

def test_find_pair_king(): 
    cards =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.KING_SCORE))

def test_find_pair_ace(): 
    cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, FigureValue.ACE_SCORE))

def return_high_hands(cards):
    count_two_cards = 0
    count_three_cards = 0
    count_four_cards = 0
    count_five_cards = 0
    count_six_cards = 0
    count_seven_cards = 0
    count_eight_cards = 0
    count_nine_cards = 0
    count_ten_cards = 0
    count_jack_cards = 0
    count_queen_cards = 0
    count_king_cards = 0
    count_ace_cards = 0
    for card in cards : 
        if card.value == CardValue.TWO : 
            count_two_cards += 1
        elif card.value == CardValue.THREE : 
            count_three_cards += 1
        elif card.value == CardValue.FOUR : 
            count_four_cards += 1
        elif card.value == CardValue.FIVE : 
            count_five_cards += 1
        elif card.value == CardValue.SIX : 
            count_six_cards += 1
        elif card.value == CardValue.SEVEN : 
            count_seven_cards += 1
        elif card.value == CardValue.EIGHT : 
            count_eight_cards += 1
        elif card.value == CardValue.NINE : 
            count_nine_cards += 1
        elif card.value == CardValue.TEN : 
            count_ten_cards += 1
        elif card.value == CardValue.JACK : 
            count_jack_cards += 1
        elif card.value == CardValue.QUEEN : 
            count_queen_cards += 1
        elif card.value == CardValue.KING : 
            count_king_cards += 1
        elif card.value == CardValue.ACE : 
            count_ace_cards += 1
    if count_two_cards == 2 : 
        return Score(HighFigure.PAIR, FigureValue.TWO_SCORE)
    elif count_three_cards == 2 : 
        return Score(HighFigure.PAIR, FigureValue.THREE_SCORE)
    elif count_four_cards == 2 : 
        return Score(HighFigure.PAIR, FigureValue.FOUR_SCORE)
    elif count_five_cards == 2 : 
        return Score(HighFigure.PAIR, FigureValue.FIVE_SCORE)
    elif count_six_cards == 2 : 
        return Score(HighFigure.PAIR, FigureValue.SIX_SCORE)
    elif count_seven_cards == 2 : 
        return Score(HighFigure.PAIR, FigureValue.SEVEN_SCORE)
    elif count_eight_cards == 2 :
        return Score(HighFigure.PAIR, FigureValue.EIGHT_SCORE)
    elif count_nine_cards == 2 :
        return Score(HighFigure.PAIR, FigureValue.NINE_SCORE)
    elif count_ten_cards == 2 :
        return Score(HighFigure.PAIR, FigureValue.TEN_SCORE)
    elif count_jack_cards == 2 :
        return Score(HighFigure.PAIR, FigureValue.JACK_SCORE)
    elif count_queen_cards == 2 :
        return Score(HighFigure.PAIR, FigureValue.QUEEN_SCORE)
    elif count_king_cards == 2 :
        return Score(HighFigure.PAIR, FigureValue.KING_SCORE)
    elif count_ace_cards == 2 :
        return Score(HighFigure.PAIR, FigureValue.ACE_SCORE)
    else : 
        return __manage_high_score_Score(cards)
    
def __manage_high_score_Score(cards):
    max_value = FigureValue.TWO_SCORE
    for card in cards : 
        if card.value == CardValue.ACE : 
            max_value = FigureValue.ACE_SCORE
        elif card.value == CardValue.KING and FigureValue.KING_SCORE > max_value: 
            max_value = FigureValue.KING_SCORE
        elif card.value == CardValue.QUEEN  and FigureValue.QUEEN_SCORE > max_value: 
            max_value = FigureValue.QUEEN_SCORE
        elif card.value == CardValue.JACK  and FigureValue.JACK_SCORE > max_value: 
            max_value = FigureValue.JACK_SCORE
        elif card.value == CardValue.TEN  and FigureValue.TEN_SCORE > max_value: 
            max_value = FigureValue.TEN_SCORE
        elif card.value == CardValue.NINE  and FigureValue.NINE_SCORE > max_value: 
            max_value = FigureValue.NINE_SCORE
        elif card.value == CardValue.EIGHT  and FigureValue.EIGHT_SCORE > max_value: 
            max_value = FigureValue.EIGHT_SCORE
        elif card.value == CardValue.SEVEN  and FigureValue.SEVEN_SCORE > max_value: 
            max_value = FigureValue.SEVEN_SCORE
    return Score(HighFigure.HIGH_VALUE, max_value)