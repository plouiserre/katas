class StatistiquesPresenceFigures: 
    def __init__(self, games_results):
        self.games_results = games_results
    
    def calculate_percentage_presence_all_figures_in_showdown(self):
        self.figures_present = {}
        percentage_presence_figure_showdown = {}        
        self.total_figure = 0
        self.__count_all_figures_in_each_showdown_phase()
        for type_figure in self.figures_present : 
            percentage_presence_figure_showdown[type_figure] = self.figures_present[type_figure]/self.total_figure                    
        return percentage_presence_figure_showdown

    def __count_all_figures_in_each_showdown_phase(self):
        for game in self.games_results : 
            self.__count_all_figures_presences(game)

    def __count_all_figures_presences(self, game):
        for player_name in game.combination_by_player : 
            self.total_figure += 1
            figure = game.combination_by_player[player_name]
            type_figure = type(figure).__name__
            if (type_figure in self.figures_present) == False : 
                self.figures_present[type_figure] = 0
            self.figures_present[type_figure] += 1