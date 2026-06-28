import random

from PokerHands.card import Card, CardColor, CardValue

# cartes = "♠ ♥ ♦ ♣"
    
def test_1():
    numbers = ["2","3","4","5","6","7","8","9","10", "J", "Q", "K", "A"]
    result_number = [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,
              CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, 
              CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING,
              CardValue.ACE]
    idx_card_number = random.randrange(0, len(numbers) - 1)
    
    color = ["♠", "♥", "♦", "♣"]
    result_color = [CardColor.SPADES, CardColor.HEARTS, CardColor.DIAMONDS, CardColor.CLUBS]
    idx_card_color = random.randrange(0, len(color) - 1)
    
    card_transcription = numbers[idx_card_number]+color[idx_card_color]    
    assert(card_transcription == identify_card(card_transcription))


def identify_card(card_transcription):
   card = Card.parse(card_transcription)
   card_transcription_render = card.render()
   return card_transcription_render
