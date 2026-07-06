from enum import Enum

class Winner(Enum):
    EQUALITY = 0
    FIRST_HAND = 1
    SECOND_HAND = 2
    UNDETERMINATED = -9999