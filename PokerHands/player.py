from PokerHands.card import Card

class Player : 
    def __init__(self, hand):
        self.hand = hand

    def calculate_hand(self, hand_content):
        cards_signs = hand_content.split(" ")
        all_cards = []
        for card_sign in cards_signs :
            new_card = Card.parse(card_sign)
            all_cards.append(new_card)
        high_figure = self.hand.determinate_high_figure(all_cards)
        return high_figure
    