from PokerHands.multiple_game import MultipleGame
from PokerHands.hand.hand import PhasePoker

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
     .define_how_many_game_will_be_launching(100)
     .launch_multiple_game()
     .confirm_all_games_are_launch()
     .confirm_all_games_are_analyzed())


class MultipleGameDriver(): 
    def __init__(self):
        self.multiple_game = MultipleGame()
        self.game_results = []
        self.number = 0

    def add_player(self, player_name): 
        self.multiple_game.add_player(player_name)
        return self

    def define_how_many_game_will_be_launching(self, number):
        self.number = number
        self.multiple_game.define_how_many_game_will_be_launching(number)
        return self

    def launch_multiple_game(self): 
        self.game_results = self.multiple_game.launch_multiple_game()
        return self

    def confirm_all_games_are_launch(self): 
        assert(len(self.game_results) == self.number)
        return self

    def confirm_all_games_are_analyzed(self): 
        for game_result in self.game_results : 
            assert((len(game_result.winners)> 0) == True)
            assert((len(game_result.poker_hands_by_player)> 0) == True)
            assert((game_result.best_figure != "None") == True)
        return self