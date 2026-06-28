import random

from PokerHands.card import Card

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
