from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.game.party import Party, PhasePoker

class MultipleGame : 
    def __init__(self):
        self.players = []
        self.number = 0
        self.party_results = []

    def add_player(self, player_name): 
        self.players.append(player_name)
        return self

    def define_how_many_game_will_be_launching(self, number):
        self.number = number
        return self

    def launch_multiple_game(self): 
        for _ in range(self.number):
            multi_draw_cards = MultiDrawCards()
            party = Party(multi_draw_cards)
            party.add_players(self.players)
            party_result = party.launch_party()
            self.party_results.append(party_result)
        return self.party_results