import random

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.draw.draw_card import DrawCard

def test_1():
    card_spread = (CardSpreadDriver()
                   .spread_one_card()
                   .get_card_spread_and_rest_cards())
    
    assert(card_spread.value in CardValue)
    assert(card_spread.value != CardValue.UNDEFINED)
    assert(card_spread.color in CardColor)
    assert(card_spread.color != CardColor.UNDEFINED)

def test_2(): 
    i = 0
    while i < 200 : 
        card_spread = (CardSpreadDriver()
                           .spread_one_card()
                           .get_card_spread_and_rest_cards())
            
        assert(card_spread.value in CardValue)
        assert(card_spread.value != CardValue.UNDEFINED)
        assert(card_spread.color in CardColor)
        assert(card_spread.color != CardColor.UNDEFINED)
        i+= 1
    
    
class CardSpreadDriver():
    def __init__(self):
        self.deck_cards = self.__build_deck_cards()
        self.draw_card = DrawCard()
     
    def spread_one_card(self):
        return self
    
    def get_card_spread_and_rest_cards(self):
        return self.draw_card.pick_one(self.deck_cards)
    
    def __build_deck_cards(self):
        all_cards = []
        for card_value in CardValue:
            if card_value == CardValue.UNDEFINED : 
                continue 
            for card_color in CardColor : 
                if card_color == CardColor.UNDEFINED :
                    continue
                card = Card(card_value, card_color)
                all_cards.append(card)
        return all_cards