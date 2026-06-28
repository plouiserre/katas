from enum import IntEnum, Enum

class Card: 
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __eq__(self, other):
        return self.value == other.value and self.color == other.color
    
    def render(self): 
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
    def parse(str):
        card_color = CardColor.UNDEFINED
        card_value = CardValue.UNDEFINED
        value = ""
        if "♠" in str : 
            card_color = CardColor.SPADES
            value = str.replace("♠", "")
        elif "♥" in str : 
            card_color = CardColor.HEARTS
            value = str.replace("♥", "")
        elif "♦" in str :
            card_color = CardColor.DIAMONDS
            value = str.replace("♦", "")
        elif "♣" in str : 
            card_color = CardColor.CLUBS
            value = str.replace("♣", "")
        if "J" in str : 
            card_value = CardValue.JACK
        elif "Q" in str : 
            card_value = CardValue.QUEEN
        elif "K" in str : 
            card_value = CardValue.KING
        elif "A" in str : 
            card_value = CardValue.ACE
        else : 
            number = int(value)
            card_value = number
        return Card(card_value, card_color)

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