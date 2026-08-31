class FakeMultiDrawCards():
    def __init__(self, fake_cards):
        self.fake_cards = fake_cards
    
    def draw_one_card(self):
        card_choose = self.fake_cards.pop(0)
        return card_choose