from PokerHands.player import Player
from PokerHands.winner import Winner

def test_1(): 
    player_one = Player()
    player_two = Player()

    assert(launched_poker_game(player_one, player_two) == Winner.FIRST_HAND
           or launched_poker_game(player_one, player_two) == Winner.SECOND_HAND
           or launched_poker_game(player_one, player_two) == Winner.EQUALITY)


def launched_poker_game(player_one : Player, player_two : Player):
    high_figure_first_hand = player_one.calculate_hand()
    high_figure_second_hand = player_two.calculate_hand()
    return None