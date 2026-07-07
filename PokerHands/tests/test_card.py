import random

from PokerHands.card import Card, CardColor, CardValue

# cartes = "♠ ♥ ♦ ♣"
    
def test_card_transcription_processus():
    numbers = ["2","3","4","5","6","7","8","9","10", "J", "Q", "K", "A"]
    idx_card_number = random.randrange(0, len(numbers) - 1)
    
    color = ["♠", "♥", "♦", "♣"]
    idx_card_color = random.randrange(0, len(color) - 1)
    
    card_transcription = numbers[idx_card_number]+color[idx_card_color]    
    assert(card_transcription == identify_card(card_transcription))    

def identify_card(card_transcription):
   card = Card.parse(card_transcription)
   card_transcription_render = card.render()
   return card_transcription_render

def test_card_parsing(): 
    numbers = ["2","3","4","5","6","7","8","9","10", "J", "Q", "K", "A"]
    numbers_value = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,
                     CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE,
                     CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING]
    idx_card_number = random.randrange(0, len(numbers) - 1)
    
    color = ["♠", "♥", "♦", "♣"]
    color_value = [CardColor.SPADES, CardColor.HEARTS, CardColor.DIAMONDS, CardColor.CLUBS]
    idx_card_color = random.randrange(0, len(color) - 1)

    card_to_parse = numbers[idx_card_number]+color[idx_card_color]
    card_parsing_expected = Card(numbers_value[idx_card_number], color_value[idx_card_color])
    
    assert(card_parsing_expected == parse_card(card_to_parse))

def parse_card(card_writing) : 
    card = Card.parse(card_writing)
    return card