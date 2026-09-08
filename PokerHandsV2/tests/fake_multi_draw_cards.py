from PokerHandsV2.card import Card

class FakeMultiDrawCards():
    def __init__(self, fake_cards):
        self.fake_cards = fake_cards
    
    def draw_one_card(self):
        card_choose_fake = self.fake_cards.pop(0)
        card_choose = Card.parse(card_choose_fake)
        return card_choose