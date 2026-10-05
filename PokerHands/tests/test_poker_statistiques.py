from PokerHands.statistiques.poker_statistiques import PokerStatistiques
from PokerHands.statistiques.statistiques_presence_figures import StatistiquesPresenceFigures
from PokerHands.statistiques.statistiques_win_figures import StatistiquesWinFigures
from PokerHands.statistiques.statistiques_winners_players import StatistiquesWinnerPlayers
from PokerHands.tests.dsl.dsl_game_result import convert_game_result_crypted
from PokerHands.tests.dsl.dsl_figure import get_name_figure_from_initial
from PokerHands.tests.dsl.dsl_player import get_player

def test_calculate_poker_satistiques():
    (StatistiquesDriver()
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

class StatistiquesDriver : 
    def __init__(self):
        self.players = []
        self.games_results = []
        self.statistiques_result = None

    def add_players(self, players_name): 
        for player_name in players_name : 
            self.players.append(player_name)
        return self 
    
    def add_game_result(self, game_result_crypted):
        game_result = convert_game_result_crypted(game_result_crypted, self.players)
        self.games_results.append(game_result)
        return self

    def calculate_percentages(self):
        statistiques = PokerStatistiques(StatistiquesPresenceFigures(self.games_results), StatistiquesWinnerPlayers(self.games_results), StatistiquesWinFigures(self.games_results))
        self.statistiques_result = statistiques.calculate_all_statistiques()
        return self

    def validate_percentage(self, datas_crypted):
        all_datas = datas_crypted.split("|")
        if all_datas[0] == "PRR":
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_presence_figure_river, "figure name")
        elif all_datas[0] == "PRE": 
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_presence_figure_everywhere, "figure name")
        elif all_datas[0] == "WNR":
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_winner_players_river, "player")
        elif all_datas[0] == "WNE":
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_winner_players_everywhere, "player")
        elif all_datas[0] == "WFR":
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_winning_figure_river, "figure name")
        elif all_datas[0] == "WFE":
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_winning_figure_everywhere, "figure name")
        return self

    def __validate_all_percentages_calculated(self, percentages_to_validate_crypted, statistiques_calculated, type_key):
        all_percentages_crypted = percentages_to_validate_crypted.split("_")        
        for percentage_crypted in all_percentages_crypted : 
            data_percentage_crypted = percentage_crypted.split(":")
            key_statistics_calculated = self.__get_key_statistics_calculated(type_key, data_percentage_crypted[0])
            data_percentage_calculated = str(statistiques_calculated[key_statistics_calculated])
            data_percentage_expected = data_percentage_crypted[1]
            assert(data_percentage_calculated == data_percentage_expected)

    def __get_key_statistics_calculated(self, type_key, key_percentage_crypted): 
        if type_key == "figure name":
            return get_name_figure_from_initial(key_percentage_crypted)
        else :
            return get_player(self.players, key_percentage_crypted)