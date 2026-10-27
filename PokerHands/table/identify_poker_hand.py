class IdentifyPokerHand : 
    def __init__(self, combination, players):
        self.combination = combination
        self.players = players
        self.combination_by_player = {} 

    def determinate_poker_hands(self):
        for player_name in self.players : 
            player = self.players[player_name]
            combination = self.combination.determinate_high_figure(player) 
            self.combination_by_player[player_name] = combination
        return self.combination_by_player