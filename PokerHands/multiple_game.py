from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.game.game import Game

class MultipleGame : 
    def __init__(self):
        self.players = []
        self.number = 0
        self.game_results = []

    def add_player(self, player_name): 
        self.players.append(player_name)
        return self

    def define_how_many_game_will_be_launching(self, number):
        self.number = number
        return self

    def launch_multiple_game(self): 
        for _ in range(self.number):
            multi_draw_cards = MultiDrawCards()
            game = Game(multi_draw_cards)
            game.add_players(self.players)
            game_result = game.launch_game()
            self.game_results.append(game_result)
        return self.game_results