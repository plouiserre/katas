from PokerHands.card import Card

class Player : 
    def __init__(self, hand):
        self.hand = hand

    def calculate_hand(self, hand_content):
        all_cards = []
        for card_acronym in hand_content :
            new_card = Card.parse(card_acronym)
            all_cards.append(new_card)
        high_figure = self.hand.determinate_high_figure(all_cards)
        return high_figure
    