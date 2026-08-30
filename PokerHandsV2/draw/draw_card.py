import random

class DrawCard : 
    def __init__(self):
        pass

    def pick_one(self, deck_cards):
        idx_card_spread = random.randint(0, len(deck_cards) - 1)
        card_spread = deck_cards[idx_card_spread]
        return card_spread