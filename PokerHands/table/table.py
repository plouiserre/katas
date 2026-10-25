class Table :
    def __init__(self, multi_draw_cards):
        self.players = {}
        self.multi_draw_cards = multi_draw_cards
        self.all_cards = []
        self.burn_cards = []     
        self.flop_cards = []
        self.turn_card = None
        self.river_card = None

    def add_player(self, name_player):
        self.players[name_player] = []
        return self
    
    def deal_card(self,name_player): 
        one_card = self.multi_draw_cards.draw_one_card()
        self.players[name_player].append(one_card)
        return one_card

    def burn_one_card(self):
        card_burned = self.multi_draw_cards.draw_one_card()
        return card_burned
        
    def deal_flop(self):
        first_card = self.multi_draw_cards.draw_one_card()
        second_card = self.multi_draw_cards.draw_one_card()
        third_card = self.multi_draw_cards.draw_one_card()
        flop_cards = [first_card, second_card, third_card]        
        return flop_cards

    def deal_turn(self):
        turn_card = self.multi_draw_cards.draw_one_card()
        return turn_card
    
    def deal_river(self):
        river_card = self.multi_draw_cards.draw_one_card()
        return river_card

    def affect_card_to_player(self, player_name, card):
        self.players[player_name].append(card)

    def affect_boards_cards_to_players(self, all_cards):
        for player_name in self.players: 
            for card in all_cards : 
                self.players[player_name].append(card)
        return self.players

