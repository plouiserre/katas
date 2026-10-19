class PlayerResult : 
    def __init__(self, winners, best_figure, poker_hands_by_player):
        self.winners = winners
        self.best_figure = best_figure
        self.poker_hands_by_player = poker_hands_by_player

    @staticmethod
    def create_player_result(comparaison_result, poker_hands_by_player) :
        return PlayerResult(comparaison_result.winners, comparaison_result.best_figure, poker_hands_by_player)