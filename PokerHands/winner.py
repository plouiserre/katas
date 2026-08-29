from enum import Enum

class Winner(Enum):
    EQUALITY = 0
    FIRST_HAND = 1
    SECOND_HAND = 2
    THIRD_HAND = 3
    FOURTH_HAND = 4
    FIFTH_HAND = 5
    SIXTH_HAND = 6
    UNDETERMINATED = -9999