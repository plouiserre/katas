from PokerHands.card import Card, CardColor, CardValue
from PokerHands.draw.draw_card import DrawCard

def test_1():
    card_draw = (MultiDrawCardDriver()
                 .draw_one_card()
                 .get_all_cards_draw())

    assert(len(card_draw) == 1)

def test_2():
    i = 0
    while i < 200 :
        three_cards_draw = (MultiDrawCardDriver()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .get_all_cards_draw())
        three_card_draw_unique_element = set(three_cards_draw)
        assert(len(three_cards_draw) == 3)
        assert (len(three_cards_draw) == len(three_card_draw_unique_element))
        i += 1

def test_3():
    i = 0
    while i < 200 :
        twelve_cards_draw = (MultiDrawCardDriver()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .draw_one_card()
                            .get_all_cards_draw())
        twelve_card_draw_unique_element = set(twelve_cards_draw)
        assert(len(twelve_cards_draw) == 12)
        assert (len(twelve_cards_draw) == len(twelve_card_draw_unique_element))
        i += 1


class MultiDrawCardDriver(): 
    def __init__(self):
        self.deck_cards = self.__build_deck_cards()
        self.draw_card = DrawCard()
        self.all_cards_picks = []

    def draw_one_card(self):
        card_pick =  self.draw_card.pick_one(self.deck_cards)
        self.deck_cards.remove(card_pick)
        self.all_cards_picks.append(card_pick)
        return self

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

