from enum import Enum, IntEnum

class Score: 
    def __init__(self, point, high_figure):
        self.point = point 
        self.high_figure = high_figure

    def __eq__(self, other):
        return other.point == self.point and self.high_figure == other.high_figure


class HighFigure(Enum) : 
    HIGH_VALUE = 1
    PAIR = 2
    THREE_OF_A_KIND = 3

class FigureValue(IntEnum):
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