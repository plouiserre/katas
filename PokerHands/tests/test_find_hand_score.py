from PokerHands.card import Card, CardColor, CardValue
from PokerHands.hand import Hand, HighFigure
from PokerHands.score import Score, FigureValue

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

def test_find_three_of_a_two(): 
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.TWO_SCORE))

def test_find_three_of_a_three(): 
    cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.THREE_SCORE))

def test_find_three_of_a_four(): 
    cards =  [Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.FOUR_SCORE))

def test_find_three_of_a_five(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.FIVE_SCORE))

def test_find_three_of_a_six(): 
    cards =  [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.SIX_SCORE))

def test_find_three_of_a_seven(): 
    cards =  [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.SEVEN_SCORE))

def test_find_three_of_a_eight(): 
    cards =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.EIGHT_SCORE))

def test_find_three_of_a_nine(): 
    cards =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.NINE_SCORE))

def test_find_three_of_a_ten(): 
    cards =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.TEN_SCORE))

def test_find_three_of_a_jack(): 
    cards =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.JACK_SCORE))

def test_find_three_of_a_queen(): 
    cards =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.QUEEN_SCORE))

def test_find_three_of_a_king(): 
    cards =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.KING_SCORE))

def test_find_three_of_a_ace(): 
    cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, FigureValue.ACE_SCORE))

def return_high_hands(cards):
    hand = Hand()
    cards_identified = hand.count_all_cards(cards)
    high_figure = hand.determinate_high_figure(cards_identified)
    if high_figure == HighFigure.PAIR : 
        return __determinate_score(cards_identified, HighFigure.PAIR, 2)
    elif high_figure == HighFigure.THREE_OF_A_KIND : 
        return __determinate_score(cards_identified, HighFigure.THREE_OF_A_KIND, 3)
    else : 
        return __manage_high_score_Score(cards)
    
def __determinate_score(cards_identified, high_figure, number_cards_implicated) : 
    if CardValue.TWO in cards_identified and cards_identified[CardValue.TWO] == number_cards_implicated:
        return Score(high_figure, FigureValue.TWO_SCORE)
    elif CardValue.THREE in cards_identified and cards_identified[CardValue.THREE] == number_cards_implicated:
        return Score(high_figure, FigureValue.THREE_SCORE)
    elif CardValue.FOUR in cards_identified and cards_identified[CardValue.FOUR] == number_cards_implicated:
        return Score(high_figure, FigureValue.FOUR_SCORE)
    elif CardValue.FIVE in cards_identified and cards_identified[CardValue.FIVE] == number_cards_implicated:
        return Score(high_figure, FigureValue.FIVE_SCORE)
    elif CardValue.SIX in cards_identified and cards_identified[CardValue.SIX] == number_cards_implicated:
        return Score(high_figure, FigureValue.SIX_SCORE)
    elif CardValue.SEVEN in cards_identified and cards_identified[CardValue.SEVEN] == number_cards_implicated:
        return Score(high_figure, FigureValue.SEVEN_SCORE)
    elif CardValue.EIGHT in cards_identified and cards_identified[CardValue.EIGHT] == number_cards_implicated:
        return Score(high_figure, FigureValue.EIGHT_SCORE)
    elif CardValue.NINE in cards_identified and cards_identified[CardValue.NINE] == number_cards_implicated:
        return Score(high_figure, FigureValue.NINE_SCORE)
    elif CardValue.TEN in cards_identified and cards_identified[CardValue.TEN] == number_cards_implicated:
        return Score(high_figure, FigureValue.TEN_SCORE)
    elif CardValue.JACK in cards_identified and cards_identified[CardValue.JACK] == number_cards_implicated:
        return Score(high_figure, FigureValue.JACK_SCORE)
    elif CardValue.QUEEN in cards_identified and cards_identified[CardValue.QUEEN] == number_cards_implicated:
        return Score(high_figure, FigureValue.QUEEN_SCORE)
    elif CardValue.KING in cards_identified and cards_identified[CardValue.KING] == number_cards_implicated:
        return Score(high_figure, FigureValue.KING_SCORE)
    elif CardValue.ACE in cards_identified and cards_identified[CardValue.ACE] == number_cards_implicated:
        return Score(high_figure, FigureValue.ACE_SCORE)
    
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