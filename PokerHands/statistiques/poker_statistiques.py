from PokerHands.statistiques.statistiques_result import StatistiquesResult

class PokerStatistiques : 
    def __init__(self, statistiques_presences_figures , statistiques_winners_players, statistiques_win_figures):
        self.statistiques_presences_figures = statistiques_presences_figures
        self.statistiques_winners_players = statistiques_winners_players
        self.statistiques_win_figures = statistiques_win_figures
        self.percentage_presence_figure_showdown = {}
        self.percentage_winner_players_showdown = {}
        self.percentage_winning_figure_showdown = {}    
        self.total_figure = 0

    def calculate_all_statistiques(self):      
        self.percentage_presence_figure_showdown = self.statistiques_presences_figures.calculate_percentage_presence_all_figures_in_showdown()
        self.percentage_winner_players_showdown = self.statistiques_winners_players.calculate_percentage_players_win_in_showdown()
        self.percentage_winning_figure_showdown = self.statistiques_win_figures.calculate_percentage_win_all_figure_in_showdown()
        return StatistiquesResult(self.percentage_presence_figure_showdown, self.percentage_winner_players_showdown, self.percentage_winning_figure_showdown)