from PokerHands.game.game import PhasePoker

class StatistiquesPresenceFigures: 
    def __init__(self, games_results):
        self.games_results = games_results

    #1 - calculer le % de chaque figure dans la river 
    def calculate_percentage_presence_all_figures_in_river(self):
        percentage_presence_figure_river = {}
        figures_present_in_river = {}
        self.total_figure = 0
        for game_result in self.games_results : 
            for phase in game_result : 
                if phase == PhasePoker.RIVER: 
                    game = game_result[phase]
                    for player_name in game.hands_by_player : 
                        self.total_figure += 1
                        figure = game.hands_by_player[player_name]
                        type_figure = type(figure).__name__
                        if (type_figure in figures_present_in_river) == False : 
                            figures_present_in_river[type_figure] = 0
                        figures_present_in_river[type_figure] += 1
        for type_figure in figures_present_in_river : 
            percentage_presence_figure_river[type_figure] = figures_present_in_river[type_figure]/self.total_figure                    
        return percentage_presence_figure_river

    #2 - calculer le % de chaque figure dans chaque phase
    def calculate_percenge_presence_all_figures_everywhere(self):
        percentage_presence_figure_everywhere = {}
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
            percentage_presence_figure_everywhere[type_figure] = figures_present[type_figure]/total_figure
        return percentage_presence_figure_everywhere