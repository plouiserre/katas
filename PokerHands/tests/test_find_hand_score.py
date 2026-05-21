from PokerHands.card import Card, CardColor, CardValue
from PokerHands.hand import Hand, HighFigure
from PokerHands.score import Score

def test_find_high_value_ace():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.ACE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, CardValue.ACE))

def test_find_high_value_king():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, CardValue.KING))

def test_find_high_value_queen():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, CardValue.QUEEN))

def test_find_high_value_jack():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS),Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, CardValue.JACK))

def test_find_high_value_ten():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.TEN, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, CardValue.TEN))

def test_find_high_value_nine():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, CardValue.NINE))

def test_find_high_value_eight():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, CardValue.EIGHT))

def test_find_high_value_seven():
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.HIGH_VALUE, CardValue.SEVEN))

def test_find_pair_two(): 
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.TWO))

def test_find_pair_three(): 
    cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.THREE))

def test_find_pair_four(): 
    cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.FOUR))

def test_find_pair_five(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.FIVE))

def test_find_pair_six(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.SIX))

def test_find_pair_seven(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.SEVEN))

def test_find_pair_eight(): 
    cards =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.EIGHT))

def test_find_pair_nine(): 
    cards =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.NINE))

def test_find_pair_ten(): 
    cards =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.TEN))

def test_find_pair_jack(): 
    cards =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.JACK))

def test_find_pair_queen(): 
    cards =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.QUEEN))

def test_find_pair_king(): 
    cards =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.KING, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.KING))

def test_find_pair_ace(): 
    cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.PAIR, CardValue.ACE))

def test_find_three_of_a_two(): 
    cards =  [Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.TWO))

def test_find_three_of_a_three(): 
    cards =  [Card(CardValue.THREE, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.THREE))

def test_find_three_of_a_four(): 
    cards =  [Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.FOUR))

def test_find_three_of_a_five(): 
    cards =  [Card(CardValue.FIVE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.FIVE))

def test_find_three_of_a_six(): 
    cards =  [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.SIX))

def test_find_three_of_a_seven(): 
    cards =  [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.SEVEN, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.SEVEN))

def test_find_three_of_a_eight(): 
    cards =  [Card(CardValue.EIGHT, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.EIGHT))

def test_find_three_of_a_nine(): 
    cards =  [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.NINE))

def test_find_three_of_a_ten(): 
    cards =  [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.TEN))

def test_find_three_of_a_jack(): 
    cards =  [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.JACK))

def test_find_three_of_a_queen(): 
    cards =  [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.QUEEN))

def test_find_three_of_a_king(): 
    cards =  [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.KING))

def test_find_three_of_a_ace(): 
    cards =  [Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES)]
    assert(return_high_hands(cards)==Score(HighFigure.THREE_OF_A_KIND, CardValue.ACE))

def return_high_hands(cards):
    hand = Hand()
    cards_identified = hand.count_all_cards(cards)
    high_figure = hand.determinate_high_figure(cards_identified)
    card_most_representative = hand.find_more_presents_cards(cards_identified)
    if high_figure == HighFigure.PAIR : 
        return Score(HighFigure.PAIR, card_most_representative)
    elif high_figure == HighFigure.THREE_OF_A_KIND : 
        return Score(HighFigure.THREE_OF_A_KIND, card_most_representative)
    else : 
        return __manage_high_score_Score(cards)
    
def __manage_high_score_Score(cards):
    max_value = 0   
    high_score = CardValue.TWO
    for card in cards : 
        if max_value < card.value.value :
            high_score = card.value
            max_value = card.value.value
    return Score(HighFigure.HIGH_VALUE, high_score)