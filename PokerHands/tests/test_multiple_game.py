from PokerHands.multiple_game import MultipleGame
def test_launch_100_games(): 
    (MultipleGameDriver()
     .add_player("Steve")
     .add_player("Natacha")
     .add_player("Tony")
     .add_player("Thor")
     .add_player("Bruce")
     .add_player("Clint")
     .add_player("Carol")
     .add_player("T'Challa")
     .add_player("Steven")
     .add_player("Wanda")
     .define_how_many_hand_will_be_launching(100)
     .launch_multiple_round()
     .confirm_all_games_are_launch()
     .confirm_all_games_are_analyzed())


class MultipleGameDriver(): 
    def __init__(self):
        self.multiple_game = MultipleGame()
        self.round_results = []
        self.number = 0

    def add_player(self, player_name): 
        self.multiple_game.add_player(player_name)
        return self

    def define_how_many_hand_will_be_launching(self, number):
        self.number = number
        self.multiple_game.define_how_many_hand_will_be_launching(number)
        return self

    def launch_multiple_round(self): 
        self.round_results = self.multiple_game.launch_multiple_round()
        return self

    def confirm_all_games_are_launch(self): 
        assert(len(self.round_results) == self.number)
        return self

    def confirm_all_games_are_analyzed(self): 
        for hand_result in self.round_results : 
            assert((len(hand_result.winners)> 0) == True)
            assert((len(hand_result.poker_hands_by_player)> 0) == True)
            assert((hand_result.best_figure != "None") == True)
        return self