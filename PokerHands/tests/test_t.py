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
from PokerHands.tests.dsl.dsl_game_result import convert_game_result_crypted

def test_1():
    (Driver()
     .add_players(["Jean-Jacques Goldman", "Mylène Farmer", "Omar Sy", "Sophie Marceau"])
     .add_game_result("DRAW_PAA_J:HIK-M:HIQ-O:PAA-S:HI7_W:O|FLOP_PAA5_J:HIK-M:HIQ-O:PAA5-S:HI7_W:O|TURN_PAAK_J:PAKQ-M:HIK-O:PAAK-S:HIK_W:O|RIVER_PAAK_J:PAKQ-M:HIK-O:PAAK-S:HIK_W:O")
     .add_game_result("DRAW_PAA_J:HIA-M:HIQ-O:PAA-S:HI7_W:O|FLOP_PAAK_J:PAKA-M:PAQK-O:PAAK-S:HIK_W:O|TURN_TKQK_J:PAKA-M:TKQK-O:PAAK-S:HIK_W:M|RIVER_TKQK_J:PAKA-M:TKQK-O:PAAK-S:HIK_W:M")
     .add_game_result("DRAW_HIA_J:HIA-M:HIQ-O:HIA-S:HI7_W:O|FLOP_PAKA_J:PAKA-M:PAQK-O:HIA-S:HIK_W:J|TURN_PAKA_J:PAKA-M:PAQK-O:HIA-S:HIK_W:J|RIVER_PAKA_J:PAKA-M:PAQK-O:HIA-S:HIK_W:J")     
     .add_game_result("DRAW_PAA_J:HIA-M:HIQ-O:PAA-S:HI7_W:O|FLOP_TKA6_J:PAAK-M:HIA-O:TKA6-S:HIA_W:O|TURN_TKA6_J:PAAK-M:PAQA-O:TKA6-S:HIA_W:O|RIVER_QF7S_J:PAKA-M:TKQK-O:PAAK-S:QF7S_W:S")     
     .add_game_result("DRAW_PAA_J:HIA-M:HIQ-O:PAA-S:HI7_W:O|FLOP_PAAK_J:PAKA-M:HIA-O:PAAK-S:HIA_W:O|TURN_TKAK_J:2PAK6-M:HIA-O:TKAK-S:HIA_W:O|RIVER_FUKA_J:FUAK-M:PAKA-O:FUKA-S:PAKA_W:O")
     .calculate_percentages()
     .validate_percentage("PRR|PA:0.5_HI:0.25_TK:0.1_QF:0.05_FU:0.1")
     .validate_percentage("PRE|PA:0.3875_HI:0.4875_TK:0.075_QF:0.0125_FU:0.025_2P:0.0125")
     .validate_percentage("WNR|J:0.2_M:0.2_O:0.4_S:0.2")
     .validate_percentage("WNE|J:0.15_M:0.1_O:0.7_S:0.05")
     .validate_percentage("WFR|PA:0.4_TK:0.2_QF:0.2_FU:0.2")
     .validate_percentage("WFE|PA:0.6_TK:0.25_QF:0.05_FU:0.05_HI:0.05"))

class Driver : 
    def __init__(self):
        self.players = []
        self.games_results = []
        self.percentage_presence_figure_river = {}
        self.percentage_presence_figure_everywhere = {}
        self.percentage_winner_players_river = {}
        self.percentage_winner_players_everywhere = {}
        self.percentage_winning_figure_river = {}    
        self.percentage_winning_figure_everywhere = {}

    def add_players(self, players_name): 
        for player_name in players_name : 
            self.players.append(player_name)
        return self 
    
    def add_game_result(self, game_result_crypted):
        game_result = convert_game_result_crypted(game_result_crypted, self.players)
        self.games_results.append(game_result)
        return self

    def calculate_percentages(self):
        self.__calculate_percentage_presence_all_figures_in_river()
        self.__calculate_percenge_presence_all_figures_everywhere()
        self.__calculate_percentage_players_win_in_river()
        self.__calculate_percentage_players_win_everywhere()
        self.__calculate_percentage_win_all_figure_in_river()
        self.__calculate_percentage_win_all_figure_everywhere()
        return self

    #1 - calculer le % de chaque figure dans la river 
    def __calculate_percentage_presence_all_figures_in_river(self):
        figures_present_in_river = {}
        total_figure = 0
        for game_result in self.games_results : 
            for phase in game_result : 
                if phase == PhasePoker.RIVER: 
                    game = game_result[phase]
                    for player_name in game.hands_by_player : 
                        total_figure += 1
                        figure = game.hands_by_player[player_name]
                        type_figure = type(figure).__name__
                        if (type_figure in figures_present_in_river) == False : 
                            figures_present_in_river[type_figure] = 0
                        figures_present_in_river[type_figure] += 1
        for type_figure in figures_present_in_river : 
                    self.percentage_presence_figure_river[type_figure] = figures_present_in_river[type_figure]/total_figure

    #2 - calculer le % de chaque figure dans chaque phase
    def __calculate_percenge_presence_all_figures_everywhere(self):
        figures_present = {}
        total_figure = 0
        for game_result in self.games_results : 
            for phase in game_result :                 
                game = game_result[phase]
                for player_name in game.hands_by_player : 
                    total_figure += 1
                    figure = game.hands_by_player[player_name]
                    type_figure = type(figure).__name__
                    if (type_figure in figures_present) == False : 
                        figures_present[type_figure] = 0
                    figures_present[type_figure] += 1
        for type_figure in figures_present : 
            self.percentage_presence_figure_everywhere[type_figure] = figures_present[type_figure]/total_figure

    #3 - calculer le % de win pour chaque joueur dans la river 
    def __calculate_percentage_players_win_in_river(self): 
        winners_each_river = {}
        total_game = 0
        for game_result in self.games_results : 
            for phase in game_result : 
                if phase == PhasePoker.RIVER :
                    total_game += 1
                    for winner in game_result[phase].winners :
                        if (winner in winners_each_river) == False : 
                            winners_each_river[winner] = 0
                        winners_each_river[winner] += 1
        for winner in winners_each_river :
            self.percentage_winner_players_river[winner] = winners_each_river[winner]/total_game

    #4 - calculer le % de win pour chaque joueur en tout
    def __calculate_percentage_players_win_everywhere(self):
        winners_each_river = {}
        total_game = 0
        for game_result in self.games_results : 
            for phase in game_result : 
                total_game += 1
                for winner in game_result[phase].winners :
                    if (winner in winners_each_river) == False : 
                        winners_each_river[winner] = 0
                    winners_each_river[winner] += 1
        for winner in winners_each_river :
            self.percentage_winner_players_everywhere[winner] = winners_each_river[winner]/total_game 

    #5 - calculer le % de win de chaque figure dans la river 
    def __calculate_percentage_win_all_figure_in_river(self):
        figure_winning_river = {}
        total_game = 0
        for game_result in self.games_results : 
            total_game += 1
            for phase in game_result : 
                if phase == PhasePoker.RIVER : 
                    figure_winner = game_result[phase].best_figure
                    type_figure = type(figure_winner).__name__
                    if (type_figure in figure_winning_river) == False : 
                        figure_winning_river[type_figure] = 0
                    figure_winning_river[type_figure] += 1
        for type_figure in figure_winning_river : 
            self.percentage_winning_figure_river[type_figure] = figure_winning_river[type_figure]/total_game

    #6 - calculer le % de win de chaque figure dans chaque phase
    def __calculate_percentage_win_all_figure_everywhere(self):
            figure_winning_everywhere = {}
            total_game = 0
            for game_result in self.games_results : 
                for phase in game_result : 
                    total_game += 1
                    figure_winner = game_result[phase].best_figure
                    type_figure = type(figure_winner).__name__
                    if (type_figure in figure_winning_everywhere) == False : 
                        figure_winning_everywhere[type_figure] = 0
                    figure_winning_everywhere[type_figure] += 1
            for type_figure in figure_winning_everywhere : 
                self.percentage_winning_figure_everywhere[type_figure] = figure_winning_everywhere[type_figure]/total_game            

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

    def validate_percentage(self, datas_crypted):
        all_datas = datas_crypted.split("|")
        if all_datas[0] == "PRR":
            self.__validate_percentage_figure_present_river(all_datas[1])
        elif all_datas[0] == "PRE": 
            self.__validate_percentage_figure_present_everywhere(all_datas[1])
        elif all_datas[0] == "WNR":
            self.__validate_percentage_winner_player_river(all_datas[1])
        elif all_datas[0] == "WNE":
            self.__validate_percentage_winner_player_everywhere(all_datas[1])
        elif all_datas[0] == "WFR":
            self.__validate_percentage_figure_winner_river(all_datas[1])
        elif all_datas[0] == "WFE":
            self.__validate_percentage_figure_winner_everywhere(all_datas[1])
        return self

    def __validate_percentage_figure_present_river(self, percentages_to_validate_crypted):
        all_percentages_crypted = percentages_to_validate_crypted.split("_")
        for percentage_crypted in all_percentages_crypted : 
            data_percentage_crypted = percentage_crypted.split(":")
            name_figure = self.__get_name_figure(data_percentage_crypted[0])
            data_percentage_calculated = str(self.percentage_presence_figure_river[name_figure])
            data_percentage_expected = data_percentage_crypted[1]
            assert(data_percentage_calculated == data_percentage_expected)
           
    def __validate_percentage_figure_present_everywhere(self, percentages_to_validate_crypted):
        all_percentages_crypted = percentages_to_validate_crypted.split("_")
        for percentage_crypted in all_percentages_crypted : 
            data_percentage_crypted = percentage_crypted.split(":")
            name_figure = self.__get_name_figure(data_percentage_crypted[0])
            data_percentage_calculated = str(self.percentage_presence_figure_everywhere[name_figure])
            data_percentage_expected = data_percentage_crypted[1]
            assert(data_percentage_calculated == data_percentage_expected)

    def __validate_percentage_winner_player_river(self, percentages_to_validate_crypted):
        all_percentages_crypted = percentages_to_validate_crypted.split("_")
        for percentage_crypted in all_percentages_crypted : 
            data_percentage_crypted = percentage_crypted.split(":")
            player_name = self.__get_player(data_percentage_crypted[0])
            percentage_calculated = str(self.percentage_winner_players_river[player_name])
            percentage_expected = data_percentage_crypted[1]
            assert(percentage_expected == percentage_calculated)

    def __validate_percentage_winner_player_everywhere(self, percentages_to_validate_crypted):        
        all_percentages_crypted = percentages_to_validate_crypted.split("_")
        for percentage_crypted in all_percentages_crypted : 
            data_percentage_crypted = percentage_crypted.split(":")
            player_name = self.__get_player(data_percentage_crypted[0])
            percentage_calculated = str(self.percentage_winner_players_everywhere[player_name])
            percentage_expected = data_percentage_crypted[1]
            assert(percentage_expected == percentage_calculated)

    def __validate_percentage_figure_winner_river(self, percentages_to_validate_crypted):
        all_percentages_crypted = percentages_to_validate_crypted.split("_")
        for percentage_crypted in all_percentages_crypted : 
            data_percentage_crypted = percentage_crypted.split(":")
            name_figure = self.__get_name_figure(data_percentage_crypted[0])
            percentage_expected = data_percentage_crypted[1]
            percentage_calculated = str(self.percentage_winning_figure_river[name_figure])
            assert(percentage_expected == percentage_calculated)
        

    def __validate_percentage_figure_winner_everywhere(self, percentages_to_validate_crypted):
        all_percentages_crypted = percentages_to_validate_crypted.split("_")
        for percentage_crypted in all_percentages_crypted : 
            data_percentage_crypted = percentage_crypted.split(":")
            name_figure = self.__get_name_figure(data_percentage_crypted[0])
            percentage_expected = data_percentage_crypted[1]
            percentage_calculated = str(self.percentage_winning_figure_everywhere[name_figure])
            assert(percentage_expected == percentage_calculated)

    def __get_name_figure(self, percentage_crypted_name): 
        name_figure = ""
        if percentage_crypted_name == "PA": 
            name_figure = PairFigure.__name__
        elif percentage_crypted_name == "HI":
            name_figure = HighCardFigure.__name__
        elif percentage_crypted_name == "TK":
            name_figure = ThreeOfKindFigure.__name__
        elif percentage_crypted_name == "QF":
            name_figure = QuinteFlushFigure.__name__
        elif percentage_crypted_name == "FU":
            name_figure = FullFigure.__name__
        elif percentage_crypted_name == "2P":
            name_figure = TwoPairFigure.__name__
        return name_figure