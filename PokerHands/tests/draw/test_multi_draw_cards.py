from PokerHands.card import Card, CardColor, CardValue
from PokerHands.draw.multi_draw_cards import MultiDrawCards

def test_draw_one_card():
    card_draw = (MultiDrawCardDriver()
                 .draw_one_card()
                 .get_all_cards_draw())

    assert(len(card_draw) == 1)

def test_draw_three_cards():
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

def test_draw_twelve_cards():
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
        self.multi_draw_cards = MultiDrawCards()

    def draw_one_card(self):
        self.multi_draw_cards.draw_one_card()
        return self

    def get_all_cards_draw(self):
        return self.multi_draw_cards.get_all_cards_draw()