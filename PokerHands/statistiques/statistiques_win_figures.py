from PokerHands.game.game import PhasePoker

class StatistiquesWinFigures: 
    def __init__(self, games_results):
        self.games_results = games_results
        self.figure_winning_every_where = {}
        self.figure_winning_river_phase = {}
        
    def calculate_percentage_win_all_figure_in_river(self):
        percentage_winning_figure_river = {}
        self.total_game = 0
        for game_result in self.games_results : 
            self.__count_winner_during_game_river_phase(game_result)
        for type_figure in self.figure_winning_river_phase : 
            percentage_winning_figure_river[type_figure] = self.figure_winning_river_phase[type_figure]/self.total_game
        return percentage_winning_figure_river

    def __count_winner_during_game_river_phase(self, game):
        for phase in game : 
            if phase == PhasePoker.RIVER : 
                self.__count_this_players_figure(game[phase], self.figure_winning_river_phase)

    def calculate_percentage_win_all_figure_everywhere(self):
        self.total_game = 0
        percentage_winning_figure_everywhere = {}
        for game_result in self.games_results :             
            self.__count_winner_during_game_every_phase(game_result)
        for type_figure in self.figure_winning_every_where : 
            percentage_winning_figure_everywhere[type_figure] = self.figure_winning_every_where[type_figure]/self.total_game
        return percentage_winning_figure_everywhere

    def __count_winner_during_game_every_phase(self, game):
        for phase in game : 
            self.__count_this_players_figure(game[phase], self.figure_winning_every_where)

    def __count_this_players_figure(self, hand_player, all_figures):
        self.total_game += 1
        figure_winner = hand_player.best_figure
        type_figure = type(figure_winner).__name__
        if (type_figure in all_figures) == False : 
            all_figures[type_figure] = 0
        all_figures[type_figure] += 1