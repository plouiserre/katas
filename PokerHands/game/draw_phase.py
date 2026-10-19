class DrawPhase :
    def __init__(self, players, hand):
        self.players = players
        self.hand = hand
        
    def launch_phase_and_get_best_players(self):
        self.__add_all_players()
        self.__each_players_draw_cards_two_times()
        result = self.hand.get_players_with_best_poker_hands()
        return result
    
    def __add_all_players(self):
        for player in self.players : 
            self.hand.add_player(player)
            
    def __each_players_draw_cards_two_times(self):
        self.__each_players_draw_one_card_first_time()
        self.__each_players_draw_one_card_second_time()
        
    def __each_players_draw_one_card_first_time(self):
        for player in self.players : 
            self.hand.draw_card_player(player)
        
    def __each_players_draw_one_card_second_time(self):
        for player in self.players : 
            self.hand.draw_card_player(player)