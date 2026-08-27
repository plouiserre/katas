from PokerHands.card import Card, CardColor, CardValue
from PokerHands.draw.draw_card import DrawCard


class MultiDrawCards: 
    def __init__(self):
        self.deck_cards = self.__build_deck_cards()
        self.draw_card = DrawCard()
        self.all_cards_picks = []

    def draw_one_card(self):
        card_pick =  self.draw_card.pick_one(self.deck_cards)
        self.deck_cards.remove(card_pick)
        self.all_cards_picks.append(card_pick)
        return card_pick

    def get_all_cards_draw(self):
         return self.all_cards_picks

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