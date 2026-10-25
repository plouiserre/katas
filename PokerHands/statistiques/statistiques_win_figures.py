from PokerHands.hand.hand import PhasePoker

class StatistiquesWinFigures: 
    def __init__(self, games_results):
        self.games_results = games_results
        self.figure_winning_every_where = {}
        self.figure_winning_showdown_phase = {}
        
    def calculate_percentage_win_all_figure_in_showdown(self):
        percentage_winning_figure_showdown = {}
        self.total_game = 0
        for game_result in self.games_results : 
            self.__count_figure_winner_during_showdown_phase(game_result)
        for type_figure in self.figure_winning_showdown_phase : 
            percentage_winning_figure_showdown[type_figure] = self.figure_winning_showdown_phase[type_figure]/self.total_game
        return percentage_winning_figure_showdown

    def __count_figure_winner_during_showdown_phase(self, game):
        self.__count_this_players_figure(game, self.figure_winning_showdown_phase)

    def __count_this_players_figure(self, poker_hand_player, all_figures):
        self.total_game += 1
        figure_winner = poker_hand_player.best_figure
        type_figure = type(figure_winner).__name__
        if (type_figure in all_figures) == False : 
            all_figures[type_figure] = 0
        all_figures[type_figure] += 1