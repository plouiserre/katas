from PokerHands.game.game import PhasePoker

class StatistiquesWinnerPlayers : 
    def __init__(self, games_results):
        self.games_results = games_results

    def calculate_percentage_players_win_in_river(self):
        percentage_winner_players_river = {}
        winners_each_river = {}
        total_game = 0
        for game_result in self.games_results : 
            for phase in game_result : 
                if phase == PhasePoker.RIVER :
                    total_game += 1
                    for winner in game_result[phase].winners :
                        if (winner in winners_each_river) == False : 
                            winners_each_river[winner] = 0
                        winners_each_river[winner] += 1
        for winner in winners_each_river :
            percentage_winner_players_river[winner] = winners_each_river[winner]/total_game
        return percentage_winner_players_river

    def calculate_percentage_players_win_everywhere(self):
        percentage_winner_players_everywhere = {}
        winners_each_river = {}
        total_game = 0
        for game_result in self.games_results : 
            for phase in game_result : 
                total_game += 1
                for winner in game_result[phase].winners :
                    if (winner in winners_each_river) == False : 
                        winners_each_river[winner] = 0
                    winners_each_river[winner] += 1
        for winner in winners_each_river :
            percentage_winner_players_everywhere[winner] = winners_each_river[winner]/total_game 
        return percentage_winner_players_everywhere