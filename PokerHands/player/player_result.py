class PlayerResult : 
    def __init__(self, winners, best_figure, hands_by_player):
        self.winners = winners
        self.best_figure = best_figure
        self.hands_by_player = hands_by_player

    @staticmethod
    def create_player_result(self, comparaison_result, hands_by_player) :
        return PlayerResult(comparaison_result.winners, comparaison_result.best_figure, hands_by_player)