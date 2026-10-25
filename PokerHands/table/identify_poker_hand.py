class IdentifyPokerHand : 
    def __init__(self, poker_hand, players):
        self.poker_hand = poker_hand
        self.players = players
        self.poker_hands_by_player = {} 

    def determinate_poker_hands(self):
        for player_name in self.players : 
            player = self.players[player_name]
            poker_hand = self.poker_hand.determinate_high_figure(player) 
            self.poker_hands_by_player[player_name] = poker_hand
        return self.poker_hands_by_player