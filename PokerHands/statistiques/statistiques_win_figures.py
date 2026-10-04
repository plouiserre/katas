from PokerHands.game.game import PhasePoker

class StatistiquesWinFigures: 
    def __init__(self, games_results):
        self.games_results = games_results

    def calculate_percentage_win_all_figure_in_river(self):
        percentage_winning_figure_river = {}
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
            percentage_winning_figure_river[type_figure] = figure_winning_river[type_figure]/total_game
        return percentage_winning_figure_river

    def calculate_percentage_win_all_figure_everywhere(self):
        percentage_winning_figure_everywhere = {}
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
            percentage_winning_figure_everywhere[type_figure] = figure_winning_everywhere[type_figure]/total_game
        return percentage_winning_figure_everywhere