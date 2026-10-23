from PokerHands.game.game_result.pre_flop_phase_result import PreFlopPhaseResult

class PreFlopPhase :
    def __init__(self, players, table):
        self.players = players
        self.table = table
        
    def launch_phase_and_get_best_players(self):
        self.__add_all_players()
        self.__each_players_draw_cards_two_times()
        pre_flop_result = PreFlopPhaseResult.create(self.table.players)
        return pre_flop_result
    
    def __add_all_players(self):
        for player in self.players : 
            self.table.add_player(player)
            
    def __each_players_draw_cards_two_times(self):
        self.__each_players_draw_one_card_first_time()
        self.__each_players_draw_one_card_second_time()
        
    def __each_players_draw_one_card_first_time(self):
        for player_name in self.players : 
            self.table.deal_card(player_name)
        
    def __each_players_draw_one_card_second_time(self):
        for player_name in self.players : 
            self.table.deal_card(player_name)