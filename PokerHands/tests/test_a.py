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
    
    card = numbers[idx_card_number]+color[idx_card_color]    
    assert(Card(result_number[idx_card_number], result_color[idx_card_color]) == identify_card(card))

def test_2():
    card = "10♥"
    assert(Card(CardValue.TEN, CardColor.HEARTS) == identify_card(card))

def test_3():
    card = "J♦"
    assert(Card(CardValue.JACK, CardColor.DIAMONDS) == identify_card(card))

def test_4():
    card = "Q♣"
    assert(Card(CardValue.QUEEN, CardColor.CLUBS) == identify_card(card))

def test_5():
    card = "K♠"
    assert(Card(CardValue.KING, CardColor.SPADES) == identify_card(card))

def test_6():
    card = "A♥"
    assert(Card(CardValue.ACE, CardColor.HEARTS) == identify_card(card))

def identify_card(card):
    card_color = CardColor.UNDEFINED
    card_value = CardValue.UNDEFINED
    value = ""
    if "♠" in card : 
        card_color = CardColor.SPADES
        value = card.replace("♠", "")
    elif "♥" in card : 
        card_color = CardColor.HEARTS
        value = card.replace("♥", "")
    elif "♦" in card :
        card_color = CardColor.DIAMONDS
        value = card.replace("♦", "")
    elif "♣" in card : 
        card_color = CardColor.CLUBS
        value = card.replace("♣", "")
    if "J" in card : 
        card_value = CardValue.JACK
    elif "Q" in card : 
        card_value = CardValue.QUEEN
    elif "K" in card : 
        card_value = CardValue.KING
    elif "A" in card : 
        card_value = CardValue.ACE
    else : 
        number = int(value)
        card_value = number
    return Card(card_value, card_color)