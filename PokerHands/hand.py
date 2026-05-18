from enum import Enum, IntEnum

class Hand :
    def __init__(self, hand_name, score_name):
        self.hand_name = hand_name
        self.score_name = score_name
        
    def __eq__(self, other):
        return other.hand_name == self.hand_name and self.score_name == other.score_name 

class HandValue(Enum) : 
    HIGH_VALUE = 19
    PAIR = 20

class HandScore(IntEnum):
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