class DrawPhase :
    def __init__(self, players, hands_manager):
        self.players = players
        self.hands_manager = hands_manager
        
    def launch_phase_and_get_best_players(self):
        self.__add_all_players()
        self.__each_players_draw_cards_two_times()
        best_players = self.hands_manager.get_players_with_best_hands()
        return best_players
    
    def __add_all_players(self):
        for player in self.players : 
            self.hands_manager.add_player(player)
            
    def __each_players_draw_cards_two_times(self):
        self.__each_players_draw_one_card_first_time()
        self.__each_players_draw_one_card_second_time()
        
    def __each_players_draw_one_card_first_time(self):
        for player in self.players : 
            self.hands_manager.draw_card_player(player)
        
    def __each_players_draw_one_card_second_time(self):
        for player in self.players : 
            self.hands_manager.draw_card_player(player)