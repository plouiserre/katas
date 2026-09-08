from PokerHandsV2.draw.multi_draw_cards import MultiDrawCards

def test_draw_one_card():
    (MultiDrawCardDriver()
        .draw_one_card()
        .get_all_cards_draw()
        .valid_number_card_draw(1))

def test_draw_three_cards():
    i = 0
    while i < 200 :
        (MultiDrawCardDriver()
            .draw_one_card()
            .draw_one_card()
            .draw_one_card()
            .get_all_cards_draw()
            .valid_number_card_draw(3)
            .valid_all_cards_draw_are_unique())
        i += 1

def test_draw_twelve_cards():
    i = 0
    while i < 200 :
        (MultiDrawCardDriver()
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
            .get_all_cards_draw()
            .valid_number_card_draw(12)
            .valid_all_cards_draw_are_unique())
        i += 1


class MultiDrawCardDriver(): 
    def __init__(self):
        self.multi_draw_cards = MultiDrawCards()
        self.cards_draw = []
                
    def draw_one_card(self):
        self.multi_draw_cards.draw_one_card()
        return self

    def get_all_cards_draw(self):
        self.cards_draw = self.multi_draw_cards.get_all_cards_draw()
        return self

    def valid_number_card_draw(self, number): 
        assert(len(self.cards_draw) == number)
        return self

    def valid_all_cards_draw_are_unique(self):
        cards_draw_unique_element = set(self.cards_draw)
        assert (len(self.cards_draw) == len(cards_draw_unique_element))
        return self