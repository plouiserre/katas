from enum import IntEnum, Enum

class Card: 
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __eq__(self, other):
        return self.value == other.value and self.color == other.color

class CardColor(Enum) : 
    UNDEFINED = 0
    CLUBS = 15
    DIAMONDS = 16
    HEARTS = 17
    SPADES = 18

class CardValue(IntEnum) : 
    UNDEFINED = 0
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