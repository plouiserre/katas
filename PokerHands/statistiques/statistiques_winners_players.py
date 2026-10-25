from PokerHands.hand.hand import PhasePoker

class StatistiquesWinnerPlayers : 
    def __init__(self, games_results):
        self.games_results = games_results
        
    def calculate_percentage_players_win_in_showdown(self):
        self.winners_each_showdown = {}
        self.total_game = 0
        percentage_winner_players_showdown = {}
        for game in self.games_results :             
            self.__add_winner_in_counting(game, self.winners_each_showdown)
        for winner in self.winners_each_showdown :
            percentage_winner_players_showdown[winner] = self.winners_each_showdown[winner]/self.total_game
        return percentage_winner_players_showdown

    def __add_winner_in_counting(self, game, all_winners_counting):
        self.total_game += 1                    
        for winner in game.winners :
            if (winner in all_winners_counting) == False : 
                all_winners_counting[winner] = 0
            all_winners_counting[winner] += 1