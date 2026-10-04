from PokerHands.game.game import PhasePoker
from PokerHands.player.comparaison_result import ComparaisonResult
from PokerHands.player.player_result import PlayerResult
from PokerHands.tests.dsl.dsl_common import get_figure, get_player

def convert_game_result_crypted(game_result_crypted, players): 
        phases_crypted = game_result_crypted.split("|")
        phases = {}
        for phase_crypted in phases_crypted : 
            part_phases = phase_crypted.split("_")
            phase_name = __get_phase_part(part_phases[0])
            best_hand = __get_best_hand(part_phases[1])
            hands = __get_all_hands(part_phases[2], players)
            winners = [__get_winners(part_phases[3], players)]
            comparaison_result = ComparaisonResult.Create(winners, best_hand)
            player_result = PlayerResult.create_player_result(comparaison_result, hands)
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

def __get_best_hand(best_hand_str):
    two_first_letters = best_hand_str[0:2]
    figure = get_figure(two_first_letters, best_hand_str[2:len(best_hand_str)])
    return figure

def __get_all_hands(hands_crypted, players):
    all_hands_crypted = hands_crypted.split("-")
    hands = {}
    for hand_crypted in all_hands_crypted : 
        hand_part = hand_crypted.split(":")
        player_name = get_player(players, hand_part[0])
        figure = get_figure(hand_part[1][0:2], hand_part[1][2:len(hand_part[1])])
        hands[player_name] = figure
    return hands

def __get_winners(winners_letter, players): 
    player_first_letter = winners_letter.split(":")[1]
    player_name = get_player(players, player_first_letter)
    return player_name