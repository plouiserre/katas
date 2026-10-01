from PokerHands.multiple_game import MultipleGame
from PokerHands.game.party import Party, PhasePoker

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
     .confirm_all_games_are_complete())


class MultipleGameDriver(): 
    def __init__(self):
        self.multiple_game = MultipleGame()
        self.party_results = []
        self.number = 0

    def add_player(self, player_name): 
        self.multiple_game.add_player(player_name)
        return self

    def define_how_many_game_will_be_launching(self, number):
        self.number = number
        self.multiple_game.define_how_many_game_will_be_launching(number)
        return self

    def launch_multiple_game(self): 
        self.party_results = self.multiple_game.launch_multiple_game()
        return self

    def confirm_all_games_are_launch(self): 
        assert(len(self.party_results) == self.number)
        return self

    def confirm_all_games_are_complete(self): 
        for party_result in self.party_results : 
            assert((PhasePoker.DRAW in party_result) == True)
            assert((PhasePoker.FLOP in party_result) == True)
            assert((PhasePoker.TURN in party_result) == True)
            assert((PhasePoker.RIVER in party_result) == True)
        return self