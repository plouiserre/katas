class RoundResult : 
    def __init__(self, winners, best_figure, combination_by_player):
        self.winners = winners
        self.best_figure = best_figure
        self.combination_by_player = combination_by_player

    @staticmethod
    def create_player_result(comparaison_result, combination_by_player) :
        return RoundResult(comparaison_result.winners, comparaison_result.best_figure, combination_by_player)