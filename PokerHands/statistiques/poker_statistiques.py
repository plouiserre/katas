from PokerHands.game.game import PhasePoker
from PokerHands.statistiques.statistiques_result import StatistiquesResult

class PokerStatistiques : 
    def __init__(self, statistiques_presences_figures , statistiques_winners_players, statistiques_win_figures):
        self.statistiques_presences_figures = statistiques_presences_figures
        self.statistiques_winners_players = statistiques_winners_players
        self.statistiques_win_figures = statistiques_win_figures
        self.percentage_presence_figure_river = {}
        self.percentage_presence_figure_everywhere = {}
        self.percentage_winner_players_river = {}
        self.percentage_winner_players_everywhere = {}
        self.percentage_winning_figure_river = {}    
        self.percentage_winning_figure_everywhere = {}
        self.total_figure = 0

    def calculate_all_statistiques(self):      
        self.percentage_presence_figure_river = self.statistiques_presences_figures.calculate_percentage_presence_all_figures_in_river()
        self.percentage_presence_figure_everywhere = self.statistiques_presences_figures.calculate_percenge_presence_all_figures_everywhere() 
        self.percentage_winner_players_river = self.statistiques_winners_players.calculate_percentage_players_win_in_river()
        self.percentage_winner_players_everywhere = self.statistiques_winners_players.calculate_percentage_players_win_everywhere()
        self.percentage_winning_figure_river = self.statistiques_win_figures.calculate_percentage_win_all_figure_in_river()
        self.percentage_winning_figure_everywhere = self.statistiques_win_figures.calculate_percentage_win_all_figure_everywhere()
        return StatistiquesResult(self.percentage_presence_figure_river, self.percentage_presence_figure_everywhere, self.percentage_winner_players_river, self.percentage_winner_players_everywhere, self.percentage_winning_figure_river, self.percentage_winning_figure_everywhere)