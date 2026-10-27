from PokerHands.table.comparaison_result import ComparaisonResult
from PokerHands.round.round_result import RoundResult
from PokerHands.tests.dsl.dsl_figure import get_figure
from PokerHands.tests.dsl.dsl_player import get_player

def convert_hand_result_crypted(round_result_crypted, players): 
        all_crypted_results = round_result_crypted.split("_")
        best_poker_hand = __get_best_poker_hand(all_crypted_results[0])
        poker_hands = __get_all_poker_hands(all_crypted_results[1], players)
        winners = [__get_winners(all_crypted_results[2], players)]
        comparaison_result = ComparaisonResult.Create(winners, best_poker_hand)
        player_result = RoundResult.create_player_result(comparaison_result, poker_hands)
        return player_result

def __get_best_poker_hand(best_combination_str):
    two_first_letters = best_combination_str[0:2]
    figure = get_figure(two_first_letters, best_combination_str[2:len(best_combination_str)])
    return figure

def __get_all_poker_hands(poker_hands_crypted, players):
    all_poker_hands_crypted = poker_hands_crypted.split("-")
    poker_hands = {}
    for combination_crypted in all_poker_hands_crypted : 
        combination_part = combination_crypted.split(":")
        player_name = get_player(players, combination_part[0])
        figure = get_figure(combination_part[1][0:2], combination_part[1][2:len(combination_part[1])])
        poker_hands[player_name] = figure
    return poker_hands

def __get_winners(winners_letter, players): 
    player_first_letter = winners_letter.split(":")[1]
    player_name = get_player(players, player_first_letter)
    return player_name