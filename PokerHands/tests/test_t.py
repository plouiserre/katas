from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import CardColor, CardValue
from PokerHands.game.game import PhasePoker
from PokerHands.player.comparaison_result import ComparaisonResult
from PokerHands.player.player_result import PlayerResult

def test_1():
    (Driver()
     .add_players(["Jean-Jacques Goldman", "Mylène Farmer", "Omar Sy", "Sophie Marceau"])
     .add_game_result("DRAW_PAA_J:HIK-M:HIQ-O:PAA-S:HI7_W:O|FLOP_PAA5_J:HIK-M:HIQ-O:PAA5-S:HI7_W:O|TURN_PAAK_J:PAKQ-M:HIK-O:PAAK-S:HIK_W:O|RIVER_PAAK_J:PAKQ-M:HIK-O:PAAK-S:HIK_W:O")
     .add_game_result("DRAW_PAA_J:HIA-M:HIQ-O:PAA-S:HI7_W:O|FLOP_PAAK_J:PAKA-M:PAQK-O:PAAK-S:HIK_W:O|TURN_TKQK_J:PAKA-M:TKQK-O:PAAK-S:HIK_W:M|RIVER_TKQK_J:PAKA-M:TKQK-O:PAAK-S:HIK_W:M")
     .add_game_result("DRAW_HIA_J:HIA-M:HIQ-O:HIA-S:HI7_W:O|FLOP_PAKA_J:PAKA-M:PAQK-O:HIA-S:HIK_W:J|TURN_PAKA_J:PAKA-M:PAQK-O:HIA-S:HIK_W:J|RIVER_PAKA_J:PAKA-M:PAQK-O:HIA-S:HIK_W:J")     
     .add_game_result("DRAW_PAA_J:HIA-M:HIQ-O:PAA-S:HI7_W:O|FLOP_TKA6_J:PAAK-M:HIA-O:TKA6-S:HIA_W:O|TURN_TKA6_J:PAAK-M:PAQA-O:TKA6-S:HIA_W:O|RIVER_QF7S_J:PAKA-M:TKQK-O:PAAK-S:QF7S_W:S")     
     .add_game_result("DRAW_PAA_J:HIA-M:HIQ-O:PAA-S:HI7_W:O|FLOP_PAAK_J:PAKA-M:HIA-O:PAAK-S:HIA_W:O|TURN_TKAK_J:2PAK6-M:HIA-O:TKAK-S:HIA_W:O|RIVER_FUKA_J:FUAK-M:PAKA-O:FUKA-S:PAKA_W:O"))
    assert(1 == 2)


class Driver : 
    def __init__(self):
        self.players = []
        self.games_results = []        

    def add_players(self, players_name): 
        for player_name in players_name : 
            self.players.append(player_name)
        return self 
    
    def add_game_result(self, game_result_crypted):
        game_result = self.__convert_game_result_crypted(game_result_crypted)
        self.games_results.append(game_result)
        return self

    def calculate_percentage(self):
        return self

    def confirm_percentage(self):
        return self

    def __convert_game_result_crypted(self, game_result_crypted): 
        phases_crypted = game_result_crypted.split("|")
        phases = {}
        for phase_crypted in phases_crypted : 
            part_phases = phase_crypted.split("_")
            phase_name = self.__get_phase_part(part_phases[0])
            best_hand = self.__get_best_hand(part_phases[1])
            hands = self.__get_all_hands(part_phases[2])
            winners = [self.__get_winners(part_phases[3])]
            comparaison_result = ComparaisonResult.Create(winners, best_hand)
            player_result = PlayerResult.create_player_result(comparaison_result, hands)
            phases[phase_name] = player_result
        return phases

    def __get_phase_part(self, phase_name_str) : 
        if phase_name_str == "DRAW": 
            return PhasePoker.DRAW
        elif phase_name_str == "FLOP": 
            return PhasePoker.FLOP
        elif phase_name_str == "TURN":
            return PhasePoker.TURN
        elif phase_name_str == "RIVER":
            return PhasePoker.RIVER

    def __get_best_hand(self, best_hand_str):
        two_first_letters = best_hand_str[0:2]
        figure = self.__get_figure(two_first_letters, best_hand_str[2:len(best_hand_str)])
        return figure

    def __get_all_hands(self, hands_crypted):
        all_hands_crypted = hands_crypted.split("-")
        hands = {}
        for hand_crypted in all_hands_crypted : 
            hand_part = hand_crypted.split(":")
            player_name = self.__get_player(hand_part[0])
            figure = self.__get_figure(hand_part[1][0:2], hand_part[1][2:len(hand_part[1])])
            hands[player_name] = figure
        return hands

    def __get_winners(self, winners_letter): 
        player_first_letter = winners_letter.split(":")[1]
        player_name = self.__get_player(player_first_letter)
        return player_name

    def __get_player(self, first_letter): 
        player_name = ""
        for player in self.players : 
            first_letter_player = player[0:1]
            if first_letter == first_letter_player : 
                player_name = player
                break
        return player_name

    def __get_figure(self, initial_figure, other_letters): 
        if initial_figure == "PA":
            return self.__get_pair_figure(other_letters)
        elif initial_figure == "HI":
            return self.__get_high_figure(other_letters)
        elif initial_figure == "TK": 
            return self.__get_three_kind_figure(other_letters)
        elif initial_figure =="QF":
            return self.__get_quinte_flush_figure(other_letters)
        elif initial_figure == "2P":
            return self.__get_two_pair_figure(other_letters)
        elif initial_figure == "FU": 
            return self.__get_full_figure(other_letters)

    def __get_pair_figure(self, pair_letters):
        high_card_pair = CardValue.UNDEFINED
        pair_figure = None
        if len(pair_letters) == 1:
            pair_value = self.__get_card(pair_letters)
            pair_figure = PairFigure(pair_value, high_card_pair)
        else : 
            pair_value = self.__get_card(pair_letters[0:1])
            high_card_pair = self.__get_card(pair_letters[1:2])
            pair_figure = PairFigure(pair_value, high_card_pair)
        return pair_figure

    def __get_high_figure(self, high_card_letters): 
        high_card_value = self.__get_card(high_card_letters)
        return HighCardFigure(high_card_value)

    def __get_three_kind_figure(self, three_of_kind_letters): 
        three_of_kind_value = self.__get_card(three_of_kind_letters[0:1])
        high_card_value = self.__get_card(three_of_kind_letters[1:2])
        return ThreeOfKindFigure(three_of_kind_value, high_card_value)

    def __get_two_pair_figure(self, two_pair_letters): 
        first_pair_value = self.__get_card(two_pair_letters[0:1])
        second_pair_value = self.__get_card(two_pair_letters[1:2])
        high_card_value = self.__get_card(two_pair_letters[2:3])
        return TwoPairFigure(first_pair_value, second_pair_value, high_card_value)

    def __get_quinte_flush_figure(self, quinte_flush_letters): 
        quinte_flush_value = self.__get_card(quinte_flush_letters[0:1])
        quinte_flush_color = self.__get_color(quinte_flush_letters[1:2])
        return QuinteFlushFigure(quinte_flush_value, quinte_flush_color)

    def __get_full_figure(self, full_figure_letters): 
        two_times_cards = self.__get_card(full_figure_letters[0:1])
        three_times_cards = self.__get_card(full_figure_letters[1:2])
        return FullFigure(two_times_cards, three_times_cards)

    def __get_card(self, card_letters): 
        if card_letters == "A":
            return CardValue.ACE
        elif card_letters == "K":
            return CardValue.KING
        elif card_letters == "Q":
            return CardValue.QUEEN
        elif card_letters == "7":
            return CardValue.SEVEN
        elif card_letters == "6":
            return CardValue.SIX
        elif card_letters == "5":
            return CardValue.FIVE
        else : 
            return CardValue.UNDEFINED

    def __get_color(self, color_letters): 
        if color_letters == "S":
            return CardColor.SPADES