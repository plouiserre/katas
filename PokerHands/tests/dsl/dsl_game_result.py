from PokerHands.game.game import PhasePoker
from PokerHands.hand.comparaison_result import ComparaisonResult
from PokerHands.hand.hand_result import HandResult
from PokerHands.tests.dsl.dsl_figure import get_figure
from PokerHands.tests.dsl.dsl_player import get_player

def convert_game_result_crypted(game_result_crypted, players): 
        phases_crypted = game_result_crypted.split("|")
        phases = {}
        for phase_crypted in phases_crypted : 
            part_phases = phase_crypted.split("_")
            phase_name = __get_phase_part(part_phases[0])
            best_poker_hand = __get_best_poker_hand(part_phases[1])
            poker_hands = __get_all_poker_hands(part_phases[2], players)
            winners = [__get_winners(part_phases[3], players)]
            comparaison_result = ComparaisonResult.Create(winners, best_poker_hand)
            player_result = HandResult.create_player_result(comparaison_result, poker_hands)
            phases[phase_name] = player_result
        return phases

def __get_phase_part(phase_name_str) : 
        if phase_name_str == "DRAW": 
            return PhasePoker.DRAW
        elif phase_name_str == "FLOP": 
            return PhasePoker.FLOP
        elif phase_name_str == "TURN":
            return PhasePoker.TURN
        elif phase_name_str == "RIVER":
            return PhasePoker.RIVER

def __get_best_poker_hand(best_poker_hand_str):
    two_first_letters = best_poker_hand_str[0:2]
    figure = get_figure(two_first_letters, best_poker_hand_str[2:len(best_poker_hand_str)])
    return figure

def __get_all_poker_hands(poker_hands_crypted, players):
    all_poker_hands_crypted = poker_hands_crypted.split("-")
    poker_hands = {}
    for poker_hand_crypted in all_poker_hands_crypted : 
        poker_hand_part = poker_hand_crypted.split(":")
        player_name = get_player(players, poker_hand_part[0])
        figure = get_figure(poker_hand_part[1][0:2], poker_hand_part[1][2:len(poker_hand_part[1])])
        poker_hands[player_name] = figure
    return poker_hands

def __get_winners(winners_letter, players): 
    player_first_letter = winners_letter.split(":")[1]
    player_name = get_player(players, player_first_letter)
    return player_name