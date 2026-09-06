from PokerHandsV2.card import Card, CardColor, CardValue
from PokerHandsV2.draw.draw_card import DrawCard

def test_draw_one_time_one_card():
    (CardSpreadDriver()
        .get_card_spread_and_rest_cards()
        .valid_card_pick())

def test_draw_two_hundred_times_one_card(): 
    i = 0
    while i < 200 : 
        (CardSpreadDriver()
            .get_card_spread_and_rest_cards()
            .valid_card_pick())
        i+= 1    
    
class CardSpreadDriver():
    def __init__(self):
        self.deck_cards = self.__build_deck_cards()
        self.draw_card = DrawCard()
        self.card_pick = None
    
    def get_card_spread_and_rest_cards(self):
        self.card_pick = self.draw_card.pick_one(self.deck_cards)
        return self

    def valid_card_pick(self):
        is_valid_value = self.card_pick.value in CardValue and self.card_pick.value != CardValue.UNDEFINED
        is_valid_color = self.card_pick.color in CardColor and self.card_pick.color != CardColor.UNDEFINED
        is_valid = is_valid_color and is_valid_value
        assert(is_valid)
    
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