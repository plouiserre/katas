from PokerHands.game.game import PhasePoker

class StatistiquesWinnerPlayers : 
    def __init__(self, games_results):
        self.games_results = games_results
        
    def calculate_percentage_players_win_in_river(self):
        self.winners_each_river = {}
        self.total_game = 0
        percentage_winner_players_river = {}
        for game_result in self.games_results :             
            for phase in game_result : 
                if phase == PhasePoker.RIVER :
                    self.__add_winner_in_counting(game_result[phase], self.winners_each_river)
        for winner in self.winners_each_river :
            percentage_winner_players_river[winner] = self.winners_each_river[winner]/self.total_game
        return percentage_winner_players_river

    def calculate_percentage_players_win_everywhere(self):
        self.winners_everywhere = {}
        self.total_game = 0
        percentage_winner_players_everywhere = {}
        for game_result in self.games_results :             
            for phase in game_result : 
                self.__add_winner_in_counting(game_result[phase], self.winners_everywhere)                
        for winner in self.winners_everywhere :
            percentage_winner_players_everywhere[winner] = self.winners_everywhere[winner]/self.total_game 
        return percentage_winner_players_everywhere

    def __add_winner_in_counting(self, game, all_winners_counting):
        self.total_game += 1                    
        for winner in game.winners :
            if (winner in all_winners_counting) == False : 
                all_winners_counting[winner] = 0
            all_winners_counting[winner] += 1