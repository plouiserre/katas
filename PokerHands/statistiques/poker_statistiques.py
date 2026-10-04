from PokerHands.game.game import PhasePoker
from PokerHands.statistiques.statistiques_result import StatistiquesResult

class PokerStatistiques : 
    def __init__(self, games_results):
        self.games_results = games_results
        self.percentage_presence_figure_river = {}
        self.percentage_presence_figure_everywhere = {}
        self.percentage_winner_players_river = {}
        self.percentage_winner_players_everywhere = {}
        self.percentage_winning_figure_river = {}    
        self.percentage_winning_figure_everywhere = {}

    def calculate_all_statistiques(self):
        self.__calculate_percentage_presence_all_figures_in_river()
        self.__calculate_percenge_presence_all_figures_everywhere()
        self.__calculate_percentage_players_win_in_river()
        self.__calculate_percentage_players_win_everywhere()
        self.__calculate_percentage_win_all_figure_in_river()
        self.__calculate_percentage_win_all_figure_everywhere()
        return StatistiquesResult(self.percentage_presence_figure_river, self.percentage_presence_figure_everywhere, self.percentage_winner_players_river, self.percentage_winner_players_everywhere, self.percentage_winning_figure_river, self.percentage_winning_figure_everywhere)

    #1 - calculer le % de chaque figure dans la river 
    def __calculate_percentage_presence_all_figures_in_river(self):
        figures_present_in_river = {}
        total_figure = 0
        for game_result in self.games_results : 
            for phase in game_result : 
                if phase == PhasePoker.RIVER: 
                    game = game_result[phase]
                    for player_name in game.hands_by_player : 
                        total_figure += 1
                        figure = game.hands_by_player[player_name]
                        type_figure = type(figure).__name__
                        if (type_figure in figures_present_in_river) == False : 
                            figures_present_in_river[type_figure] = 0
                        figures_present_in_river[type_figure] += 1
        for type_figure in figures_present_in_river : 
                    self.percentage_presence_figure_river[type_figure] = figures_present_in_river[type_figure]/total_figure

    #2 - calculer le % de chaque figure dans chaque phase
    def __calculate_percenge_presence_all_figures_everywhere(self):
        figures_present = {}
        total_figure = 0
        for game_result in self.games_results : 
            for phase in game_result :                 
                game = game_result[phase]
                for player_name in game.hands_by_player : 
                    total_figure += 1
                    figure = game.hands_by_player[player_name]
                    type_figure = type(figure).__name__
                    if (type_figure in figures_present) == False : 
                        figures_present[type_figure] = 0
                    figures_present[type_figure] += 1
        for type_figure in figures_present : 
            self.percentage_presence_figure_everywhere[type_figure] = figures_present[type_figure]/total_figure

    #3 - calculer le % de win pour chaque joueur dans la river 
    def __calculate_percentage_players_win_in_river(self): 
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
            self.percentage_winner_players_river[winner] = winners_each_river[winner]/total_game

    #4 - calculer le % de win pour chaque joueur en tout
    def __calculate_percentage_players_win_everywhere(self):
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
            self.percentage_winner_players_everywhere[winner] = winners_each_river[winner]/total_game 

    #5 - calculer le % de win de chaque figure dans la river 
    def __calculate_percentage_win_all_figure_in_river(self):
        figure_winning_river = {}
        total_game = 0
        for game_result in self.games_results : 
            total_game += 1
            for phase in game_result : 
                if phase == PhasePoker.RIVER : 
                    figure_winner = game_result[phase].best_figure
                    type_figure = type(figure_winner).__name__
                    if (type_figure in figure_winning_river) == False : 
                        figure_winning_river[type_figure] = 0
                    figure_winning_river[type_figure] += 1
        for type_figure in figure_winning_river : 
            self.percentage_winning_figure_river[type_figure] = figure_winning_river[type_figure]/total_game

    #6 - calculer le % de win de chaque figure dans chaque phase
    def __calculate_percentage_win_all_figure_everywhere(self):
            figure_winning_everywhere = {}
            total_game = 0
            for game_result in self.games_results : 
                for phase in game_result : 
                    total_game += 1
                    figure_winner = game_result[phase].best_figure
                    type_figure = type(figure_winner).__name__
                    if (type_figure in figure_winning_everywhere) == False : 
                        figure_winning_everywhere[type_figure] = 0
                    figure_winning_everywhere[type_figure] += 1
            for type_figure in figure_winning_everywhere : 
                self.percentage_winning_figure_everywhere[type_figure] = figure_winning_everywhere[type_figure]/total_game