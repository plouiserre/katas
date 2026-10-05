from PokerHands.game.game import PhasePoker

class StatistiquesPresenceFigures: 
    def __init__(self, games_results):
        self.games_results = games_results
    
    def calculate_percentage_presence_all_figures_in_river(self):
        self.figures_present = {}
        percentage_presence_figure_river = {}        
        self.total_figure = 0
        self.__count_all_figures_in_each_river_phase()
        for type_figure in self.figures_present : 
            percentage_presence_figure_river[type_figure] = self.figures_present[type_figure]/self.total_figure                    
        return percentage_presence_figure_river

    def __count_all_figures_in_each_river_phase(self):
        for game_result in self.games_results : 
            for phase in game_result : 
                if phase == PhasePoker.RIVER: 
                    game = game_result[phase]
                    self.__count_all_figures_presences(game)

    def calculate_percenge_presence_all_figures_everywhere(self):
        self.figures_present = {}
        percentage_presence_figure_everywhere = {}
        self.total_figure = 0
        self.__count_all_figures_in_each_phase()
        for type_figure in self.figures_present : 
            percentage_presence_figure_everywhere[type_figure] = self.figures_present[type_figure]/self.total_figure
        return percentage_presence_figure_everywhere

    def __count_all_figures_in_each_phase(self):
        for game_result in self.games_results : 
            for phase in game_result :                 
                game = game_result[phase]
                self.__count_all_figures_presences(game)

    def __count_all_figures_presences(self, game):
        for player_name in game.hands_by_player : 
            self.total_figure += 1
            figure = game.hands_by_player[player_name]
            type_figure = type(figure).__name__
            if (type_figure in self.figures_present) == False : 
                self.figures_present[type_figure] = 0
            self.figures_present[type_figure] += 1