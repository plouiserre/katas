import random

from PokerHands.card import Card, CardColor, CardValue

def test_1():
    card_spread = (CardSpreadDriver()
                   .spread_one_card()
                   .get_card_spread_and_rest_cards())
    
    assert(card_spread.value in CardValue)
    assert(card_spread.color in CardColor)
    
    
class CardSpreadDriver():
    def __init__(self):
        self.deck_cards = self.__build_all_cards()
     
    def spread_one_card(self):
        return self
    
    def get_card_spread_and_rest_cards(self):
        idx_card_spread = random.randint(0, len(self.deck_cards) - 1)
        card_spread = self.deck_cards[idx_card_spread]
        return card_spread
    
    def __build_all_cards(self):
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