from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.card import CardValue
from PokerHands.player.compare_hand import CompareHand

def test_1():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", HighCardFigure(CardValue.JACK))
        .add_hand("Natacha", HighCardFigure(CardValue.QUEEN))
        .determinate_winners()
        .check_winner_name("Natacha"))


class Driver(): 
    def __init__(self):
        self.players = []
        self.hand_players = {}
        self.result = None
        self.winner = ""

    def add_player(self, name_player): 
        self.players.append(name_player)
        return self

    def add_hand(self, name_player, hand): 
        self.hand_players[name_player] = hand
        return self

    def determinate_winners(self):
        compare_hand = CompareHand(self.players, self.hand_players) 
        self.result = compare_hand.get_players_with_best_hands()
        return self

    def check_winner_name(self, winner_name): 
        assert(self.winner == winner_name)