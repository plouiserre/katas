class IdentifyHand : 
    def __init__(self, hand, players):
        self.hand = hand
        self.players = players
        self.hands_by_player = {} 

    def determinate_hands(self):
        for player_name in self.players : 
            player = self.players[player_name]
            hand = self.hand.determinate_high_figure(player) 
            self.hands_by_player[player_name] = hand
        return self.hands_by_player