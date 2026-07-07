from enum import IntEnum, Enum
from typing import Self
#TODO separate in folder card_entities this three entities


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

class Card: 
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __eq__(self, other):
        return self.value == other.value and self.color == other.color
    
    def render(self) -> str: 
        transcription = ""
        number = ""
        color = ""
        if self.value == CardValue.ACE: 
            number = "A"
        elif self.value == CardValue.KING : 
            number = "K"
        elif self.value == CardValue.QUEEN :
            number = "Q"
        elif self.value == CardValue.JACK : 
            number = "J"
        else : 
            number = str(self.value)
        if self.color == CardColor.SPADES :
            color = "♠"
        elif self.color == CardColor.HEARTS : 
            color = "♥"
        elif self.color == CardColor.DIAMONDS : 
            color = "♦"
        else : 
            color = "♣"
        transcription = number+color
        return transcription        
    
    @staticmethod
    def parse(str) -> Self:
        card_color = CardColor.UNDEFINED
        card_value = CardValue.UNDEFINED
        card_color = Card.__parse_color(str)
        card_value = Card.__parse_value(str)
        return Card(card_value, card_color)
    
    @staticmethod
    def __parse_color(str) -> CardColor :
        card_color = CardColor.UNDEFINED
        if "♠" in str : 
            card_color = CardColor.SPADES
        elif "♥" in str : 
            card_color = CardColor.HEARTS
        elif "♦" in str :
            card_color = CardColor.DIAMONDS
        elif "♣" in str : 
            card_color = CardColor.CLUBS
        return card_color
    
    @staticmethod
    def __parse_value(str) -> CardValue : 
        if "2" in str : 
            card_value = CardValue.TWO
        elif "3" in str : 
            card_value = CardValue.THREE
        elif "4" in str : 
            card_value = CardValue.FOUR
        elif "5" in str : 
            card_value = CardValue.FIVE
        elif "6" in str : 
            card_value = CardValue.SIX
        elif "7" in str : 
            card_value = CardValue.SEVEN
        elif "8" in str : 
            card_value = CardValue.EIGHT
        elif "9" in str : 
            card_value = CardValue.NINE
        elif "10" in str : 
            card_value = CardValue.TEN
        elif "J" in str : 
            card_value = CardValue.JACK
        elif "Q" in str : 
            card_value = CardValue.QUEEN
        elif "K" in str : 
            card_value = CardValue.KING
        elif "A" in str : 
            card_value = CardValue.ACE
        else : 
            card_value = CardValue.UNDEFINED
        return card_value