from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.round.round import Round

class MultipleGame : 
    def __init__(self):
        self.players = []
        self.number = 0
        self.round_results = []

    def add_player(self, player_name): 
        self.players.append(player_name)
        return self

    def define_how_many_hand_will_be_launching(self, number):
        self.number = number
        return self

    def launch_multiple_round(self): 
        for _ in range(self.number):
            multi_draw_cards = MultiDrawCards()
            round = Round(multi_draw_cards)
            round.add_players(self.players)
            round_result = round.launch_hand()
            self.round_results.append(round_result)
        return self.round_results