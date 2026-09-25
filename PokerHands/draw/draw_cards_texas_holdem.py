from PokerHands.draw.multi_draw_cards import MultiDrawCards

class DrawCardsTexasHoldem :
    def __init__(self):
        self.players = {}
        self.cards_on_table = []
        self.burn_cards = []
        self.multi_draw = MultiDrawCards()

    def add_players(self, player_name):
        self.players[player_name] = []

    def burn_card(self):
            card_burn = self.multi_draw.draw_one_card()
            self.burn_cards.append(card_burn)

    def draw_one_card_for_one_player(self, name_player):
        card_draw = self.multi_draw.draw_one_card()
        self.players[name_player].append(card_draw)

    def draw_flop_cards(self): 
        first_card_draw = self.multi_draw.draw_one_card()
        second_card_draw = self.multi_draw.draw_one_card()
        third_card_draw = self.multi_draw.draw_one_card()
        self.cards_on_table.append(first_card_draw)
        self.cards_on_table.append(second_card_draw)
        self.cards_on_table.append(third_card_draw)

    def draw_river_card(self):
        river_card_draw = self.multi_draw.draw_one_card()
        self.cards_on_table.append(river_card_draw)

    def draw_turn_card(self):
        turn_card_draw = self.multi_draw.draw_one_card()
        self.cards_on_table.append(turn_card_draw)

    def get_all_burns_cards(self) : 
        return self.burn_cards

    def get_all_cards_on_table(self):
        return self.cards_on_table

    def get_players(self): 
        return self.players