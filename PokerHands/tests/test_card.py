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

def test_card_parsing_simple(): 
    card_one = "K♥"
    card_two =  "6♣"
    card_one_created = Card.parse(card_one)
    card_two_created = Card.parse(card_two)
    
    assert(card_one_created == Card(CardValue.KING, CardColor.HEARTS))
    assert(type (card_one_created.value) is CardValue)
    assert(card_two_created == Card(CardValue.SIX, CardColor.CLUBS))
    assert(type (card_two_created.value) is CardValue)


def test_card_parsing_random(): 
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
    
    card_parsed = parse_card(card_to_parse)
    assert(card_parsing_expected == card_parsed)
    assert(type (card_parsed.value) is CardValue)

 
def parse_card(card_writing) : 
    card = Card.parse(card_writing)
    return card